"""bnf_api.py

Module d'interaction avec l'API SRU de la BNF.

Ce module permet de :
- rechercher des ouvrages par ISBN ;
- récupérer des métadonnées bibliographiques ;
- normaliser les résultats ;
- capturer les erreurs API.
"""

import xmltodict

import requests


BNF_API_URL = "https://catalogue.bnf.fr/api/SRU"


def search_book_by_isbn(isbn: str) -> dict:
    """
    Recherche un ouvrage dans la BNF à partir d'un ISBN.

    Args:
        isbn: ISBN 10 ou ISBN 13.

    Returns:
        Dictionnaire normalisé contenant les métadonnées ou une erreur.
    """
    params = {
        "version": "1.2",
        "operation": "searchRetrieve",
        "query": f'bib.isbn="{isbn}"',
        "recordSchema": "dublincore",
        "maximumRecords": 1,
    }

    try:
        response = requests.get(
            BNF_API_URL,
            params=params,
            timeout=15,
        )

        if response.status_code == 429:
            return build_not_found_result(
                isbn=isbn,
                error="quota_exceeded",
                status_code=response.status_code,
            )

        response.raise_for_status()

    except requests.Timeout:
        return build_not_found_result(
            isbn=isbn,
            error="timeout",
            status_code=None,
        )

    except requests.RequestException as error:
        return build_not_found_result(
            isbn=isbn,
            error=f"request_error: {error}",
            status_code=None,
        )

    try:
        data = xmltodict.parse(response.text)

    except Exception as error:
        return build_not_found_result(
            isbn=isbn,
            error=f"xml_parsing_error: {error}",
            status_code=response.status_code,
        )

    response_data = data.get(
        "srw:searchRetrieveResponse",
        {},
    )

    records_container = response_data.get("srw:records")

    if not records_container:
        return build_not_found_result(
            isbn=isbn,
            error="no_result",
            status_code=response.status_code,
        )

    records = records_container.get("srw:record")

    if isinstance(records, list):
        record = records[0]

    else:
        record = records

    return normalize_book(
        record=record,
        isbn_query=isbn,
        status_code=response.status_code,
    )


def normalize_book(
    record: dict,
    isbn_query: str,
    status_code: int | None,
) -> dict:
    """
    Normalise un résultat BNF Dublin Core.

    Args:
        record: Record XML converti en dictionnaire.
        isbn_query: ISBN recherché.
        status_code: Code HTTP de la réponse.

    Returns:
        Dictionnaire normalisé.
    """
    record_data = (
        record
        .get("srw:recordData", {})
        .get("oai_dc:dc", {})
    )

    return {
        "source": "bnf",
        "isbn_query": isbn_query,
        "found": True,
        "error": None,
        "status_code": status_code,

        "source_id": extract_first(
            record_data.get("dc:identifier")
        ),

        "isbn": isbn_query,

        "title": extract_first(
            record_data.get("dc:title")
        ),

        "subtitle": None,

        "authors": ensure_list(
            record_data.get("dc:creator")
        ),

        "publisher": extract_first(
            record_data.get("dc:publisher")
        ),

        "published_date": extract_first(
            record_data.get("dc:date")
        ),

        "language": extract_first(
            record_data.get("dc:language")
        ),

        "description": extract_first(
            record_data.get("dc:description")
        ),

        "categories": [],

        "thumbnail": None,

        "page_count": None,

        "print_type": "BOOK",

        "maturity_rating": None,
        "average_rating": None,
        "ratings_count": None,

        "preview_link": None,
        "info_link": None,
        "canonical_volume_link": None,

        "industry_identifiers": ensure_list(
            record_data.get("dc:identifier")
        ),

        "format": extract_first(
            record_data.get("dc:format")
        ),

        "types": ensure_list(
            record_data.get("dc:type")
        ),

        "rights": ensure_list(
            record_data.get("dc:rights")
        ),

        "raw_data": record,
    }


def ensure_list(value) -> list:
    """
    Convertit une valeur en liste homogène.
    """
    if value is None:
        return []

    if isinstance(value, list):
        return value

    return [value]


def extract_first(value) -> str | None:
    """
    Extrait la première valeur texte.
    """
    if value is None:
        return None

    if isinstance(value, list):
        return value[0]

    return value


def build_not_found_result(
    isbn: str,
    error: str,
    status_code: int | None,
) -> dict:
    """
    Construit un résultat standardisé pour une erreur ou un ISBN absent.
    """
    return {
        "source": "bnf",
        "isbn_query": isbn,
        "found": False,
        "error": error,
        "status_code": status_code,
    }