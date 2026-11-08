from pathlib import Path
import json

path = Path(__file__).parent / "favorite_number.json"

if path.exists():
    number = json.loads(path.read_text())
    print(f"Aku tahu angka favoritmu! Yaitu {number}.")
else:
    number = input("Apa angka favoritmu? ")
    path.write_text(json.dumps(number))
    print("Oke, angka favoritmu sudah disimpan. Jalankan lagi ya!")