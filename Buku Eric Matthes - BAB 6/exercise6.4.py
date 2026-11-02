glosarium = {
    "list": "Kumpulan item berurutan, ditulis dengan kurung siku.",
    "tuple": "List yang isinya tidak bisa diubah.",
    "loop": "Perulangan untuk menjalankan kode yang sama pada tiap item.",
    "if": "Pernyataan yang jalan hanya jika kondisinya True.",
    "dictionary": "Pasangan key dan value, ditulis dengan kurung kurawal.",
    "string": "Rangkaian karakter, ditulis dengan tanda kutip.",
    "variabel": "Nama yang dipakai untuk menyimpan sebuah nilai.",
    "append()": "Method untuk menambah item ke akhir list.",
    "range()": "Fungsi untuk membuat deretan angka.",
    "slice": "Bagian tertentu dari sebuah list.",
}

for kata, arti in glosarium.items():
    print(f"{kata}:")
    print(f"    {arti}\n")