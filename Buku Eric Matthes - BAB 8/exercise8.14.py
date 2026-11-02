def make_car(pabrikan, model, **info_tambahan):
    """Simpan informasi mobil di dalam dictionary."""
    mobil = {"pabrikan": pabrikan, "model": model}
    for kunci, nilai in info_tambahan.items():
        mobil[kunci] = nilai
    return mobil


mobil = make_car("bmw", "x5", warna="hitam", sunroof=True)
print(mobil)