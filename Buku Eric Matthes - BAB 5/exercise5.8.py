daftar_pengguna = ["Admin", "Kayna", "Vania", "Rastiva", "Nayla"]

for pengguna in daftar_pengguna:
    if pengguna == "Admin":
        print("Halo Admin, apakah Anda ingin melihat laporan status?")
    else:
        print(f"Halo {pengguna}, terima kasih sudah login kembali.")