# Reviewed for PEP 8
def make_shirt(size="large", text="I love Python"):
    """Print the size and message of a shirt."""
    print(f"The shirt is size {size} and says '{text}'.")


make_shirt()                          # large, pesan default
make_shirt("medium")                  # medium, pesan default
make_shirt("small", "Hello World")    # ukuran lain, pesan lain