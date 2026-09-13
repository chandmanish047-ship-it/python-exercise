cities=[]
names=input("enter the name of cities or press enter to quit:")
while(names!=""):
    cities.append(names)
    names=input("enter the name of cities or press enter to quit:")
for i in cities:
    print(i)