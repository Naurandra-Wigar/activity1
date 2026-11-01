guests = ["tazkia", "sinta", "lala"]

print(f"Dear {guests[0]}, I would like to invite you to dinner.")
print(f"Dear {guests[1]}, I would like to invite you to dinner.")
print(f"Dear {guests[2]}, I would like to invite you to dinner.")

print(f"\n{guests[1]} can't make it to the dinner.")
guests[1] = "sunoo"

print(f"\nDear {guests[0]}, I would like to invite you to dinner.")
print(f"Dear {guests[1]}, I would like to invite you to dinner.")
print(f"Dear {guests[2]}, I would like to invite you to dinner.")

print("\nGood news! I found a bigger dinner table.")
guests.insert(0, "taya")   # awal
guests.insert(2, "fathma")   # tengah
guests.append("ais")      # akhir

print(f"\nDear {guests[0]}, I would like to invite you to dinner.")
print(f"Dear {guests[1]}, I would like to invite you to dinner.")
print(f"Dear {guests[2]}, I would like to invite you to dinner.")
print(f"Dear {guests[3]}, I would like to invite you to dinner.")
print(f"Dear {guests[4]}, I would like to invite you to dinner.")
print(f"Dear {guests[5]}, I would like to invite you to dinner.")