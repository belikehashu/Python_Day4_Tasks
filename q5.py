class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, name, price):
        self.items[name] = price

    def remove_item(self, name):
        if name in self.items:
            del self.items[name]

    def total_price(self):
        return sum(self.items.values())


cart = ShoppingCart()
cart.add_item("Book", 300)
cart.add_item("Pen", 20)
cart.remove_item("Pen")
print("Total Price:", cart.total_price())
