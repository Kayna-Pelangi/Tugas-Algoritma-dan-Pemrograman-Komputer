from pathlib import Path

# Menggunakan jalur absolut sesuai lokasi file di komputer Anda
path = Path(r'C:\Users\ASUS\alpro\Buku Eric Matthes\learning_python.txt')

# Membaca isi file berkas teks
contents = path.read_text().rstrip()

# --- CARA 1: Membaca dan mencetak seluruh isi file sekaligus ---
print("--- Cara 1: Membaca Seluruh File ---")
print(contents)
print("\n")

# --- CARA 2: Menyimpan baris ke dalam list lalu melakukan looping ---
print("--- Cara 2: Menyimpan dalam List dan Di-loop ---")
lines = contents.splitlines() 

for line in lines:
    print(line)