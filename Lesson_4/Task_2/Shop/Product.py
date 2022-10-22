

class Product():
    def __init__(self, name, category, price):
        self.name = name
        self.category = category
        self.price = price

    def print_product(self):
        print(f"Produkt: {self.name} | Kategoria: {self.category} | Cena: {self.price} PLN/szt")
