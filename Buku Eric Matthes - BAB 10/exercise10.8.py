filenames = ['cats.txt', 'dogs.txt']

for filename in filenames:
    print(f"\nMembaca berkas: {filename}")
    try:
        with open(filename, 'r') as file:
            contents = file.read()
            print(contents.strip())
    except FileNotFoundError:
        # Menampilkan pesan ramah jika berkas hilang
        print(f"Maaf, berkas '{filename}' tidak dapat ditemukan di direktori ini.")