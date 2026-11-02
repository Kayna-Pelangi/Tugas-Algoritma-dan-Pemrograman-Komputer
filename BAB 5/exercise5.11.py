angka = list(range(1, 10))

for nomor in angka:
    if nomor == 1:
        print(f"{nomor}st")
    elif nomor == 2:
        print(f"{nomor}nd")
    elif nomor == 3:
        print(f"{nomor}rd")
    else:
        print(f"{nomor}th")