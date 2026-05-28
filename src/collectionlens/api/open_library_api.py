"""open_library_api.py

Module d'interaction avec l'API OpenLibrary.

Ce module permet de :
- rechercher des livres par ISBN ;
- récupérer des métadonnées bibliographiques ;
- normaliser les résultats ;
- capturer les erreurs sans interrompre le pipeline.
"""

import requests


OPEN_LIBRARY_API_URL = "https://openlibrary.org/api/books"


def search_book_by_isbn(isbn: str) -> dict:
    """
    Recherche un livre dans OpenLibrary à partir d'un ISBN.

    Args:
        isbn: ISBN 10 ou ISBN 13.

    Returns:
        Dictionnaire normalisé avec found/error.
    """
    params = {
        "bibkeys": f"ISBN:{isbn}",
        "format": "json",
        "jscmd": "data",
    }

    try:
        response = requests.get(
            OPEN_LIBRARY_API_URL,
            params=params,
            timeout=10,
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

    data = response.json()
    key = f"ISBN:{isbn}"

    if key not in data:
        return build_not_found_result(
            isbn=isbn,
            error="no_result",
            status_code=response.status_code,
        )

    return normalize_book(
        item=data[key],
        isbn_query=isbn,
        status_code=response.status_code,
    )


def normalize_book(item: dict, isbn_query: str, status_code: int | None) -> dict:
    """
    Normalise les données d'un livre retourné par OpenLibrary.

    Args:
        item: Résultat brut retourné par OpenLibrary.
        isbn_query: ISBN recherché.
        status_code: Code HTTP de la réponse.

    Returns:
        Dictionnaire normalisé exploitable dans CollectionLens.
    """
    authors = [
        author.get("name")
        for author in item.get("authors", [])
        if author.get("name")
    ]

    publishers = [
        publisher.get("name")
        for publisher in item.get("publishers", [])
        if publisher.get("name")
    ]

    subjects = [
        subject.get("name")
        for subject in item.get("subjects", [])
        if subject.get("name")
    ]

    cover = item.get("cover", {})

    return {
        "source": "openlibrary",
        "isbn_query": isbn_query,
        "found": True,
        "error": None,
        "status_code": status_code,
        "source_id": item.get("key"),
        "openlibrary_key": item.get("key"),
        "isbn": isbn_query,
        "title": item.get("title"),
        "subtitle": item.get("subtitle"),
        "authors": authors,
        "publisher": publishers[0] if publishers else None,
        "publishers": publishers,
        "published_date": item.get("publish_date"),
        "language": None,
        "description": extract_description(item),
        "categories": subjects,
        "thumbnail": cover.get("medium") or cover.get("large") or cover.get("small"),
        "page_count": item.get("number_of_pages"),
        "print_type": "BOOK",
        "maturity_rating": None,
        "average_rating": None,
        "ratings_count": None,
        "preview_link": item.get("url"),
        "info_link": item.get("url"),
        "canonical_volume_link": item.get("url"),
        "industry_identifiers": item.get("identifiers", {}),
        "raw_data": item,
    }


def extract_description(item: dict) -> str | None:
    """
    Extrait la description depuis un résultat OpenLibrary.

    Args:
        item: Résultat brut OpenLibrary.

    Returns:
        Description si disponible, sinon None.
    """
    description = item.get("description")

    if isinstance(description, dict):
        return description.get("value")

    if isinstance(description, str):
        return description

    return None


def build_not_found_result(
    isbn: str,
    error: str,
    status_code: int | None,
) -> dict:
    """
    Construit un résultat normalisé pour un ISBN non trouvé ou en erreur.
    """
    return {
        "source": "openlibrary",
        "isbn_query": isbn,
        "found": False,
        "error": error,
        "status_code": status_code,
    }