import random
from Shop.Product import Product, print_product

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
