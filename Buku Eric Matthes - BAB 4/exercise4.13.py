menu_buffet = ("nasi goreng", "ayam bakar", "soto", "gado-gado", "sate")

print("Menu buffet:")
for makanan in menu_buffet:
    print(makanan)

try:
    menu_buffet[0] = "mie goreng"
except TypeError:
    print("\nError: isi tuple tidak bisa diubah!")

menu_buffet = ("nasi goreng", "mie goreng", "soto", "rendang", "sate")

print("\nMenu buffet yang baru:")
for makanan in menu_buffet:
    print(makanan)