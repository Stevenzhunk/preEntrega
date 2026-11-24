
import csv
import json
from pathlib import Path


# Ruta raíz del proyecto
DATA_DIR = Path(__file__).resolve().parent.parent / "data"


def read_users_csv():
    archivo = DATA_DIR / "users.csv"

    with open(archivo, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        return list(reader)


def read_productos_json():
    archivo = DATA_DIR / "products.json"

    with open(archivo, mode="r", encoding="utf-8") as file:
        return json.load(file)
