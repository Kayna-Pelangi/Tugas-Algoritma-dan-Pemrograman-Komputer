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


class IceCreamStand(Restaurant):
    """Model kios es krim, yaitu jenis khusus dari restoran."""

    def __init__(self, nama_restoran, jenis_masakan):
        """Inisialisasi atribut induk, lalu atribut kios es krim."""
        super().__init__(nama_restoran, jenis_masakan)
        self.rasa = ["vanila", "cokelat", "stroberi", "matcha"]

    def show_flavors(self):
        """Tampilkan daftar rasa es krim."""
        print("Rasa es krim yang tersedia:")
        for rasa in self.rasa:
            print(f"- {rasa}")


kios = IceCreamStand("Es Krim Ceria", "es krim")
kios.describe_restaurant()
kios.show_flavors()