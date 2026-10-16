import math
def calculate_unit_price(diameter, price):
    radius = diameter / 2 / 100
    area = math.pi * radius ** 2
    unit_price = price / area
    return unit_price
diameter1 = float(input("Enter the diameter of the first pizza (cm): "))
price1 = float(input("Enter the price of the first pizza (€): "))
diameter2 = float(input("Enter the diameter of the second pizza (cm): "))
price2 = float(input("Enter the price of the second pizza (€): "))
unit_price1 = calculate_unit_price(diameter1, price1)
unit_price2 = calculate_unit_price(diameter2, price2)
print("First pizza unit price:", round(unit_price1, 2), "€/m²")