from Shop.Order import Order, generate_order


def run_homework():

    first_order = generate_order()

    first_order.print_order()

if __name__ == "__main__":
    run_homework()