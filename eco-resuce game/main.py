from player import Player
from room import Room
from item import Item
print("|||||-----------------------|||||")
print("Welcome to Hood")
print("|||||-----------------------|||||")

print("Welcome to Helsinki city:")
print("Your mission is to protect Helsinki city from pollution.")

name = input("Enter your name: ")
age = int(input("Enter your age: "))

if age < 12:
    print("You are a minor.")
    print("You can't play this game.")
    print("Game closed***")
    exit()

print("Welcome", name)
print("Your age:", age)
print("You can play this game.")


# Creating items

plastic_bottle = Item("Plastic bottle", 0.5)
trash_bag = Item("Trash bag", 1)
recycling_box = Item("Recycling box", 2)


# Creating rooms

helsinki = Room("Helsinki")
river = Room("River", plastic_bottle)
forest = Room("Forest", trash_bag)
city_centre = Room("City Centre", recycling_box)


# Creating player

player = Player(name, helsinki)


# List for environmental actions

actions = []


def add_action():
    action = input("Enter an action that you will take: ")
    actions.append(action)
    print("Action added successfully!")


def show_actions():
    print("\n##### Your environmental actions #####")

    if len(actions) == 0:
        print("You have not added any actions yet.")
    else:
        for action in actions:
            print("-", action)


def instructions():
    print("\n##### INSTRUCTIONS #####")
    print("Your mission is to protect Helsinki city from pollution.")
    print("You can choose different paths according to your choice.")
    print("You can visit the river, forest and city centre.")
    print("You can also collect items and add your own environmental actions.")


def river_story():

    print("\nYou arrived at the river.")

    print("1 - Clean the river and properly dispose of waste.")
    print("2 - Ignore all the problems related to the river.")

    choice = int(input("Enter the choice: "))

    if choice == 1:
        print("You cleaned the river and protected aquatic animals.")
        print("The river becomes cleaner than ever.")
        print("You become the River Guardian!")

    elif choice == 2:
        print("You ignored all the river problems.")
        print("Aquatic animals suffer because of pollution.")
        print("Game over.")

    else:
        print("Invalid choice.")


def forest_story():

    print("\nYou entered the forest.")

    print("1 - Plant more trees and clean litter.")
    print("2 - Ignore the forest's problems.")

    choice = int(input("Enter the choice: "))

    if choice == 1:
        print("You planted many trees.")
        print("You also stopped hunting and poaching.")
        print("Now the forest is greener than ever!")

    elif choice == 2:
        print("You ignored all the problems of the forest.")
        print("The forest habitat was destroyed.")
        print("Animals entered the city.")

    else:
        print("Invalid choice.")


def city_story():

    print("\nYou arrived at Helsinki City Centre.")

    print("1 - Impose strict laws and inspire people.")
    print("2 - Ignore all the problems.")

    choice = int(input("Enter the choice: "))

    if choice == 1:
        print("You imposed strict laws against pollution.")
        print("You inspired people to walk and ride bicycles.")
        print("Pollution decreased a lot!")

    elif choice == 2:
        print("You ignored all the problems of Helsinki.")
        print("Helsinki became one of the most polluted cities.")

    else:
        print("Invalid choice.")


def start_game():

    print("\nStarting game---")
    print("You are now at Helsinki.")
    print("Your mission is to protect Helsinki.")

    playing = True

    while playing:

        print("\n========== GAME MENU ==========")
        print("1 - Go to River")
        print("2 - Go to Forest")
        print("3 - Go to City Centre")
        print("4 - Collect item")
        print("5 - Show collected items")
        print("6 - Add environmental action")
        print("7 - Show environmental actions")
        print("8 - Show current location")
        print("9 - Return to main menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            player.move(river)
            river_story()

        elif choice == "2":
            player.move(forest)
            forest_story()

        elif choice == "3":
            player.move(city_centre)
            city_story()

        elif choice == "4":
            player.collect_item()

        elif choice == "5":
            player.show_items()

        elif choice == "6":
            add_action()

        elif choice == "7":
            show_actions()

        elif choice == "8":
            print("Your current location is:", player.location.name)

        elif choice == "9":
            print("Returning to main menu-----")
            playing = False

        else:
            print("Invalid choice.")
            print("Please choose a valid option.")


# Main menu

running = True

while running:

    print("\n========== MAIN MENU ==========")
    print("1 - Start game")
    print("2 - Instructions")
    print("3 - Add environmental action")
    print("4 - Show my environmental actions")
    print("Type lopeta to quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        start_game()

    elif choice == "2":
        instructions()

    elif choice == "3":
        add_action()
    elif choice == "4":
        show_actions()
    elif choice == "lopeta":
        print("Exiting from the game-----")
        print("Goodbye!")
        running = False
    else:
        print("Invalid choice.")
        print("Please choose a valid command.")
print("Follow for more games and updates!")