def make_shirt(ukuran="L", tulisan="Teknik Industri UNS"):
    """Tampilkan ringkasan ukuran dan tulisan di kaos."""
    print(f"Ukuran kaos: {ukuran}. Tulisan di kaos: {tulisan}.")


# Kaos large dengan pesan default
make_shirt()

# Kaos medium dengan pesan default
make_shirt(ukuran="M")

# Kaos ukuran bebas dengan pesan berbeda
make_shirt(ukuran="XL", tulisan="TI '26")