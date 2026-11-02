pesan = "\nBerapa umur Anda?"
pesan += "\n(Ketik 'quit' kalau sudah selesai.) "

while True:
    umur = input(pesan)

    if umur == "quit":
        break

    umur = int(umur)

    if umur < 3:
        print("Tiket Anda gratis.")
    elif umur <= 12:
        print("Harga tiket Anda $10.")
    else:
        print("Harga tiket Anda $15.")