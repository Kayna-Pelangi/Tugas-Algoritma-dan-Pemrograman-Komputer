import json
from pathlib import Path

folder = Path(__file__).resolve().parent
filepath = folder / 'favorite_number.json'

try:
    with open(filepath, 'r') as file:
        number = json.load(file)
except FileNotFoundError:
    print("Anda belum menyimpan angka favorit!")
else:
    print(f"I know your favorite number! It's {number}.")