from pathlib import Path
import json

path = Path(__file__).parent / "user_info.json"

if path.exists():
    user = json.loads(path.read_text())
    print("Ini yang saya ingat tentang kamu:")
else:
    user = {
        "name": input("Siapa namamu? "),
        "age": input("Berapa umurmu? "),
        "city": input("Kamu tinggal di kota mana? "),
    }
    path.write_text(json.dumps(user))
    print("\nData kamu sudah disimpan. Ini yang saya ingat:")

print(f"- Nama : {user['name']}")
print(f"- Umur : {user['age']}")
print(f"- Kota : {user['city']}")