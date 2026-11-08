from pathlib import Path
import json

path = Path(__file__).parent / "favorite_number.json"
number = json.loads(path.read_text())

print(f"Aku tahu angka favoritmu! Yaitu {number}.")