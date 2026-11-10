"""Modul berisi class User."""


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