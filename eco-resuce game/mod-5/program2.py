a=int(input("enter the value in inches:"))
while(a<0):
    print("value shouldn't be negative:")
    exit()
else:
    cm=a*2.54
    print("value in centimeter:",cm)
print("thank you:")
