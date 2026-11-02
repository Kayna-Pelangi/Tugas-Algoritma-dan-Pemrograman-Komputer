hewan_1 = {"jenis": "kucing", "pemilik": "Kayna"}
hewan_2 = {"jenis": "ikan", "pemilik": "Vania"}
hewan_3 = {"jenis": "kelinci", "pemilik": "Nayla"}

pets = [hewan_1, hewan_2, hewan_3]

for hewan in pets:
    print(f"Jenis hewan: {hewan['jenis']}")
    print(f"Pemilik: {hewan['pemilik']}\n")