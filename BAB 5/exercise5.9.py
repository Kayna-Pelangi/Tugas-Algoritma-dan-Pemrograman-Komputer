daftar_pengguna = []

if daftar_pengguna:
    for pengguna in daftar_pengguna:
        if pengguna == "Admin":
            print("Halo Admin, apakah Anda ingin melihat laporan status?")
        else:
            print(f"Halo {pengguna}, terima kasih sudah login kembali.")
else:
    print("Kita perlu mencari beberapa pengguna!")