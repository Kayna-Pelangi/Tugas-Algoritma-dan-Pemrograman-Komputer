class User:
    """Model sederhana profil pengguna."""

    def __init__(self, nama_depan, nama_belakang, umur, kota):
        """Inisialisasi atribut pengguna."""
        self.nama_depan = nama_depan
        self.nama_belakang = nama_belakang
        self.umur = umur
        self.kota = kota

    def describe_user(self):
        """Tampilkan ringkasan informasi pengguna."""
        print(f"Nama: {self.nama_depan} {self.nama_belakang}")
        print(f"Umur: {self.umur}")
        print(f"Kota: {self.kota}")

    def greet_user(self):
        """Tampilkan sapaan personal untuk pengguna."""
        print(f"Halo, {self.nama_depan}! Selamat datang kembali.\n")


pengguna_1 = User("Kayna Pelangi", "Maulana", 18, "Bekasi")
pengguna_2 = User("Vania", "Ramadhani", 19, "Jakarta")
pengguna_3 = User("Nayla", "Saputri", 19, "Solo")

pengguna_1.describe_user()
pengguna_1.greet_user()

pengguna_2.describe_user()
pengguna_2.greet_user()

pengguna_3.describe_user()
pengguna_3.greet_user()