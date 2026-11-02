daftar_tamu = ["Tulus", "Albert Einstein", "Nadin Amizah", "Raim Laode", "Hindia", "Pamungkas"]

print("Maaf, meja baru tidak datang tepat waktu. Saya hanya bisa mengundang dua orang.\n")

tamu_dipop = daftar_tamu.pop()
print(f"Maaf {tamu_dipop}, saya tidak bisa mengundang Anda makan malam.")
tamu_dipop = daftar_tamu.pop()
print(f"Maaf {tamu_dipop}, saya tidak bisa mengundang Anda makan malam.")
tamu_dipop = daftar_tamu.pop()
print(f"Maaf {tamu_dipop}, saya tidak bisa mengundang Anda makan malam.")
tamu_dipop = daftar_tamu.pop()
print(f"Maaf {tamu_dipop}, saya tidak bisa mengundang Anda makan malam.\n")

print(f"{daftar_tamu[0]}, Anda masih diundang makan malam.")
print(f"{daftar_tamu[1]}, Anda masih diundang makan malam.\n")

del daftar_tamu[0]
del daftar_tamu[0]

print(daftar_tamu)