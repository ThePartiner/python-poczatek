

class Product():
    def __init__(self, name, category, price):
        self.name = name
        self.category = category
        self.price = price

def print_product(product):
    print(f"Produkt: {product.name} | Kategoria: {product.category} | Cena: {product.price} PLN/szt")
