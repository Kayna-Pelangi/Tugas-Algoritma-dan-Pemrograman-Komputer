sungai = {
    "nil": "Mesir",
    "amazon": "Brasil",
    "mekong": "Vietnam",
}

for nama, negara in sungai.items():
    print(f"Sungai {nama.title()} mengalir melalui {negara}.")

print("\nNama sungai di dalam dictionary:")
for nama in sungai.keys():
    print(nama.title())

print("\nNama negara di dalam dictionary:")
for negara in sungai.values():
    print(negara)