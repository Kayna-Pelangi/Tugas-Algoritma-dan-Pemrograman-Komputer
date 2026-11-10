from random import choice

# Membuat daftar berisi 10 angka dan 5 huruf
lottery_pool = [1, 3, 5, 7, 9, 12, 15, 22, 33, 45, 'A', 'M', 'K', 'X', 'Z']

winning_ticket = []
print("Menarik nomor pemenang...")

# Memilih 4 item unik secara acak
while len(winning_ticket) < 4:
    pulled_item = choice(lottery_pool)
    if pulled_item not in winning_ticket:
        winning_ticket.append(pulled_item)

print(f"Tiket yang cocok dengan 4 angka/huruf ini memenangkan hadiah: {winning_ticket}")