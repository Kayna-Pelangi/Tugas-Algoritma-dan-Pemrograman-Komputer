import json
from pathlib import Path

# Mendapatkan jalur folder tempat skrip berada
folder = Path(__file__).resolve().parent
filepath = folder / 'favorite_number.json'

favorite_number = input("Masukkan angka favorit Anda: ")

# Menyimpan angka ke dalam berkas json
with open(filepath, 'w') as file:
    json.dump(favorite_number, file)

print("Angka favorit Anda telah disimpan!")