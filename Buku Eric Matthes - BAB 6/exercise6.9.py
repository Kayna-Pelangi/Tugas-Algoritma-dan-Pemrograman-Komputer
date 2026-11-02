tempat_favorit = {
    "Kayna": ["Bekasi", "Jakarta"],
    "Vania": ["Yogyakarta"],
    "Nayla": ["Yogyakarta"],
}

for nama, daftar_tempat in tempat_favorit.items():
    print(f"Tempat favorit {nama}:")
    for tempat in daftar_tempat:
        print(f"    {tempat}")
    print()