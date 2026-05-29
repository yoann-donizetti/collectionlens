"""isbn_pipeline.py

Pipeline de récupération des métadonnées ISBN.
"""

import json
from collections.abc import Callable
from datetime import datetime, timezone
from pathlib import Path


SearchFunction = Callable[[str], dict]


def fetch_isbn_metadata(
    isbn: str,
    sources: dict[str, SearchFunction],
    raw_output_dir: Path | None = None,
) -> dict:
    """
    Récupère les métadonnées d'un ISBN depuis plusieurs sources.
    """
    results = {
        "isbn_query": isbn,
        "retrieved_at": datetime.now(timezone.utc).isoformat(),
        "sources": {},
    }

    for source_name, search_func in sources.items():
        source_result = search_func(isbn)

        results["sources"][source_name] = source_result

        if raw_output_dir is not None:
            save_raw_result_json(
                isbn=isbn,
                source_name=source_name,
                result=source_result,
                output_dir=raw_output_dir,
            )

    return results


def fetch_many_isbns_metadata(
    isbns: list[str],
    sources: dict[str, SearchFunction],
    raw_output_dir: Path | None = None,
) -> list[dict]:
    """
    Récupère les métadonnées de plusieurs ISBN depuis plusieurs sources.
    """
    return [
        fetch_isbn_metadata(
            isbn=isbn,
            sources=sources,
            raw_output_dir=raw_output_dir,
        )
        for isbn in isbns
    ]


def save_raw_result_json(
    isbn: str,
    source_name: str,
    result: dict,
    output_dir: Path,
) -> Path:
    """
    Sauvegarde le résultat brut d'une source au format JSON.

    Args:
        isbn: ISBN recherché.
        source_name: Nom de la source.
        result: Résultat retourné par la source.
        output_dir: Dossier racine de sauvegarde.

    Returns:
        Chemin du fichier JSON généré.
    """
    source_output_dir = output_dir / source_name
    source_output_dir.mkdir(parents=True, exist_ok=True)

    output_path = source_output_dir / f"{isbn}.json"

    payload = {
        "isbn_query": isbn,
        "source": source_name,
        "saved_at": datetime.now(timezone.utc).isoformat(),
        "result": result,
    }

    with output_path.open("w", encoding="utf-8") as file:
        json.dump(
            payload,
            file,
            ensure_ascii=False,
            indent=2,
            default=str,
        )

    return output_path