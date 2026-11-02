daftar_negara = ["Monaco", "Jepang", "Singapura", "Arab Saudi"]
print(f"Daftar awal: {daftar_negara}")

# Mengakses elemen lewat indeks
print(f"Negara pertama: {daftar_negara[0]}")
print(f"Negara terakhir: {daftar_negara[-1]}\n")

# Mengubah elemen
daftar_negara[1] = "Korea Selatan"
print(f"Setelah diubah: {daftar_negara}")

# append()
daftar_negara.append("Uni Emirat Arab")
print(f"Setelah append(): {daftar_negara}")

# insert()
daftar_negara.insert(0, "Jepang")
print(f"Setelah insert(): {daftar_negara}")

# del
del daftar_negara[1]
print(f"Setelah del: {daftar_negara}")

# pop()
negara_terakhir = daftar_negara.pop()
print(f"Setelah pop(): {daftar_negara} (yang di-pop: {negara_terakhir})")

# remove()
daftar_negara.remove("Singapura")
print(f"Setelah remove(): {daftar_negara}\n")

# sorted() (sementara)
print(f"Dengan sorted(): {sorted(daftar_negara)}")
print(f"Urutan asli tetap: {daftar_negara}\n")

# sort() (permanen)
daftar_negara.sort()
print(f"Setelah sort(): {daftar_negara}")

daftar_negara.sort(reverse=True)
print(f"Setelah sort(reverse=True): {daftar_negara}")

# reverse()
daftar_negara.reverse()
print(f"Setelah reverse(): {daftar_negara}\n")

# len()
print(f"Jumlah negara di daftar: {len(daftar_negara)}")