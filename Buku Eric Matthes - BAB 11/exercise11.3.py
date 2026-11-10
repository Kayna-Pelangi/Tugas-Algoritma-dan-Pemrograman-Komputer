import unittest

# ==========================================
# 1. KELAS YANG AKAN DIUJI (EMPLOYEE CLASS)
# ==========================================
class Employee:
    """Sebuah kelas untuk merepresentasikan seorang karyawan."""

    def __init__(self, first_name, last_name, salary):
        """Menyimpan nama depan, nama belakang, dan gaji tahunan."""
        self.first = first_name.title()
        self.last = last_name.title()
        self.salary = salary

    def give_raise(self, amount=5000):
        """Memberikan kenaikan gaji (default $5000)."""
        self.salary += amount


# ==========================================
# 2. PROSES PENGUJIAN KELAS (UNIT TEST)
# ==========================================
class TestEmployee(unittest.TestCase):

    def setUp(self):
        """Membuat satu objek Karyawan menggunakan fungsi bawaan setUp()."""
        # Objek ini akan otomatis dibuat ulang untuk setiap fungsi tes di bawah
        self.karyawan = Employee('budi', 'santoso', 60000)

    def test_give_default_raise(self):
        """Memastikan kenaikan gaji bawaan sebesar 5000 bekerja dengan benar."""
        self.karyawan.give_raise()
        self.assertEqual(self.karyawan.salary, 65000)

    def test_give_custom_raise(self):
        """Memastikan kenaikan gaji kustom (misal 10000) bekerja dengan benar."""
        self.karyawan.give_raise(10000)
        self.assertEqual(self.karyawan.salary, 70000)

# Menjalankan tes otomatis saat tombol Play ditekan
if __name__ == '__main__':
    unittest.main()