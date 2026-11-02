daftar_negara = ["Monaco", "Jepang", "Singapura", "Arab Saudi", "Uni Emirat Arab"]

print("Urutan asli:")
print(daftar_negara)

print("\nDiurutkan A-Z dengan sorted():")
print(sorted(daftar_negara))

print("\nUrutan asli masih sama:")
print(daftar_negara)

print("\nDiurutkan Z-A dengan sorted():")
print(sorted(daftar_negara, reverse=True))

print("\nUrutan asli masih sama:")
print(daftar_negara)

daftar_negara.reverse()
print("\nSetelah reverse():")
print(daftar_negara)

daftar_negara.reverse()
print("\nSetelah reverse() lagi (kembali ke urutan asli):")
print(daftar_negara)

daftar_negara.sort()
print("\nSetelah sort() (A-Z permanen):")
print(daftar_negara)

daftar_negara.sort(reverse=True)
print("\nSetelah sort(reverse=True) (Z-A permanen):")
print(daftar_negara)