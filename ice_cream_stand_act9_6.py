from restaurant import Restaurant


class IceCreamStand(Restaurant):
    """Kios es krim, jenis khusus dari restoran."""

    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def display_flavors(self):
        print(f"Rasa es krim di {self.restaurant_name}:")
        for flavor in self.flavors:
            print(f"- {flavor}")


stand = IceCreamStand("Es Krim Ceria", "es krim", ["vanila", "coklat", "stroberi", "matcha"])
stand.describe_restaurant()
stand.display_flavors()