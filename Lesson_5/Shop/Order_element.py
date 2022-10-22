from Shop.Product import Product

class OrderElement():
    def __init__(self, product, quanity):
        self.product = product
        self.quanity = quanity

    def calculate_price(self):
        return self.product.price * self.quanity

    def __str__(self):
        return f" {self.product} x {self.quanity}"

    def __eq__(self, other):
        if self.__class__ != other.__class__:
            return NotImplemented
        return self.quanity == other.quanity and self.product == other.product
