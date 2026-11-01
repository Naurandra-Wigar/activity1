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

print("\nSorry, the new table won't arrive in time. I can invite only two people for dinner.")

removed = guests.pop()
print(f"Sorry {removed}, I can't invite you to dinner.")
removed = guests.pop()
print(f"Sorry {removed}, I can't invite you to dinner.")
removed = guests.pop()
print(f"Sorry {removed}, I can't invite you to dinner.")
removed = guests.pop()
print(f"Sorry {removed}, I can't invite you to dinner.")

print(f"\nDear {guests[0]}, you are still invited to dinner.")
print(f"Dear {guests[1]}, you are still invited to dinner.")

del guests[1]
del guests[0]
print(guests)   # hasilnya: []