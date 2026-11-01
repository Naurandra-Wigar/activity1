favorite_places = {
    "fathma": ["Bali", "Yogyakarta"],             # ganti
    "arya": ["Bandung", "Lombok", "Malang"],      # ganti
    "sunoo": ["Raja Ampat"],                      # ganti
}

for name, places in favorite_places.items():
    print(f"{name.title()}'s favorite places are:")
    for place in places:
        print(f"- {place}")
    print()