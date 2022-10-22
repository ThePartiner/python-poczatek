from Shop.Order import Order
from Shop.Apple import Apple
from Shop.Product import Product
from Shop.Order_element import OrderElement
from Shop.Tax import TaxCalculator

def run_homework():

    first_order = Order.generate_order()

    print(first_order)

    japko = Apple("zielone", "male", 5, 5)

    repr(japko)
    print(japko)

    print(len(first_order))

    cookies = Product("ciacho", "jedzenie", 4)

    first_order.add_product(cookies, 6)

    print(first_order)


    cookie = Product ("Ciastko", "Owoce", 5)

    ten_cookies = OrderElement (cookie, 10)

    cookies_tax = TaxCalculator.tax_for_order_element(ten_cookies)

    print(f"Cena ciastek: {ten_cookies.calculate_price()} + {cookies_tax:.2f}")


if __name__ == "__main__":
    run_homework()