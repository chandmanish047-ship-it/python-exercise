import random
dice = int(input("How many dice do you want to roll? "))
total = 0
for i in range(dice):
    roll = random.randint(1, 6)
    print("Dice:", roll)
    total += roll
print("Sum of the dice:", total)