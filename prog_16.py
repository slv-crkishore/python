'''Write a function that takes a list of numbers and returns the median (middle) value of the list. If the list has an even number of elements, return the average of the two middle values.'''


def find_median(numbers):

    temp = [int(i) for i in numbers]
    temp.sort()
    # Find the length of the list
    length = len(temp)
    # If the length of the list is odd, return the middle value
    if length % 2 == 1:
        return temp[length // 2]
    # If the length of the list is even, return the average of the two middle values
    else:
        return (temp[length // 2 - 1] + temp[length // 2]) / 2


print(find_median(numbers=input("enter the number : ").split()))
