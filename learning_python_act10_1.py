from pathlib import Path

path = Path(__file__).parent / "learning_python.txt"

# Cara 1: baca seluruh isi file sekaligus
contents = path.read_text()
print(contents)

print("-----")

# Cara 2: simpan baris-baris ke dalam list, lalu loop
lines = contents.splitlines()
for line in lines:
    print(line)