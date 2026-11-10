from datetime import datetime

# Mengambil waktu saat ini
hari_ini = datetime.now()

# Menentukan tanggal target (misal: Tahun Baru 2027)
tahun_baru = datetime(2027, 1, 1)

# Menghitung selisih waktu
selisih = tahun_baru - hari_ini

print(f"Saat ini: {hari_ini.strftime('%d-%m-%Y %H:%M')}")
print(f"Tersisa {selisih.days} hari lagi menuju tahun baru 2027!")