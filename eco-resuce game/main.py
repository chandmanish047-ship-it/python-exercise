print("|||||-----------------------|||||")
print("Welcome to Hood")
print("|||||-----------------------|||||")
print("welcome to Helsinki city:")
print("your mission is to protect helsinki city from pollution:")
name=input("enter your name:")
age=int(input("enter the age:"))
print("welcome",name)
print("your age",age,"years old")
def instruction():
    print("#####instructions#####")
    print("your mission is to protect helsinki city from pollution:")
    print("you can choose different paths according to your choice:")
    print("each path have different ending story:")
print("Main menu")
print("1-Start game")
print("2-Instructions")
print("3-Quit")
choice=int(input("enter the choice:"))
if choice==1:
    print("starting-game---")
    print("you are now at Helsinki:")
    print("your mission is to protect helsinki:")
    print("you can choose different routes:")
    print("where do you want to go?")
    print("1-River")
    print("2-Forest")
    print("3-City centre")
    print("4-return to main menu")
    route=int(input("enter the route number:"))
    if(route==1):
        print("1-You clean and dumped the waste nearby and in river also you fed the fishes and ducks:")
        print("2-you ignored all the problem related to river and moved on:")
        river_choice=int(input("enter the choice of river way:"))
        if(river_choice==1):
            print("you cleaned the river and fed the aquatic animals:")
            print("river becomes cleaner than ever:")
            print("you become river gaurdian:")
        elif(river_choice==2):
            print("you ignored all the river problem and moved on:")
            print("aquatic animals dies because they can't get enough food and pure river:")
            print("Game over:")
        else:
            print("Invalid choice:")
    elif(route==2):
        print("you entered through forest:")
        print("1-you planted more and more trees and cleaned the litter caused by people:")
        print("2-you just ignored forest's problem and starting moving on")
        path=int(input("enter the path you want to choose:"))
        if(path==1):
            print("you planted a lot more trees and stopped hunting and poaching of wild animal:")
            print("Now the jungle is most green as ever:")
        if(path==2):
            print("you just ignored all the problems of jungle and started moving on:")
            print("Jungle habitat got destroyed and animals entered in city due to which hunting and poaching increased a lot:")
        else:
            print("Invalid choice:")
    elif(route==3):
        print("1-imposed strict law and order and inspiring people:")
        print("2-just ignoring all the problem and leaving the city as it was earlier:")
        option=int(input("enter the choices:"))
        if(option==1):
            print("you emposed strict laws and order on those who spit anywhere in city:")
            print("you inspired people to ride bicycles or by foot and it reduced pollution a lot:")
        elif(option==2):
            print("you just ignored all the problems of Helsinki city and moved on from here:")
            print("Helsinki be came the most polluted city in the world:")
        else:
            print("invalid choice:")
    elif(route==4):
        print("Returning to main menu-----")
        print("ThanK you for playing this game::::")
        print("The End:::::::")
        running=False
    else:
        print("choose between 1,2,3,4 only")
if(choice==1):
    print("Clean the dump and wastes near river body and make it's water portable:")
    print("you have to fed all the fishes,ducks and other aquatic animals living in and near water bodies:")
elif choice==2:
    print("protect Helsinki from threat of pollution:")
    print("You have to choose different paths according to your choice:")
    print("Each part have different ending story:")
elif choice==3:
    print("exiting from the game-----")
    print("Good bye")
    running=False
else:
    print("invalid choice")
    print("plz choose between 1 to 3:")
    print("Game closed***")
print("Follow for more games and updates:")


