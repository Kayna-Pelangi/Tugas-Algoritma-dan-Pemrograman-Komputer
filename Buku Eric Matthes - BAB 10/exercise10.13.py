import json
from pathlib import Path

folder = Path(__file__).resolve().parent
filepath = folder / 'user_profile.json'

# Meminta 3 informasi berbeda dari pengguna
user_info = {}
user_info['username'] = input("Masukkan nama pengguna Anda: ")
user_info['hobby'] = input("Apa hobi Anda? ")
user_info['city'] = input("Di kota mana Anda tinggal? ")

# Menyimpan kamus ke berkas JSON
with open(filepath, 'w') as file:
    json.dump(user_info, file)
print("\n[Data berhasil disimpan!]\n")

# Membaca kembali data JSON ke bentuk dictionary
with open(filepath, 'r') as file:
    saved_data = json.load(file)

# Menampilkan ringkasan informasi pengguna
print("Berikut ringkasan profil Anda yang kami ingat:")
print(f"- Nama: {saved_data['username']}")
print(f"- Hobi: {saved_data['hobby']}")
print(f"- Kota: {saved_data['city']}")