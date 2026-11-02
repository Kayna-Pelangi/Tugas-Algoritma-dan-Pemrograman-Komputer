def city_country(kota, negara):
    """Kembalikan string berformat 'Kota, Negara'."""
    return f"{kota.title()}, {negara.title()}"


hasil_1 = city_country("bekasi", "indonesia")
hasil_2 = city_country("surakarta", "indonesia")
hasil_3 = city_country("tokyo", "jepang")

print(hasil_1)
print(hasil_2)
print(hasil_3)