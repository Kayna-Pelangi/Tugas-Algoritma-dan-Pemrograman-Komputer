import json
from pathlib import Path

folder = Path(__file__).resolve().parent
filepath = folder / 'favorite_number.json'

try:
    with open(filepath, 'r') as file:
        number = json.load(file)
except FileNotFoundError:
    # Jika berkas belum ada, minta input dan simpan
    number = input("Masukkan angka favorit Anda: ")
    with open(filepath, 'w') as file:
        json.dump(number, file)
    print("Angka favorit Anda telah berhasil disimpan!")
else:
    # Jika berkas sudah ada, langsung tampilkan
    print(f"I know your favorite number! It's {number}.")