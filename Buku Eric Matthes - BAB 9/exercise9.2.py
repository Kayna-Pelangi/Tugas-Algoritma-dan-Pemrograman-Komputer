class Restaurant:
    """Model sederhana sebuah restoran."""

    def __init__(self, nama_restoran, jenis_masakan):
        """Inisialisasi atribut nama dan jenis masakan."""
        self.nama_restoran = nama_restoran
        self.jenis_masakan = jenis_masakan

    def describe_restaurant(self):
        """Tampilkan informasi tentang restoran."""
        print(f"Restoran {self.nama_restoran} menyajikan masakan "
              f"{self.jenis_masakan}.")

    def open_restaurant(self):
        """Tampilkan pesan bahwa restoran sedang buka."""
        print(f"Restoran {self.nama_restoran} sedang buka!")


restoran_1 = Restaurant("Warung Kayna", "Jawa")
restoran_2 = Restaurant("Sushi Tei", "Jepang")
restoran_3 = Restaurant("Pizza Hut", "Italia")

restoran_1.describe_restaurant()
restoran_2.describe_restaurant()
restoran_3.describe_restaurant()