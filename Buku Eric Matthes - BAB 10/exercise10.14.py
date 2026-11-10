import json
from pathlib import Path

folder = Path(__file__).resolve().parent
filepath = folder / 'username.json'

def get_stored_username():
    """Mengambil nama pengguna yang tersimpan jika ada."""
    if filepath.exists():
        with open(filepath, 'r') as file:
            username = json.load(file)
        return username
    return None

def get_new_username():
    """Meminta nama pengguna baru dan menyimpannya."""
    username = input("Masukkan nama pengguna Anda: ")
    with open(filepath, 'w') as file:
        json.dump(username, file)
    return username

def greet_user():
    """Menyapa pengguna dan memverifikasi identitasnya."""
    username = get_stored_username()
    
    if username:
        # Menambahkan fitur verifikasi identitas pengguna
        correct_user = input(f"Apakah Anda adalah {username}? (y/n): ")
        if correct_user.lower() == 'y':
            print(f"Welcome back, {username}!")
            return
            
    # Jika user salah atau data kosong, daftarkan user baru
    print("\nSilakan daftarkan pengguna baru.")
    username = get_new_username()
    print(f"Kami akan mengingat Anda saat kembali nanti, {username}!")

# Menjalankan fungsi utama
greet_user()