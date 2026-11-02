pesanan_sandwich = ["tuna", "ayam", "telur", "keju"]
sandwich_selesai = []

while pesanan_sandwich:
    sandwich_saat_ini = pesanan_sandwich.pop()
    print(f"Saya sudah membuat sandwich {sandwich_saat_ini} Anda.")
    sandwich_selesai.append(sandwich_saat_ini)

print("\nSandwich yang sudah selesai dibuat:")
for sandwich in sandwich_selesai:
    print(sandwich)