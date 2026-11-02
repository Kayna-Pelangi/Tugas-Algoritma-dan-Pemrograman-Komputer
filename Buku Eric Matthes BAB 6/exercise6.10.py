angka_favorit = {
    "Kayna": [7, 11],
    "Vania": [2],
    "Rastiva": [21, 5, 8],
    "Nayla": [9, 1],
    "Windi": [14, 2],
}

for nama, daftar_angka in angka_favorit.items():
    print(f"Angka favorit {nama}:")
    for angka in daftar_angka:
        print(f"    {angka}")
    print()