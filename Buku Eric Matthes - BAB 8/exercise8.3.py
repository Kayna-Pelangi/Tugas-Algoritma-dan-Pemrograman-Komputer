def make_shirt(ukuran, tulisan):
    """Tampilkan ringkasan ukuran dan tulisan di kaos."""
    print(f"Ukuran kaos: {ukuran}. Tulisan di kaos: '{tulisan}'.")


# Argumen posisional
make_shirt("L", "Teknik Industri UNS")

# Argumen keyword
make_shirt(ukuran="M", tulisan="TI '26")