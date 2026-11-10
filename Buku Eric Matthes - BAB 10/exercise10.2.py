from pathlib import Path

# Menggunakan jalur absolut komputer Anda
path = Path(r'C:\Users\ASUS\alpro\Buku Eric Matthes\learning_python.txt')
contents = path.read_text().rstrip()

print("--- Hasil Modifikasi Bahasa (Python -> C) ---")
# Melakukan perulangan untuk setiap baris teks
for line in contents.splitlines():
    # Mengganti kata 'Python' menjadi 'C'
    modified_line = line.replace('Python', 'C')
    print(modified_line)