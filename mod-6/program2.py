str=[]
number=input("enter the number or press enter to quit:")
while(number!=""):
    str.append(number)
    number=input("enter the number or press enter to quit:")
for i in str:
    order=sorted(str,reverse=True)
print(order)
