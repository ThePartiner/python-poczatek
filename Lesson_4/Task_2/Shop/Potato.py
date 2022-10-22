class Potato():
    def __init__(self, species, size, unit_price, kilo):
        self.species = species
        self.size = size
        self.unit_price = unit_price
        self.kilo = kilo

    def coast_potato(self):
        coast = self.unit_price * self.kilo
        print(f"Cena jabłek wynosi: {coast}")