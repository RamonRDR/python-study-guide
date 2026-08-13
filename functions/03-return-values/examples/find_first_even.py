def find_first_even(numbers):
    for number in numbers:
        if number % 2 == 0:
            return number

    return None


print(find_first_even([3, 7, 8, 10]))
print(find_first_even([1, 3, 5]))
