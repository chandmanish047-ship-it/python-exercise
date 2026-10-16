airports = {}
while True:
    print("\nChoose an option:")
    print("1. Enter a new airport")
    print("2. Fetch airport information")
    print("3. Quit")
    choice = input("Enter your choice (1-3): ")
    if choice == "1":
        icao = input("Enter the ICAO code: ").upper()
        name = input("Enter the airport name: ")
        airports[icao] = name
        print("Airport saved.")
    elif choice == "2":
        icao = input("Enter the ICAO code to search: ").upper()
        if icao in airports:
            print("Airport name:", airports[icao])
        else:
            print("Airport not found.")
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please choose 1, 2, or 3.")
