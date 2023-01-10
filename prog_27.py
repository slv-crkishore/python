'''Write a function that takes in a list of numbers and returns the sum of the numbers.'''


def sum_numbers(numbers):

    temp = [int(i) for i in numbers]
    # res = 0
    # for i in temp:
    #     res += i

    # return res

    return sum(temp)


print(sum_numbers(numbers=input("enter numbers : ")))
