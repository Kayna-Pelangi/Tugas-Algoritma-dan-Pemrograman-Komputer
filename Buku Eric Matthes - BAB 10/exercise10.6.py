print("--- Program Penjumlahan Sederhana ---")

try:
    num1 = input("Masukkan angka pertama: ")
    num1 = int(num1)
    
    num2 = input("Masukkan angka kedua: ")
    num2 = int(num2)
    
except ValueError:
    # Ditampilkan jika input tidak bisa diubah menjadi integer
    print("Maaf, input yang Anda masukkan harus berupa angka!")
else:
    result = num1 + num2
    print(f"Hasil penjumlahan: {num1} + {num2} = {result}")