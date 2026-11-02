def build_profile(depan, belakang, **info_pengguna):
    """Bangun dictionary berisi semua informasi tentang pengguna."""
    info_pengguna["nama_depan"] = depan
    info_pengguna["nama_belakang"] = belakang
    return info_pengguna


profil_saya = build_profile(
    "Kayna",
    "Maulana",
    kota="Solo",
    kampus="UNS",
    jurusan="Teknik Industri",
)

print(profil_saya)