def describe_city(kota, negara="Indonesia"):
    """Tampilkan kalimat sederhana tentang sebuah kota."""
    print(f"{kota.title()} ada di {negara}.")


describe_city("bekasi")
describe_city("surakarta")
describe_city("tokyo", "Jepang")