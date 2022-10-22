from Shop.Order import Order

def get_order_price(order):
    return order.total_price

def run_homework():

    orders = []
    for _ in range(5):
        orders.append(Order.generate_order())

    orders.sort(key=get_order_price)
    for order in orders:
        print(order)


if __name__ == "__main__":
    run_homework()