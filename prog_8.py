'''Write a Python function that takes a list of integers and returns the sum of the even numbers in the list.'''


def sum_even():
    numbers = input("enter the numbers :")
    temp = []

    for i in numbers:
        # breakpoint()
        temp.append(int(i))

    res = sum([n for n in temp if n % 2 == 0])
    print(res)


sum_even()
