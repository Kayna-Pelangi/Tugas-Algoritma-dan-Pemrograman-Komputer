def make_album(artis, judul, jumlah_lagu=None):
    """Kembalikan dictionary berisi informasi album."""
    album = {"artis": artis, "judul": judul}
    if jumlah_lagu:
        album["jumlah_lagu"] = jumlah_lagu
    return album


album_1 = make_album("Hindia", "Menari dengan Bayangan")
album_2 = make_album("Tulus", "Monokrom")
album_3 = make_album("Nadin Amizah", "Selamat Ulang Tahun", 10)

print(album_1)
print(album_2)
print(album_3)