"""Configuración de rutas del proyecto."""

from pathlib import Path
import yaml

# Raíz del proyecto: carpeta que contiene src/, notebooks/, config/, etc.
PROJECT_ROOT = Path(__file__).resolve().parents[1]

# Ruta al archivo YAML con las rutas de datos
CONFIG_PATH = PROJECT_ROOT / "config" / "path.yaml"  # o "paths.yaml" si lo nombraste así

with open(CONFIG_PATH, "r", encoding="utf-8") as f:
    PATHS = yaml.safe_load(f)

PROJECT_DATA_ROOT = Path(PATHS["project_data_root"]).expanduser().resolve()
LOCAL_DB_DIR = Path(PATHS["local_db_dir"]).expanduser().resolve()
PROCESSED_DIR = Path(PATHS["processed_dir"]).expanduser().resolve()
RESULTS_EXTERNAL = DATA_ROOT / "results"
TABLES_EXTERNAL = RESULTS_EXTERNAL / "tables"
FIGURES_EXTERNAL = RESULTS_EXTERNAL / "figures"
MODELS_EXTERNAL = RESULTS_EXTERNAL / "models"

if __name__ == "__main__":
    print("PROJECT_ROOT      :", PROJECT_ROOT)
    print("PROJECT_DATA_ROOT :", PROJECT_DATA_ROOT)
    print("LOCAL_DB_DIR      :", LOCAL_DB_DIR)
    print("PROCESSED_DIR     :", PROCESSED_DIR)
    print("RESULTS_EXTERNAL     :", RESULTS_EXTERNAL)
    print("FIGURES_EXTERNAL     :", FIGURES_EXTERNAL)
    print("TABLES_EXTERNAL   :", TABLES_EXTERNAL)
    print("MODELS_EXTERNAL     :", MODELS_EXTERNAL)
    