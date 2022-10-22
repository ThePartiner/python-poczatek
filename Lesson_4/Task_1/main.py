from Shop.Apple import Apple
from Shop.Potato import Potato
from Shop.Order import Order, generate_order
from Shop.Product import Product

def run_homework():
    green_apple = Apple("Green", "XL", 2)
    young_potato = Potato("Young", "S", 6)

    pepsi = Product("Pepsi", "Drinks", 8 )
    cookies = Product("Cookies", "Candys", 4)

    order_julia =Order("Julia", "Slowikowska", products=[cookies, pepsi, cookies])
    order_patryk =Order("Patryk", "Slowik")

    first_order= generate_order()
    print(first_order)
    Order.print_order(first_order)

if __name__ == "__main__":
    run_homework()