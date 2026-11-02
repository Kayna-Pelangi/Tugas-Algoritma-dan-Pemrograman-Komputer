pesanan_sandwich = [
    "tuna", "sosis", "ayam", "sosis", "telur", "sosis", "keju",
]
sandwich_selesai = []

print("Maaf, sosis sudah habis.")

while "sosis" in pesanan_sandwich:
    pesanan_sandwich.remove("sosis")

while pesanan_sandwich:
    sandwich_saat_ini = pesanan_sandwich.pop()
    print(f"Saya sudah membuat sandwich {sandwich_saat_ini} Anda.")
    sandwich_selesai.append(sandwich_saat_ini)

print("\nSandwich yang sudah selesai dibuat:")
for sandwich in sandwich_selesai:
    print(sandwich)