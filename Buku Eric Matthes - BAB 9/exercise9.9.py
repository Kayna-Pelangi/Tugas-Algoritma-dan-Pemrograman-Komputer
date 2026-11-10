class Car:
    """Model sederhana sebuah mobil."""

    def __init__(self, make, model, year):
        """Inisialisasi atribut mobil."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Kembalikan nama deskriptif yang rapi."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Tampilkan jarak tempuh mobil."""
        print(f"Mobil ini sudah menempuh {self.odometer_reading} mil.")


class Battery:
    """Model baterai untuk mobil listrik."""

    def __init__(self, battery_size=40):
        """Inisialisasi atribut baterai."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Tampilkan kapasitas baterai."""
        print(f"Mobil ini punya baterai {self.battery_size}-kWh.")

    def get_range(self):
        """Tampilkan jarak tempuh berdasarkan kapasitas baterai."""
        if self.battery_size == 40:
            jarak = 150
        elif self.battery_size == 65:
            jarak = 225
        print(f"Mobil ini bisa menempuh sekitar {jarak} mil "
              f"dengan baterai penuh.")

    def upgrade_battery(self):
        """Naikkan kapasitas baterai ke 65 kalau belum."""
        if self.battery_size != 65:
            self.battery_size = 65


class ElectricCar(Car):
    """Model mobil listrik."""

    def __init__(self, make, model, year):
        """Inisialisasi atribut induk, lalu buat objek Battery."""
        super().__init__(make, model, year)
        self.battery = Battery()


my_leaf = ElectricCar("nissan", "leaf", 2024)
print(my_leaf.get_descriptive_name())

my_leaf.battery.get_range()

my_leaf.battery.upgrade_battery()
my_leaf.battery.get_range()