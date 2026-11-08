from random import choice

# 10 angka dan 5 huruf
lottery_items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "A", "B", "C", "D", "E"]

winning_ticket = []
while len(winning_ticket) < 4:
    pick = choice(lottery_items)
    if pick not in winning_ticket:
        winning_ticket.append(pick)

print(f"Tiket dengan 4 angka/huruf berikut menang hadiah: {winning_ticket}")