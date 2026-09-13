import random
number=int(input("enter the number of dice to roll:"))
i=0
for i in range(number):
    roll=random.randint(1,6)
    i=i+roll
print(i)