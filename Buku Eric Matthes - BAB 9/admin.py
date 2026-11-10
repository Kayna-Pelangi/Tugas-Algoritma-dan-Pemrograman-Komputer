"""Modul berisi class Privileges dan Admin."""

from user import User


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
