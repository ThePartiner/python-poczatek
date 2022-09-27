import calculations.calc

capital = int(input("Podaj kapitał: "))
percentage = int(input("Podaj procenty: "))
years = int(input("Podaj lata: "))

lokata =  calculations.calc.calculation_locat(capital, percentage, years)
print(f"Lokat a po {years} bedzie warta: {lokata}")