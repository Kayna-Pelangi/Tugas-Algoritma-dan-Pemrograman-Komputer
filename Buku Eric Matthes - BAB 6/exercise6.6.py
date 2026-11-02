bahasa_favorit = {
    "nisrina": "python",
    "fayza": "c",
    "isha": "rust",
    "bunga": "python",
}

orang_yang_diundang = ["nisrina", "kayna", "fayza", "vania", "isha", "nayla"]

for orang in orang_yang_diundang:
    if orang in bahasa_favorit.keys():
        print(f"Terima kasih {orang.title()}, sudah mengisi polling.")
    else:
        print(f"{orang.title()}, tolong isi polling kami!")