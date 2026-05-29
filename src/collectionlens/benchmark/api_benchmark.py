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

from math import ceil
from pathlib import Path
import json
import time

import pandas as pd


def benchmark_source_in_batches(
    source_name: str,
    search_func,
    isbns: list[str],
    batch_size: int,
    output_dir: Path,
    sleep_seconds: float = 1.0,
) -> pd.DataFrame:
    """
    Lance un benchmark API par batch avec sauvegarde incrémentale.

    Cette fonction permet :
    - de traiter les ISBN par paquets ;
    - de sauvegarder chaque batch en JSONL ;
    - de reprendre automatiquement les batchs déjà calculés ;
    - d'éviter de perdre les résultats si le notebook est interrompu.
    """
    output_dir.mkdir(parents=True, exist_ok=True)

    total_isbns = len(isbns)
    total_batches = ceil(total_isbns / batch_size)

    all_results = []

    for batch_index in range(total_batches):
        start = batch_index * batch_size
        end = start + batch_size
        batch_isbns = isbns[start:end]

        batch_output_path = (
            output_dir
            / f"{source_name}_batch_{batch_index + 1:03d}.jsonl"
        )

        if batch_output_path.exists():
            batch_df = pd.read_json(
                batch_output_path,
                lines=True,
            )
            all_results.extend(batch_df.to_dict("records"))
            print(
                f"Batch {batch_index + 1}/{total_batches} déjà présent, chargé."
            )
            continue

        print(
            f"Traitement batch {batch_index + 1}/{total_batches} "
            f"({len(batch_isbns)} ISBN)"
        )

        batch_results = []

        for isbn in batch_isbns:
            result = search_func(isbn)
            batch_results.append(result)
            time.sleep(sleep_seconds)

        with batch_output_path.open(
            "w",
            encoding="utf-8",
        ) as file:
            for result in batch_results:
                file.write(
                    json.dumps(
                        result,
                        ensure_ascii=False,
                        default=str,
                    )
                    + "\n"
                )

        all_results.extend(batch_results)

    return pd.DataFrame(all_results)