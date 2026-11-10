"""Modul berisi class User, Privileges, dan Admin."""


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


class Privileges:
    """Model hak akses untuk seorang admin."""

    def __init__(self):
        """Inisialisasi daftar hak akses."""
        self.hak_akses = [
            "bisa menambah postingan",
            "bisa menghapus postingan",
            "bisa memblokir pengguna",
        ]

    def show_privileges(self):
        """Tampilkan hak akses."""
        print("Hak akses admin:")
        for hak in self.hak_akses:
            print(f"- {hak}")


class Admin(User):
    """Model administrator, yaitu jenis khusus dari pengguna."""

    def __init__(self, nama_depan, nama_belakang, umur, kota):
        """Inisialisasi atribut induk, lalu buat objek Privileges."""
        super().__init__(nama_depan, nama_belakang, umur, kota)
        self.privileges = Privileges()