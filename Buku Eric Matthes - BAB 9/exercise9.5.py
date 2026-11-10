class User:
    """Model sederhana profil pengguna."""

    def __init__(self, nama_depan, nama_belakang, umur, kota):
        """Inisialisasi atribut pengguna."""
        self.nama_depan = nama_depan
        self.nama_belakang = nama_belakang
        self.umur = umur
        self.kota = kota
        self.percobaan_login = 0

    def describe_user(self):
        """Tampilkan ringkasan informasi pengguna."""
        print(f"Nama: {self.nama_depan} {self.nama_belakang}")
        print(f"Umur: {self.umur}")
        print(f"Kota: {self.kota}")

    def greet_user(self):
        """Tampilkan sapaan personal untuk pengguna."""
        print(f"Halo, {self.nama_depan}! Selamat datang kembali.\n")

    def increment_login_attempts(self):
        """Tambah percobaan login sebanyak 1."""
        self.percobaan_login += 1

    def reset_login_attempts(self):
        """Reset percobaan login menjadi 0."""
        self.percobaan_login = 0


pengguna = User("Kayna", "Santoso", 20, "Bekasi")

pengguna.increment_login_attempts()
pengguna.increment_login_attempts()
pengguna.increment_login_attempts()
print(f"Percobaan login: {pengguna.percobaan_login}")

pengguna.reset_login_attempts()
print(f"Percobaan login: {pengguna.percobaan_login}")