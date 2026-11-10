from pathlib import Path

# Menggunakan jalur absolut komputer Anda
path = Path(r'C:\Users\ASUS\alpro\Buku Eric Matthes\learning_python.txt')
contents = path.read_text().rstrip()

print("--- Kode Ringkas Tanpa Variabel Sementara ---")
# Langsung melakukan perulangan pada hasil splitlines() tanpa membuat variabel baru
for line in contents.splitlines():
    print(line)