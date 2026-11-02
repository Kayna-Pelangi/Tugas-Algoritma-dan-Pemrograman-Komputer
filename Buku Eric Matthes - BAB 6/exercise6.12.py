pesanan = [
    {
        "kerak": "tebal",
        "ukuran": "besar",
        "harga": 85000,
        "topping": ["jamur", "keju ekstra"],
    },
    {
        "kerak": "tipis",
        "ukuran": "sedang",
        "harga": 65000,
        "topping": ["pepperoni", "nanas", "bawang"],
    },
]

total = 0

for nomor, pizza in enumerate(pesanan, start=1):
    print(f"Pesanan {nomor}: pizza {pizza['ukuran']}, "
          f"kerak {pizza['kerak']}")
    print("    Topping:")
    for topping in pizza["topping"]:
        print(f"        {topping}")
    print(f"    Harga: Rp{pizza['harga']}\n")
    total += pizza["harga"]

print(f"Total bayar: Rp{total}")