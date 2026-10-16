def calculate_sum(numbers):
    total = 0
    for number in numbers:
        total += number
    return total
my_numbers = [10, 20, 30, 40, 50]
result = calculate_sum(my_numbers)
print("The sum is:", result)