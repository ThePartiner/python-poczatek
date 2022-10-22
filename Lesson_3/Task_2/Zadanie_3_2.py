class Product():
    def __init__(self, name, category, price):
        self.name = name
        self.category = category
        self.price = price


class Order():
    def __init__(self, first_name, last_name, products = None):
        self.first_name = first_name
        self.last_name = last_name
        if products == None:
            products = []
        self.products = products
        total_price = 0
        for single_product in products:
            total_price += single_product.price
        self.total_price = total_price

class Apple():
    def __init__(self, species, size, unit_price):
        self.species = species
        self.size = size
        self.unit_price = unit_price
class Potato():
    def __init__(self, species, size, unit_price):
        self.species = species
        self.size = size
        self.unit_price = unit_price

def print_product(product):
    print(f"Produkt: {product.name} | Kategoria: {product.category} | Cena: {product.price} PLN/szt")

def print_order(order):
    print(80 * "x")
    print(f"Użytkownik o imieniu {order.first_name} i nazwisku {order.last_name} złożył zamówienie: ")
    print()
    for single_product in order.products:
        Product.print_product(single_product)
    print()
    print(f"Całkowity koszt zamówienia wynosi {order.total_price}")
    print()
    print(80 * "x")

green_apple = Apple("Green", "XL", 2)
young_potato = Potato("Young", "S", 6)

pepsi = Product("Pepsi", "Drinks", 8 )
cookies = Product("Cookies", "Candys", 4)

order_julia =Order("Julia", "Slowikowska", products=[cookies, pepsi, cookies])
order_patryk = Order("Patryk", "Slowik")

print(pepsi)
print_product(pepsi)

print_order(order_julia)