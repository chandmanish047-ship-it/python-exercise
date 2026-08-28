print("LUX")
print("A")
print("B")
print("C")
category=input("enter the cabin-class:")
if(category=="LUX"):
    print("you will get upper deck cabin with balcony:")
elif(category=="A"):
    print("you will get your cabin above the car deck,equipped with a window:")
elif(category=="B"):
    print("you will get your cabin above the car deck,without the window:")
elif(category=="C"):
    print("you will get your cabin below the car deck,without the window:")
else:
    print("invalid cabin class:")
print("Thank you:")
