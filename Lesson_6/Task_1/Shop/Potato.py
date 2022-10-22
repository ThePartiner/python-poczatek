class Potato():
    def __init__(self, species, size, unit_price, kilo):
        self.species = species
        self.size = size
        self.unit_price = unit_price
        self.kilo = kilo

    def coast_potato(self):
        coast = self.unit_price * self.kilo
        print(f"Cena jabłek wynosi: {coast}")

    def __repr__(self):
        return f"Potato species = '{self.species}', size = '{self.size}', unit_price = '{self.unit_price}', kilo = '{self.kilo}'"