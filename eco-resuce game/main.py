
print("|||||-----------------------|||||")
print("Welcome to Hood")
print("|||||-----------------------|||||")

print("Welcome to Helsinki city:")
print("Your mission is to protect Helsinki city from pollution:")

name = input("Enter your name: ")
age = int(input("Enter your age: "))

if age < 12:
    print("You are a minor.")
    print("You can't play this game.")
    print("Game closed***")
    exit()
else:
    print("Welcome", name)
    print("Your age:", age)
    print("You can play this game:")


# List for storing pollution actions
actions = []


# Function 1: Ask user for information and add it to a list
def add_action():
    print("\nAdd a new environmental action.")
    action = input("Enter an action you would take to protect Helsinki: ")

    actions.append(action)

    print("Action added successfully!")


# Function 2: Print the contents of the list
def show_actions():
    print("\n##### Your environmental actions #####")

    if len(actions) == 0:
        print("You have not added any actions yet.")
    else:
        for action in actions:
            print("-", action)


# Function 3: Show game instructions
def instructions():
    print("\n##### INSTRUCTIONS #####")
    print("Your mission is to protect Helsinki city from pollution.")
    print("You can choose different paths according to your choice.")
    print("Each path has a different ending story.")
    print("You can also add your own environmental actions.")


# Function 4: Start the game
def start_game():

    print("\nStarting game---")
    print("You are now at Helsinki.")
    print("Your mission is to protect Helsinki.")
    print("You can choose different routes:")

    print("\n1 - River")
    print("2 - Forest")
    print("3 - City centre")
    print("4 - Return to main menu")

    route = int(input("Enter the route number: "))

    if route == 1:

        print("\n1 - Clean the river and properly dispose of waste.")
        print("2 - Ignore all the problems related to the river.")

        river_choice = int(input("Enter the choice: "))

        if river_choice == 1:

            print("You cleaned the river and protected aquatic animals.")
            print("The river becomes cleaner than ever.")
            print("You become the River Guardian!")

        elif river_choice == 2:

            print("You ignored all the river problems.")
            print("Aquatic animals suffer because of pollution.")
            print("Game over.")

        else:
            print("Invalid choice.")

    elif route == 2:

        print("\nYou entered the forest.")
        print("1 - Plant more trees and clean litter.")
        print("2 - Ignore the forest's problems.")

        path = int(input("Enter the path you want to choose: "))

        if path == 1:

            print("You planted many trees.")
            print("You also stopped hunting and poaching.")
            print("Now the forest is greener than ever!")

        elif path == 2:

            print("You ignored all the problems of the forest.")
            print("The forest habitat was destroyed.")
            print("Animals entered the city.")

        else:
            print("Invalid choice.")

    elif route == 3:

        print("\n1 - Impose strict laws and inspire people.")
        print("2 - Ignore all the problems.")

        option = int(input("Enter the choice: "))

        if option == 1:

            print("You imposed strict laws against pollution.")
            print("You inspired people to walk and ride bicycles.")
            print("Pollution decreased a lot!")

        elif option == 2:

            print("You ignored all the problems of Helsinki.")
            print("Helsinki became one of the most polluted cities.")

        else:
            print("Invalid choice.")

    elif route == 4:

        print("Returning to main menu-----")

    else:

        print("Choose between 1, 2, 3 or 4 only.")


# Main program
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