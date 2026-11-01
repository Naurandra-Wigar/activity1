sandwich_orders = [
    "pastrami", "tuna", "pastrami", "turkey", "veggie", "pastrami"
]
finished_sandwiches = []

print("The deli has run out of pastrami.")
while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I made your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\nAll the sandwiches that were made:")
for sandwich in finished_sandwiches:
    print(f"- {sandwich} sandwich")