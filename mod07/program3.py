def litres():
    gallon=int(input("enter the amount in american gallons:"))
    litres=gallon*3.785
    return litres
result=litres()
print("the amount of litres:",result)