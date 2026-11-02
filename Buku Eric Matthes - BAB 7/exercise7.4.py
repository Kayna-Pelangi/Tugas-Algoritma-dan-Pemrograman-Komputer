pesan = "\nMasukkan topping pizza yang Anda inginkan:"
pesan += "\n(Ketik 'quit' kalau sudah selesai.) "

while True:
    topping = input(pesan)

    if topping == "quit":
        break
    else:
        print(f"Saya akan menambahkan {topping} ke pizza Anda.")