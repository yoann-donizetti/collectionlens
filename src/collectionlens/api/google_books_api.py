"""google_books_api.py

Module d'interaction avec l'API Google Books.

Ce module permet de :
- rechercher des livres ;
- récupérer des métadonnées ;
- normaliser les résultats ;
- rechercher un livre par ISBN.
"""

import os

import requests
from dotenv import load_dotenv


load_dotenv()

GOOGLE_BOOKS_API_URL = "https://www.googleapis.com/books/v1/volumes"
API_KEY = os.getenv("GOOGLE_BOOKS_API_KEY")


def search_books(query: str, max_results: int = 40) -> dict:
    """
    Recherche des livres via Google Books API.

    Args:
        query: Requête de recherche.
        max_results: Nombre maximum de résultats.

    Returns:
        Dictionnaire contenant :
        - items : liste de livres normalisés ;
        - error : code erreur éventuel ;
        - status_code : code HTTP éventuel.
    """
    params = {
        "q": query,
        "maxResults": max_results,
        "langRestrict": "fr",
        "printType": "books",
    }

    if API_KEY:
        params["key"] = API_KEY

    try:
        response = requests.get(
            GOOGLE_BOOKS_API_URL,
            params=params,
            timeout=10,
        )

        if response.status_code == 429:
            return {
                "items": [],
                "error": "quota_exceeded",
                "status_code": response.status_code,
            }

        response.raise_for_status()

    except requests.Timeout:
        return {
            "items": [],
            "error": "timeout",
            "status_code": None,
        }

    except requests.RequestException as error:
        return {
            "items": [],
            "error": f"request_error: {error}",
            "status_code": None,
        }

    data = response.json()
    items = data.get("items", [])

    if not items:
        return {
            "items": [],
            "error": "no_result",
            "status_code": response.status_code,
        }

    return {
        "items": [normalize_book(item) for item in items],
        "error": None,
        "status_code": response.status_code,
    }


def search_book_by_isbn(isbn: str) -> dict:
    """
    Recherche un livre dans Google Books à partir d'un ISBN.

    Args:
        isbn: ISBN 10 ou ISBN 13.

    Returns:
        Dictionnaire normalisé avec found/error.
    """
    response = search_books(
        query=f"isbn:{isbn}",
        max_results=1,
    )

    results = response["items"]
    error = response["error"]
    status_code = response["status_code"]

    if error:
        return {
            "source": "google_books",
            "isbn_query": isbn,
            "found": False,
            "error": error,
            "status_code": status_code,
        }

    result = results[0]
    result["found"] = True
    result["error"] = None
    result["status_code"] = status_code
    result["isbn_query"] = isbn

    return result


def normalize_book(item: dict) -> dict:
    """
    Normalise les données d'un livre retourné par Google Books.

    Args:
        item: Résultat brut retourné par Google Books.

    Returns:
        Dictionnaire normalisé exploitable dans CollectionLens.
    """
    volume_info = item.get("volumeInfo", {})
    image_links = volume_info.get("imageLinks", {})

    return {
        "source": "google_books",
        "source_id": item.get("id"),
        "google_books_id": item.get("id"),
        "isbn": extract_isbn(volume_info),
        "title": volume_info.get("title"),
        "subtitle": volume_info.get("subtitle"),
        "authors": volume_info.get("authors", []),
        "publisher": volume_info.get("publisher"),
        "published_date": volume_info.get("publishedDate"),
        "language": volume_info.get("language"),
        "description": volume_info.get("description"),
        "categories": volume_info.get("categories", []),
        "thumbnail": image_links.get("thumbnail"),
        "page_count": volume_info.get("pageCount"),
        "print_type": volume_info.get("printType"),
        "maturity_rating": volume_info.get("maturityRating"),
        "average_rating": volume_info.get("averageRating"),
        "ratings_count": volume_info.get("ratingsCount"),
        "preview_link": volume_info.get("previewLink"),
        "info_link": volume_info.get("infoLink"),
        "canonical_volume_link": volume_info.get("canonicalVolumeLink"),
        "industry_identifiers": volume_info.get("industryIdentifiers", []),
        "raw_data": item,
    }


def extract_isbn(volume_info: dict) -> str | None:
    """
    Extrait l'ISBN depuis les informations Google Books.

    Args:
        volume_info: Dictionnaire volumeInfo.

    Returns:
        ISBN 13 si disponible, sinon ISBN 10, sinon None.
    """
    identifiers = volume_info.get("industryIdentifiers", [])

    isbn_10 = None

    for identifier in identifiers:
        identifier_type = identifier.get("type")
        value = identifier.get("identifier")

        if identifier_type == "ISBN_13":
            return value

        if identifier_type == "ISBN_10":
            isbn_10 = value

    return isbn_10