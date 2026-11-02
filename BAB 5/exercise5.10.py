pengguna_saat_ini = ["Admin", "Windi", "Vania", "Rastiva", "Bunga"]
pengguna_baru = ["windi", "Nisrina", "Fayza", "Isha", "BUNGA"]

pengguna_saat_ini_kecil = []
for pengguna in pengguna_saat_ini:
    pengguna_saat_ini_kecil.append(pengguna.lower())

for pengguna in pengguna_baru:
    if pengguna.lower() in pengguna_saat_ini_kecil:
        print(f"Username {pengguna} sudah dipakai, coba yang lain.")
    else:
        print(f"Username {pengguna} tersedia.")