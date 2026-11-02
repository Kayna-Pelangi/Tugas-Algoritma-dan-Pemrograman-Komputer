# Tes kesamaan dan ketidaksamaan string
hewan = "kucing"
print("\nApakah hewan == 'kucing'? Prediksi saya True.")
print(hewan == "kucing")

print("\nApakah hewan != 'kucing'? Prediksi saya False.")
print(hewan != "kucing")

# Tes dengan lower()
nama = "Budi"
print("\nApakah nama.lower() == 'budi'? Prediksi saya True.")
print(nama.lower() == "budi")

print("\nApakah nama.lower() == 'Budi'? Prediksi saya False.")
print(nama.lower() == "Budi")

# Tes numerik: sama dengan dan tidak sama dengan
angka = 10
print("\nApakah angka == 10? Prediksi saya True.")
print(angka == 10)

print("\nApakah angka != 10? Prediksi saya False.")
print(angka != 10)

# Tes numerik: lebih besar dan lebih kecil
print("\nApakah angka > 5? Prediksi saya True.")
print(angka > 5)

print("\nApakah angka < 5? Prediksi saya False.")
print(angka < 5)

# Tes numerik: lebih besar sama dengan dan lebih kecil sama dengan
print("\nApakah angka >= 10? Prediksi saya True.")
print(angka >= 10)

print("\nApakah angka <= 9? Prediksi saya False.")
print(angka <= 9)

# Tes dengan and
umur_0 = 22
umur_1 = 18
print("\nApakah umur_0 >= 21 and umur_1 >= 18? Prediksi saya True.")
print(umur_0 >= 21 and umur_1 >= 18)

print("\nApakah umur_0 >= 21 and umur_1 >= 21? Prediksi saya False.")
print(umur_0 >= 21 and umur_1 >= 21)

# Tes dengan or
print("\nApakah umur_0 >= 21 or umur_1 >= 21? Prediksi saya True.")
print(umur_0 >= 21 or umur_1 >= 21)

print("\nApakah umur_0 >= 30 or umur_1 >= 30? Prediksi saya False.")
print(umur_0 >= 30 or umur_1 >= 30)

# Tes item ada di dalam list
topping = ["jamur", "bawang", "nanas"]
print("\nApakah 'jamur' in topping? Prediksi saya True.")
print("jamur" in topping)

print("\nApakah 'pepperoni' in topping? Prediksi saya False.")
print("pepperoni" in topping)

# Tes item tidak ada di dalam list
print("\nApakah 'pepperoni' not in topping? Prediksi saya True.")
print("pepperoni" not in topping)

print("\nApakah 'jamur' not in topping? Prediksi saya False.")
print("jamur" not in topping)