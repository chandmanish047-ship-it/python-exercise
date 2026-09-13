str=[]
num=input("enter the number or press enter to stop:")
while num!="":
    str.append(num)
    num=input("enter the number or press enter to stop:")
max=max(str)
print("the largest number is:",max)
min=min(str)
print("the smallest number is:",min)