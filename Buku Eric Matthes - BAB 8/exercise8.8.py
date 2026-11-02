def make_album(artis, judul, jumlah_lagu=None):
    """Kembalikan dictionary berisi informasi album."""
    album = {"artis": artis, "judul": judul}
    if jumlah_lagu:
        album["jumlah_lagu"] = jumlah_lagu
    return album


while True:
    print("\nMasukkan data album:")
    print("(ketik 'q' kapan saja untuk berhenti)")

    nama_artis = input("Nama artis: ")
    if nama_artis == "q":
        break

    judul_album = input("Judul album: ")
    if judul_album == "q":
        break

    album = make_album(nama_artis, judul_album)
    print(album)