kota = {
    "jakarta": {
        "negara": "Indonesia",
        "populasi": 10600000,
        "fakta": "Ibu kota Indonesia dengan MRT pertama di Indonesia.",
    },
    "tokyo": {
        "negara": "Jepang",
        "populasi": 14000000,
        "fakta": "Salah satu kota terpadat di dunia.",
    },
    "paris": {
        "negara": "Prancis",
        "populasi": 2100000,
        "fakta": "Menara Eiffel berdiri di kota ini.",
    },
}

for nama_kota, info in kota.items():
    print(f"Kota: {nama_kota.title()}")
    print(f"    Negara: {info['negara']}")
    print(f"    Populasi: {info['populasi']}")
    print(f"    Fakta: {info['fakta']}\n")