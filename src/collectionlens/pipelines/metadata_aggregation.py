"""metadata_aggregation.py

Pipeline d'agrégation des métadonnées multi-sources.

Ce module permet de :
- fusionner les résultats issus de plusieurs sources bibliographiques ;
- appliquer les règles de priorité définies pour CollectionLens ;
- produire une fiche ouvrage unique ;
- conserver la traçabilité des sources utilisées.
"""

from typing import Any


def is_empty(value: Any) -> bool:
    """
    Vérifie si une valeur est vide ou inexploitable.
    """
    if value is None:
        return True

    if value == "":
        return True

    if value == []:
        return True

    return False


def select_first_available(
    candidates: list[tuple[str, Any]],
) -> tuple[Any, str | None]:
    """
    Retourne la première valeur disponible avec sa source.

    Args:
        candidates: Liste de tuples (source, valeur).

    Returns:
        Tuple contenant :
        - la valeur retenue ;
        - le nom de la source utilisée.
    """
    for source_name, value in candidates:
        if not is_empty(value):
            return value, source_name

    return None, None


def aggregate_book_metadata(
    sources_data: dict[str, dict[str, Any]],
) -> dict[str, Any]:
    """
    Agrège les métadonnées d'un ouvrage à partir des sources disponibles.

    Args:
        sources_data: Dictionnaire contenant les résultats par source.

    Returns:
        Fiche ouvrage agrégée.
    """
    nudger = sources_data.get("nudger", {})
    google_books = sources_data.get("google_books", {})
    bnf = sources_data.get("bnf", {})
    openlibrary = sources_data.get("openlibrary", {})

    title, title_source = select_first_available(
        [
            ("nudger", nudger.get("title")),
            ("google_books", google_books.get("title")),
            ("bnf", bnf.get("title")),
        ]
    )

    authors, authors_source = select_first_available(
        [
            ("google_books", google_books.get("authors")),
            ("bnf", bnf.get("authors")),
        ]
    )

    publisher, publisher_source = select_first_available(
        [
            ("nudger", nudger.get("publisher")),
            ("bnf", bnf.get("publisher")),
            ("google_books", google_books.get("publisher")),
        ]
    )

    published_date, published_date_source = select_first_available(
        [
            ("google_books", google_books.get("published_date")),
            ("bnf", bnf.get("published_date")),
        ]
    )

    description, description_source = select_first_available(
        [
            ("google_books", google_books.get("description")),
            ("bnf", bnf.get("description")),
        ]
    )

    categories, categories_source = select_first_available(
        [
            ("nudger", nudger.get("categories")),
            ("google_books", google_books.get("categories")),
            ("openlibrary", openlibrary.get("categories")),
        ]
    )

    page_count, page_count_source = select_first_available(
        [
            ("nudger", nudger.get("page_count")),
            ("google_books", google_books.get("page_count")),
            ("bnf", bnf.get("page_count")),
        ]
    )

    format_value, format_source = select_first_available(
        [
            ("nudger", nudger.get("format")),
            ("bnf", bnf.get("format")),
        ]
    )

    cover_url, cover_url_source = select_first_available(
        [
            ("google_books", google_books.get("thumbnail")),
            ("openlibrary", openlibrary.get("cover_large")),
            ("openlibrary", openlibrary.get("thumbnail")),
        ]
    )

    bnf_ark, bnf_ark_source = select_first_available(
        [
            ("bnf", bnf.get("bnf_ark")),
        ]
    )

    return {
        "isbn": select_first_available(
            [
                ("nudger", nudger.get("isbn")),
                ("google_books", google_books.get("isbn")),
                ("bnf", bnf.get("isbn_query")),
                ("openlibrary", openlibrary.get("isbn")),
            ]
        )[0],
        "title": title,
        "title_source": title_source,
        "authors": authors,
        "authors_source": authors_source,
        "publisher": publisher,
        "publisher_source": publisher_source,
        "published_date": published_date,
        "published_date_source": published_date_source,
        "description": description,
        "description_source": description_source,
        "categories": categories,
        "categories_source": categories_source,
        "page_count": page_count,
        "page_count_source": page_count_source,
        "format": format_value,
        "format_source": format_source,
        "cover_url": cover_url,
        "cover_url_source": cover_url_source,
        "bnf_ark": bnf_ark,
        "bnf_ark_source": bnf_ark_source,
    }