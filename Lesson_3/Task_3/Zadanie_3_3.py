import random

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

def print_order(order):


    print(80 * "x")
    print(f"Użytkownik {order.first_name} {order.last_name} złożył/a zamówienie: ")
    print()
    for single_product in order.products:
        print_product(single_product)
    print()
    print(f"Całkowity koszt zamówienia wynosi: {order.total_price} PLN")
    if order.total_price > 1000:
        print("Za dużo wydajesz GAMONIU!")
    print()
    print(80 * "x")


def print_product(product):
    print(f"Produkt: {product.name} | Kategoria: {product.category} | Cena: {product.price} PLN/szt")

def generate_order():
    numbers = random.randint(1, 20)
    product_list = []
    for single_product in range(numbers):
        one_product = random.randint(0,5)
        shop_list = ["shelti", "kosmetyki", "ciastka", "chipsy", "sushi", "marian"]
        name = (f"{shop_list[one_product]}")
        category = "Inna"
        random_price = random.randint(25, 800)
        single_product = Product(name, category, random_price)
        product_list.append(single_product)
    order = Order("Kinga", "Elert", product_list)
    return order


green_apple = Apple("Green", "XL", 2)
young_potato = Potato("Young", "S", 6)

pepsi = Product("Pepsi", "Drinks", 8 )
cookies = Product("Cookies", "Candys", 4)

order_julia =Order("Julia", "Slowikowska", products=[cookies, pepsi, cookies])
order_patryk =Order("Patryk", "Slowik")

first_order= generate_order()
print(first_order)
print_order(first_order)