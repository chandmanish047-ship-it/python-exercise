import random
def dice_roll():
    dice=random.randint(1,6)
    print(dice)
print("the result of dice roll:")
result=dice_roll()
while result!=6:
    result=dice_roll()
print(result)
