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


restaurant = Restaurant("Warung Kayna", "Jawa")

print(f"Nama restoran: {restaurant.nama_restoran}")
print(f"Jenis masakan: {restaurant.jenis_masakan}")

restaurant.describe_restaurant()
restaurant.open_restaurant()