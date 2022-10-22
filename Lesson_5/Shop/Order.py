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

    def __str__(self):
        one = 80 * "x"
        two = f"Użytkownik {self.first_name} {self.last_name} złożył/a zamówienie: \n"
        for single_product in self.products:
            two += f"\t{single_product}\n"
        four = f"Całkowity koszt zamówienia wynosi: {self.total_price} PLN"
        result = "\n".join([one,two, four, one])
        return result

    def __len__(self):
        return len(self.products)

    def __eq__(self, other):
        if self.__class__ != other.__class__:
            return NotImplemented
        if len(self.products) != len(other.products):
            return False
        if self.first_name != other.first_name or self.last_name != other.last_name:
            return False
        for element in self.products:
            if element not in other.products:
                return False
        return True

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
