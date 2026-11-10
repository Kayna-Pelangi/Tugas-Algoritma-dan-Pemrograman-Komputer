filename = 'guest_book.txt'

print("Ketik 'quit' jika Anda ingin selesai.")

while True:
    name = input("\nMasukkan nama Anda: ")
    
    # Memeriksa apakah pengguna ingin keluar dari program
    if name.lower() == 'quit':
        break
    else:
        # Membuka berkas dalam mode tambah ('a') agar data sebelumnya tidak terhapus
        with open(filename, 'a') as file_object:
            file_object.write(f"{name}\n")
            
        print(f"Halo {name}, nama Anda telah ditambahkan ke buku tamu.")