import random
num1=random.randint(1,10)
num2=int(input("enter any number between 1 to 10:"))
while(num1!=num2):
    if(num2<num1):
        print("too low:")
    elif(num2>num1):
        print("too high:")
    num2=int(input("enter again:"))
else:
    print("correct guess:")
print("thank you for playing the game:")