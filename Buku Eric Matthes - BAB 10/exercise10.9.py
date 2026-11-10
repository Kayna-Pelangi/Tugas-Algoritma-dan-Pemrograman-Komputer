filenames = ['Buku Eric Matthes/cats.txt', 'Buku Eric Matthes/dogs.txt']

for filename in filenames:
    try:
        with open(filename, 'r') as file:
            contents = file.read()
            print(f"\nIsi dari {filename}:")
            print(contents.strip())
    except FileNotFoundError:
        # Gagal secara diam-diam tanpa memunculkan pesan error
        pass