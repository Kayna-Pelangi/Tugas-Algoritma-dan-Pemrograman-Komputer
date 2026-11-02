daftar_pizza = ["pepperoni", "margherita", "bbq chicken", "four cheese"]

pizza_teman = daftar_pizza[:]

daftar_pizza.append("hawaiian")
pizza_teman.append("meat lovers")

print("Pizza favorit saya adalah:")
for pizza in daftar_pizza:
    print(pizza)

print("\nPizza favorit teman saya adalah:")
for pizza in pizza_teman:
    print(pizza)