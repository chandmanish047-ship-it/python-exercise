
print("|||||-----------------------|||||")
print("Welcome to Hood")
print("|||||-----------------------|||||")

print("welcome to Helsinki city:")
print("your mission is to protect helsinki city from pollution:")

name = input("enter your name:")
age = int(input("enter the age:"))

if age<12:
    print("You are a minor.")
    print("you can't play this game:")
    print("Game closed***")
    exit()
else:
    print("welcome", name)
    print("your age:",age)
    print("you can play this game:")

running = True

while running:

    print("\nMain menu")
    print("1-Start game")
    print("2-Instructions")
    print("Type lopeta to quit")

    choice = input("enter the choice:")

    if choice == "1":

        print("starting-game---")
        print("you are now at Helsinki:")
        print("your mission is to protect helsinki:")
        print("you can choose different routes:")
        print("where do you want to go?")

        print("1-River")
        print("2-Forest")
        print("3-City centre")
        print("4-return to main menu")

        route = int(input("enter the route number:"))

        if route == 1:

            print("1-You clean and dump the waste nearby and in river.")
            print("2-you ignored all the problem related to river and moved on:")

            river_choice = int(input("enter the choice of river way:"))

            if river_choice == 1:

                print("you cleaned the river and fed the aquatic animals:")
                print("river becomes cleaner than ever:")
                print("you become river guardian:")

            elif river_choice == 2:

                print("you ignored all the river problem and moved on:")
                print("aquatic animals suffer because of pollution:")
                print("Game over:")

            else:
                print("Invalid choice:")

        elif route == 2:

            print("you entered through forest:")
            print("1-you planted more and more trees and cleaned the litter caused by people:")
            print("2-you just ignored forest's problem and started moving on")

            path = int(input("enter the path you want to choose:"))

            if path == 1:

                print("you planted a lot more trees and stopped hunting and poaching of wild animals:")
                print("Now the jungle is greener than ever:")

            elif path == 2:

                print("you just ignored all the problems of jungle and started moving on:")
                print("Jungle habitat got destroyed and animals entered in city:")

            else:
                print("Invalid choice:")

        elif route == 3:

            print("1-imposed strict law and order and inspiring people:")
            print("2-just ignoring all the problem and leaving the city as it was earlier:")

            option = int(input("enter the choices:"))

            if option == 1:

                print("you imposed strict laws and order on those who pollute the city:")
                print("you inspired people to ride bicycles or walk:")
                print("it reduced pollution a lot:")

            elif option == 2:

                print("you just ignored all the problems of Helsinki city:")
                print("Helsinki became the most polluted city in the world:")

            else:
                print("invalid choice:")

        elif route == 4:

            print("Returning to main menu-----")

        else:

            print("choose between 1,2,3,4 only")

    elif choice == "2":

        print("#####instructions#####")
        print("your mission is to protect helsinki city from pollution:")
        print("you can choose different paths according to your choice:")
        print("each path has different ending story:")

    elif choice == "3":

        print("You travelled to the river.")
        print("The river is polluted.")
        print("Your mission is to clean the river and protect aquatic animals.")

    elif choice == "4":

        print("You entered the forest.")
        print("You found litter and damaged trees.")
        print("Your mission is to protect the forest.")

    elif choice == "5":

        print("You are now in Helsinki city centre.")
        print("You encouraged people to walk and ride bicycles.")
        print("Pollution has started to decrease.")

    elif choice == "lopeta":

        print("exiting from the game-----")
        print("Good bye")
        running = False

    else:

        print("invalid choice")
        print("plz choose a valid command")

print("Follow for more games and updates:")