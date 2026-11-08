from pathlib import Path

name = input("Siapa namamu? ")

path = Path(__file__).parent / "guest.txt"
path.write_text(name)

print(f"Halo, {name}! Namamu sudah disimpan di guest.txt.")