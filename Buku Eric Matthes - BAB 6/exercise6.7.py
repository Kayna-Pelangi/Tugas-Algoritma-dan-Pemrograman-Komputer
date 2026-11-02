orang_1 = {
    "nama_depan": "Kayna",
    "nama_belakang": "Maulana",
    "umur": 18,
    "kota": "Bekasi",
}

orang_2 = {
    "nama_depan": "Vania",
    "nama_belakang": "Ramadhani",
    "umur": 19,
    "kota": "Yogyakarta",
}

orang_3 = {
    "nama_depan": "Nayla",
    "nama_belakang": "Saputri",
    "umur": 18,
    "kota": "Solo",
}

people = [orang_1, orang_2, orang_3]

for orang in people:
    print(f"Nama: {orang['nama_depan']} {orang['nama_belakang']}")
    print(f"Umur: {orang['umur']}")
    print(f"Kota: {orang['kota']}\n")