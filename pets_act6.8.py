pets = [
    {"kind": "cat", "owner": "Arya"},      # ganti jenis hewannya
    {"kind": "dog", "owner": "Sunoo"},     # ganti
    {"kind": "rabbit", "owner": "Kama"},   # ganti
]

for pet in pets:
    print(f"Kind of animal: {pet['kind']}")
    print(f"Owner: {pet['owner']}\n")