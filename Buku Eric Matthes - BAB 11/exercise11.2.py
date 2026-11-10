import unittest

# ==========================================
# 1. FUNGSI YANG DIUJI (Latihan 11-2)
# ==========================================
def format_lokasi(kota, negara, populasi=None):
    """Mengembalikan string berformat 'Kota, Negara – population XXX' jika ada populasi."""
    if populasi:
        return f"{kota.title()}, {negara.title()} – population {populasi}"
    else:
        return f"{kota.title()}, {negara.title()}"


# ==========================================
# 2. PROSES PENGUJIAN (UNIT TEST)
# ==========================================
class TestCityCountryPopulation(unittest.TestCase):
    
    def test_city_country(self):
        """Memastikan format tanpa populasi tetap bekerja dengan benar."""
        hasil = format_lokasi('santiago', 'chile')
        self.assertEqual(hasil, 'Santiago, Chile')

    def test_city_country_population(self):
        """Memastikan format dengan nilai populasi kustom berhasil lolos uji."""
        hasil = format_lokasi('santiago', 'chile', populasi=5000000)
        self.assertEqual(hasil, 'Santiago, Chile – population 5000000')

# Menjalankan pengujian otomatis saat tombol Play ditekan
if __name__ == '__main__':
    unittest.main()