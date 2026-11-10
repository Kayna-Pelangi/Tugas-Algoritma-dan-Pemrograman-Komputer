"""Modul berisi class Restaurant."""


class Restaurant:
    """Model sederhana sebuah restoran."""

    def __init__(self, nama_restoran, jenis_masakan):
        """Inisialisasi atribut restoran."""
        self.nama_restoran = nama_restoran
        self.jenis_masakan = jenis_masakan
        self.jumlah_dilayani = 0

    def describe_restaurant(self):
        """Tampilkan informasi tentang restoran."""
        print(f"Restoran {self.nama_restoran} menyajikan masakan "
              f"{self.jenis_masakan}.")

    def open_restaurant(self):
        """Tampilkan pesan bahwa restoran sedang buka."""
        print(f"Restoran {self.nama_restoran} sedang buka!")

    def set_number_served(self, jumlah):
        """Atur jumlah pelanggan yang sudah dilayani."""
        self.jumlah_dilayani = jumlah

    def increment_number_served(self, tambahan):
        """Tambahkan jumlah pelanggan yang sudah dilayani."""
        self.jumlah_dilayani += tambahan