from restaurant import restaurant

restaurant = restaurant("Warung Sedap", "Jawa")

print(f"Pelanggan yang sudah dilayani: {restaurant.number_served}")

# Ubah nilai secara langsung
restaurant.number_served = 25
print(f"Pelanggan yang sudah dilayani: {restaurant.number_served}")

# Pakai method set_number_served()
restaurant.set_number_served(40)
print(f"Pelanggan yang sudah dilayani: {restaurant.number_served}")

# Pakai method increment_number_served()
restaurant.increment_number_served(60)
print(f"Setelah sehari berjualan: {restaurant.number_served}")