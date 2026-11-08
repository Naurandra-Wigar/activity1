from random import choice

lottery_items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "A", "B", "C", "D", "E"]


def draw_ticket():
    """Mengundi 4 item berbeda."""
    ticket = []
    while len(ticket) < 4:
        pick = choice(lottery_items)
        if pick not in ticket:
            ticket.append(pick)
    return ticket


my_ticket = [3, 7, "A", "D"]
print(f"Tiket saya: {my_ticket}")

attempts = 0
while True:
    attempts += 1
    winning_ticket = draw_ticket()
    # Urutan tidak penting, jadi bandingkan sebagai himpunan
    if set(winning_ticket) == set(my_ticket):
        break

print(f"Tiket yang menang: {winning_ticket}")
print(f"Dibutuhkan {attempts} kali undian sampai tiket saya menang.")