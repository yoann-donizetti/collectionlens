"""nudger_dataset.py

Module d'interaction avec le dataset local Nudger.

Ce module permet de :
- charger un fichier CSV Nudger ;
- nettoyer les ISBN/EAN ;
- rechercher un ouvrage par ISBN ;
- normaliser les résultats pour les benchmarks CollectionLens.
"""

from pathlib import Path

import pandas as pd


def clean_isbn(isbn: str | int | float | None) -> str | None:
    """
    Nettoie un ISBN/EAN pour faciliter les comparaisons.
    """
    if pd.isna(isbn):
        return None

    return (
        str(isbn)
        .replace("-", "")
        .replace(" ", "")
        .strip()
    )


def load_nudger_dataset(
    csv_path: str | Path,
    isbn_column: str = "isbn",
) -> pd.DataFrame:
    """
    Charge le dataset Nudger et ajoute une colonne ISBN nettoyée.
    """
    df = pd.read_csv(
        csv_path,
        dtype=str,
        low_memory=False,
    )

    if isbn_column not in df.columns:
        raise ValueError(
            f"Colonne ISBN introuvable dans le fichier Nudger : {isbn_column}"
        )

    df["isbn_clean"] = df[isbn_column].apply(clean_isbn)

    return df


def search_book_by_isbn_from_dataframe(
    isbn: str,
    df_nudger: pd.DataFrame,
) -> dict:
    """
    Recherche un ISBN dans le dataset Nudger déjà chargé.

    Args:
        isbn: ISBN/EAN recherché.
        df_nudger: DataFrame Nudger chargé.

    Returns:
        Dictionnaire normalisé avec found/error.
    """
    clean_value = clean_isbn(isbn)

    if clean_value is None:
        return build_not_found_result(
            isbn=isbn,
            error="invalid_isbn",
        )

    matches = df_nudger[df_nudger["isbn_clean"] == clean_value]

    if matches.empty:
        return build_not_found_result(
            isbn=isbn,
            error="no_result",
        )

    row = matches.iloc[0]

    return {
        "source": "nudger",
        "isbn_query": isbn,
        "found": True,
        "error": None,
        "status_code": None,
        "source_id": clean_value,
        "isbn": clean_value,
        "title": get_optional_value(row, "title"),
        "subtitle": None,
        "authors": [],
        "publisher": get_optional_value(row, "editeur"),
        "published_date": None,
        "language": None,
        "description": None,
        "categories": build_categories(row),
        "thumbnail": None,
        "page_count": get_optional_value(row, "nb_page"),
        "print_type": get_optional_value(row, "format"),
        "maturity_rating": None,
        "average_rating": None,
        "ratings_count": None,
        "preview_link": get_optional_value(row, "url"),
        "info_link": get_optional_value(row, "url"),
        "canonical_volume_link": get_optional_value(row, "url"),
        "industry_identifiers": [],
        "url": get_optional_value(row, "url"),
        "format": get_optional_value(row, "format"),
        "offers_count": get_optional_value(row, "offers_count"),
        "min_price": get_optional_value(row, "min_price"),
        "currency": get_optional_value(row, "currency"),
        "last_updated": get_optional_value(row, "last_updated"),
        "raw_data": row.to_dict(),
    }


def build_nudger_search_function(df_nudger: pd.DataFrame):
    """
    Construit une fonction compatible avec le benchmark.

    Le benchmark attend une fonction :

    search_func(isbn)

    Nudger étant un dataset local, cette fonction crée un wrapper
    autour du DataFrame chargé.
    """

    def search_book_by_isbn(isbn: str) -> dict:
        return search_book_by_isbn_from_dataframe(
            isbn=isbn,
            df_nudger=df_nudger,
        )

    return search_book_by_isbn


def get_optional_value(
    row: pd.Series,
    column_name: str,
) -> str | None:
    """
    Récupère une valeur optionnelle dans une ligne pandas.
    """
    value = row.get(column_name)

    if pd.isna(value) or value == "":
        return None

    return value


def build_categories(row: pd.Series) -> list[str]:
    """
    Construit la liste des catégories Nudger.
    """
    categories = []

    for column in ["souscategorie", "souscategorie2"]:
        value = get_optional_value(row, column)

        if value:
            categories.append(value)

    return categories


def build_not_found_result(
    isbn: str,
    error: str,
) -> dict:
    """
    Construit un résultat standardisé pour un ISBN absent ou invalide.
    """
    return {
        "source": "nudger",
        "isbn_query": isbn,
        "found": False,
        "error": error,
        "status_code": None,
    }