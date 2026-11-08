from random import randint


class Die:
    """Dadu dengan jumlah sisi tertentu."""

    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        print(randint(1, self.sides))


for sides in (6, 10, 20):
    die = Die(sides)
    print(f"\nMelempar dadu {sides} sisi sebanyak 10 kali:")
    for _ in range(10):
        die.roll_die()