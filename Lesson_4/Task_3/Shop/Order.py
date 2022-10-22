import random
from Shop.Product import Product
from Shop.Order_element import OrderElement

class Order():
    def __init__(self, first_name, last_name, products = None):
        self.first_name = first_name
        self.last_name = last_name
        if products == None:
            products = []
        self.products = products
        self.total_price = self.calculate_total_price()

    def calculate_total_price(self):
        total_price = 0
        for single_product in self.products:
            total_price += single_product.calculate_price()
        return total_price

    def print_order(self):
        print(80 * "x")
        print(f"Użytkownik {self.first_name} {self.last_name} złożył/a zamówienie: ")
        for single_product in self.products:
            single_product.print_element()
        print(f"Całkowity koszt zamówienia wynosi: {self.total_price} PLN")
        print(80 * "x")

def generate_order():
    numbers = random.randint(1, 20)
    product_list = []
    for single_product in range(numbers):
        one_product = random.randint(0,5)
        name = (f"Produkt-{single_product}")
        category = "Inna"
        random_price = random.randint(25, 800)
        single_product = Product(name, category, random_price)
        quanity = random.randint(1, 10)
        product_list.append(OrderElement(single_product, quanity))
    order = Order("Kinga", "Elert", product_list)
    return order
