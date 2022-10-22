class Product():
    pass

class Order():
    pass

class Apple():
    pass
class Potato():
    pass

green_apple = Apple()
young_potato = Potato()

print(f'green_apple to {type(green_apple)}')
print(f"young_potato to {type(young_potato)}")

Orders = [Order(), Order(), Order(), Order(), Order()]

dictionery = {
    "pepsi": Product(),
    "yougurt": Product(),
}