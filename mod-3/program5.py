talents=int(input("enter the mass in talents:"))
pounds=int(input("enter the mass in pounds:"))
lots=float(input("enter the mass in lots:"))
gram=(talents*20*32*13.3)+(pounds*32*13.3)+(lots*13.3)
kilogram=gram/1000
print("weight is kilogram",kilogram)
