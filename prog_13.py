'''Write a function that takes a list of numbers and returns the largest number in the list.'''


def large_number(numbers):

    temp = [int(num) for num in numbers]
    return max(temp)


print(large_number(numbers=input("enter  numbers : ").split(" ")))
