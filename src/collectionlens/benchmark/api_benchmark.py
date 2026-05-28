import pandas as pd


def build_source_table(
    source_name: str,
    search_func,
    isbns: list[str],
) -> pd.DataFrame:
    """
    Lance un benchmark générique sur une source bibliographique.

    Args:
        source_name: Nom de la source benchmarkée.
        search_func: Fonction de recherche ISBN.
        isbns: Liste des ISBN à tester.

    Returns:
        DataFrame contenant les résultats du benchmark.
    """
    rows = []

    for isbn in isbns:
        result = search_func(isbn)
        rows.append(result)

    df = pd.DataFrame(rows)

    df["source"] = source_name

    return df