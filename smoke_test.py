from __future__ import annotations

import os
import importlib
import sys
from pathlib import Path


REQUIRED_MODULES = [
    "ipaddress",
    "numpy",
    "pandas",
    "matplotlib",
    "seaborn",
    "sklearn",
]

DATASET_NAME = "unbalaced_20_80_dataset.csv"


def main() -> int:
    project_root = Path(__file__).resolve().parent
    dataset_path = project_root / DATASET_NAME
    mpl_config_dir = project_root / ".mplconfig"
    ipython_dir = project_root / ".ipython"
    mpl_config_dir.mkdir(exist_ok=True)
    ipython_dir.mkdir(exist_ok=True)
    os.environ.setdefault("MPLCONFIGDIR", str(mpl_config_dir))
    os.environ.setdefault("IPYTHONDIR", str(ipython_dir))

    print("Checking Python dependencies...")
    missing: list[str] = []
    for module_name in REQUIRED_MODULES:
        try:
            importlib.import_module(module_name)
            print(f"  OK  {module_name}")
        except ModuleNotFoundError:
            print(f"  MISSING  {module_name}")
            missing.append(module_name)

    if missing:
        print("\nInstall the missing packages with:")
        print("  pip install -r requirements.txt")
        return 1

    print("\nChecking dataset...")
    print(f"  Expected file: {dataset_path}")
    if not dataset_path.exists():
        print("  MISSING dataset file")
        print(
            "  Download the Kaggle dataset and place the expected CSV in the project root."
        )
        return 2

    print("  OK dataset file found")

    import pandas as pd

    try:
        df = pd.read_csv(dataset_path, nrows=5)
    except Exception as exc:  # pragma: no cover - diagnostic path
        print(f"  FAILED to read dataset: {exc}")
        return 3

    print(f"  OK dataset readable, sample shape: {df.shape}")
    print(f"  Columns loaded: {len(df.columns)}")

    required_columns = {"Src IP", "Dst IP", "Label"}
    missing_columns = sorted(required_columns - set(df.columns))
    if missing_columns:
        print(f"  WARNING missing expected columns: {', '.join(missing_columns)}")
        return 4

    print("\nSmoke test passed. The notebook should be ready to run.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
