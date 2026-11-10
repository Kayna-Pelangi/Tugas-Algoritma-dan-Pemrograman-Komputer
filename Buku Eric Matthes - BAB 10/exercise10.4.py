# Meminta pengguna untuk memasukkan nama mereka
name = input("Masukkan nama Anda: ")

filename = 'guest.txt'

# Membuka berkas dalam mode tulis ('w') dan menyimpan nama
with open(filename, 'w') as file_object:
    file_object.write(name)

print(f"Nama Anda telah dicatat di berkas {filename}.")