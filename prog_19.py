'''Write a function that takes a list of integers and returns True if the list is sorted in ascending order, and False otherwise.'''


def is_sorted(numbers):
    # Iterate through the list of numbers and check if each element is greater than or equal to the previous element
    for i in range(1, len(numbers)):
        if numbers[i] < numbers[i - 1]:
            return False
    # If all elements are in ascending order, return True
    return True


print(is_sorted(numbers=[1, 2, 3, 4, 5]))
