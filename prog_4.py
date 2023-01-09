''' find the largest number in the list of given integers'''


def largest_number():
    numbers = list(input("enter the numbers:"))
    temp = float("-inf")
    for num in numbers:
        if temp < int(num):
            temp = int(num)

    return temp


print(largest_number())
