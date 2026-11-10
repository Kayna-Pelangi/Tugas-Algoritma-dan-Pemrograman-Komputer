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


class Admin(User):
    """Model administrator, yaitu jenis khusus dari pengguna."""

    def __init__(self, nama_depan, nama_belakang, umur, kota):
        """Inisialisasi atribut induk, lalu atribut admin."""
        super().__init__(nama_depan, nama_belakang, umur, kota)
        self.hak_akses = [
            "bisa menambah postingan",
            "bisa menghapus postingan",
            "bisa memblokir pengguna",
        ]

    def show_privileges(self):
        """Tampilkan hak akses admin."""
        print("Hak akses admin:")
        for hak in self.hak_akses:
            print(f"- {hak}")


admin = Admin("Kayna Pelangi", "Maulana", 18, "Bekasi")
admin.describe_user()
admin.show_privileges()