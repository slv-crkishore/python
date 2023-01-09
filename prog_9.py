'''Write a python function that takes a list of integers and returns True if the list contains any duplicates, and False otherwise.'''


def has_duplicates(numbers):
    temp = [int(i) for i in numbers]
    num_set = set()
    for num in temp:
        if num in num_set:
            return True
        else:
            num_set.add(num)
    return False


print(has_duplicates(numbers=input("enter numbers : ").split(" ")))
