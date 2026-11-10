print("--- Kalkulator Penjumlahan (Ketik 'q' untuk keluar) ---")

while True:
    num1 = input("\nMasukkan angka pertama: ")
    if num1.lower() == 'q':
        break
        
    num2 = input("Masukkan angka kedua: ")
    if num2.lower() == 'q':
        break
        
    try:
        total = int(num1) + int(num2)
    except ValueError:
        print("Error: Salah satu input bukan angka valid. Silakan coba lagi.")
    else:
        print(f"Hasilnya adalah: {total}")