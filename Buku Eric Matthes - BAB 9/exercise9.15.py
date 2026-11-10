from random import choice

def generate_ticket(pool):
    """Fungsi untuk membuat kombinasi 4 pilihan acak dari pool."""
    ticket = []
    while len(ticket) < 4:
        pulled_item = choice(pool)
        if pulled_item not in ticket:
            ticket.append(pulled_item)
    return ticket

# Kumpulan nomor lotre dan tiket kita
lottery_pool = [1, 3, 5, 7, 9, 12, 15, 22, 33, 45, 'A', 'M', 'K', 'X', 'Z']
my_ticket = [7, 22, 'M', 'Z']

# Loop simulasi pencarian sampai menang
attempts = 0
while True:
    winning_ticket = generate_ticket(lottery_pool)
    attempts += 1
    
    # Cek apakah semua elemen di tiket kita ada di tiket pemenang
    # (Menggunakan set agar urutan tidak memengaruhi hasil)
    if set(my_ticket) == set(winning_ticket):
        break

print(f"Tiket Anda: {my_ticket}")
print(f"Lotre dimenangkan setelah perulangan ke-{attempts}!")