names=set()
while True:
    name=input("enter the name or press enter to quit:")
    if name=="":
        break
    if name in names:
        print("name already exits:")
    else:
        names.add(name)
for name in names:
    print(name)
