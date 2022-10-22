from Shop.Product import Product

class OrderElement():
    def __init__(self, product, quanity):
        self.product = product
        self.quanity = quanity

    def calculate_price(self):
        return self.product.price * self.quanity

    def print_element(self):
        self.product.print_product()
        print(f"x {self.quanity}")