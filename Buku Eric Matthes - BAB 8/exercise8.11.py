def send_messages(daftar_pesan, pesan_terkirim):
    """Cetak tiap pesan, lalu pindahkan ke list pesan terkirim."""
    while daftar_pesan:
        pesan_saat_ini = daftar_pesan.pop()
        print(f"Mengirim pesan: {pesan_saat_ini}")
        pesan_terkirim.append(pesan_saat_ini)


pesan_teks = [
    "Halo, apa kabar?",
    "Jangan lupa kumpul tugas hari ini.",
    "Nanti malam jadi belajar bareng?",
]
pesan_terkirim = []

send_messages(pesan_teks[:], pesan_terkirim)

print("\nIsi pesan_teks:")
print(pesan_teks)

print("\nIsi pesan_terkirim:")
print(pesan_terkirim)