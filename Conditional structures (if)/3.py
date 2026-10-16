gender = input("Enter your biological gender (female/male): ")
hemoglobin = float(input("Enter your hemoglobin value (g/l): "))
if gender in ["female", "f"]:
    if hemoglobin < 117:
        print("Your hemoglobin value is low.")
    elif 117 <= hemoglobin <= 155:
        print("Your hemoglobin value is normal.")
    else:
        print("Your hemoglobin value is high.")
elif gender in ["male", "m"]:
    if hemoglobin < 134:
        print("Your hemoglobin value is low.")
    elif 134 <= hemoglobin <= 167:
        print("Your hemoglobin value is normal.")
    else:
        print("Your hemoglobin value is high.")
else:
    print("Invalid gender entered. Please type 'female' or 'male'.")