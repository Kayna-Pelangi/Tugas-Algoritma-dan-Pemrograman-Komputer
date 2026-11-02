def show_messages(daftar_pesan):
    """Tampilkan setiap pesan di dalam list."""
    for pesan in daftar_pesan:
        print(pesan)


pesan_teks = [
    "Halo, apa kabar?",
    "Jangan lupa kumpul tugas hari ini.",
    "Nanti malam jadi belajar bareng?",
]

show_messages(pesan_teks)