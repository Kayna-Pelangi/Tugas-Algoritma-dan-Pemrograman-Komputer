hasil_polling = {}

polling_aktif = True

while polling_aktif:
    nama = input("\nSiapa nama Anda? ")
    tempat = input("Kalau bisa mengunjungi satu tempat di dunia, "
                   "ke mana Anda akan pergi? ")

    hasil_polling[nama] = tempat

    ulang = input("Apakah ada orang lain yang mau menjawab? (ya/tidak) ")
    if ulang == "tidak":
        polling_aktif = False

print("\n--- Hasil Polling ---")
for nama, tempat in hasil_polling.items():
    print(f"{nama} ingin berlibur ke {tempat}.")