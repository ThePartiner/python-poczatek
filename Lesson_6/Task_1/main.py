from Shop.Order import Order, generate_order
from Shop.Apple import Apple
from Shop.Product import Product

def run_homework():

    first_order = generate_order()

    print(first_order)

    japko = Apple("zielone", "male", 5, 5)

    repr(japko)
    print(japko)

    print(len(first_order))

    cookies = Product("ciacho", "jedzenie", 4)

    first_order.add_product(cookies, 6)

    print(first_order)


if __name__ == "__main__":
    run_homework()