from random import randint

class Die:
    """Representasi dari sebuah dadu."""
    
    def __init__(self, sides=6):
        """Secara default dadu memiliki 6 sisi."""
        self.sides = sides

    def roll_die(self):
        """Mencetak angka acak antara 1 dan jumlah sisi dadu."""
        print(randint(1, self.sides), end=" ")

# 1. Membuat dadu 6 sisi dan mengocoknya 10 kali
print("Kocokan dadu 6 sisi (10x):")
die_6 = Die()
for _ in range(10):
    die_6.roll_die()
print("\n")

# 2. Membuat dadu 10 sisi dan mengocoknya 10 kali
print("Kocokan dadu 10 sisi (10x):")
die_10 = Die(sides=10)
for _ in range(10):
    die_10.roll_die()
print("\n")

# 3. Membuat dadu 20 sisi dan mengocoknya 10 kali
print("Kocokan dadu 20 sisi (10x):")
die_20 = Die(sides=20)
for _ in range(10):
    die_20.roll_die()
print()