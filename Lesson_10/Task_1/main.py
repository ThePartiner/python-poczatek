from Shop.Order import Order

def get_order_price(order):
    return order.total_price

def run_homework():

    orders = []
    for _ in range(5):
        orders.append(Order.generate_order())

    orders.sort(key = lambda order: order._calculate_total_price())

    for element in orders:
        print(element)
if __name__ == "__main__":
    run_homework()