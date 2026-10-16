SIZE_LIMIT = 42
length = float(input("Enter the length of the zander in centimeters: "))
if length < SIZE_LIMIT:
    difference = SIZE_LIMIT - length
    print("Please release the fish back into the lake.")
    print(f"The zander is {difference:.1f} cm below the size limit.")
else:
    print("Congratulations! Your zander meets the size limit and you can keep it.")