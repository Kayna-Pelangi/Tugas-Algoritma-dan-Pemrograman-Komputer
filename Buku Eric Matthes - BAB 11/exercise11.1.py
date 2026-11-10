import unittest

# ==========================================
# 1. FUNGSI YANG DIUJI (Latihan 11-1 & 11-2)
# ==========================================
def format_lokasi(kota, negara, populasi=None):
    """Mengembalikan string berformat 'Kota, Negara' atau dengan populasi."""
    if populasi:
        return f"{kota.title()}, {negara.title()} – population {populasi}"
    else:
        return f"{kota.title()}, {negara.title()}"


# ==========================================
# 2. PROSES PENGUJIAN (UNIT TEST)
# ==========================================
class TestKotaNegara(unittest.TestCase):
    
    def test_kota_negara(self):
        """Memastikan format kota dan negara standar berhasil (11-1)."""
        hasil = format_lokasi('santiago', 'chile')
        self.assertEqual(hasil, 'Santiago, Chile')

    def test_kota_negara_populasi(self):
        """Memastikan format dengan populasi juga berhasil (11-2)."""
        hasil = format_lokasi('santiago', 'chile', populasi=5000000)
        self.assertEqual(hasil, 'Santiago, Chile – population 5000000')

# Menjalankan pengujian otomatis saat tombol Play ditekan
if __name__ == '__main__':
    unittest.main()