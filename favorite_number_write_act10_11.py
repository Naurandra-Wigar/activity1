from pathlib import Path
import json

number = input("Apa angka favoritmu? ")

path = Path(__file__).parent / "favorite_number.json"
path.write_text(json.dumps(number))

print("Angka favoritmu sudah disimpan.")