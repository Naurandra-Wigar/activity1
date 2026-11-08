from pathlib import Path

filenames = ["alice.txt", "pride_and_prejudice.txt", "frankenstein.txt"]

for filename in filenames:
    path = Path(__file__).parent / filename
    try:
        contents = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        print(f"File {filename} tidak ditemukan.")
        continue

    lowered = contents.lower()
    count_the = lowered.count("the")
    count_the_space = lowered.count("the ")

    print(f"{filename}:")
    print(f"  'the'  muncul sekitar {count_the} kali")
    print(f"  'the ' muncul sekitar {count_the_space} kali")