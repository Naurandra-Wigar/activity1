# Reviewed for PEP 8
def make_sandwich(*items):
    """Print a summary of the items in a sandwich order."""
    print("\nMaking a sandwich with:")
    for item in items:
        print(f"- {item}")


make_sandwich("ham", "cheese")
make_sandwich("tuna", "lettuce", "tomato")
make_sandwich("egg", "mayo", "cucumber", "onion")