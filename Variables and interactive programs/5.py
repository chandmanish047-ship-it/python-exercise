GRAMS_PER_LOT = 13.3
LOTS_PER_POUND = 32
POUNDS_PER_TALENT = 20
GRAMS_PER_POUND = LOTS_PER_POUND * GRAMS_PER_LOT
GRAMS_PER_TALENT = POUNDS_PER_TALENT * GRAMS_PER_POUND
talents = float(input("Enter talents (leiviskä): "))
pounds = float(input("Enter pounds (naula): "))
lots = float(input("Enter lots (luoti): "))
total_grams = (talents * GRAMS_PER_TALENT) + (pounds * GRAMS_PER_POUND) + (lots * GRAMS_PER_LOT)
kilograms = int(total_grams // 1000)
remaining_grams = total_grams % 1000
print(f"The mass is {kilograms} kg and {remaining_grams:.2f} g.")