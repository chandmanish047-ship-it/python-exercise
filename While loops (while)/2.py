INCH_TO_CM = 2.54
while True:
    inches = float(input("Enter length in inches (negative value to quit): "))
    if inches < 0:
        print("Program ended.")
        break
    centimeters = inches * INCH_TO_CM
    print(f"{inches} inches is equal to {centimeters:.2f} cm.\n")