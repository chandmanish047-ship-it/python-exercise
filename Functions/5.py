def remove_odd_numbers(numbers):
    result = []
    for number in numbers:
        if number % 2 == 0:
            result.append(number)
    return result
my_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = remove_odd_numbers(my_numbers)
print("Original list:", my_numbers)
print("List without odd numbers:", even_numbers)
