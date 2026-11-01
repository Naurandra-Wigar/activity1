favorite_numbers = {
    "tazkia": [7, 21],
    "thaya": [3, 9, 15],
    "ais": [12],
    "fathma": [8, 4],
    "arya": [21, 1],
}

for name, numbers in favorite_numbers.items():
    print(f"{name.title()}'s favorite numbers are:")
    for number in numbers:
        print(number)
    print()