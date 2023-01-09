'''Write a function that takes a list of integers and returns the largest product that can be obtained by multiplying any three integers in the list. For example, if the list is [1, 2, 3, 4, 5], the function should return 60, since 4 * 5 * 3 is the largest product that can be obtained by multiplying any three integers in the list.'''


def product(numbers):

    temp = []
    for num in numbers:
        temp.append(num)

    temp = sorted(list(map(int, temp)))
    res = temp[-1]*temp[-2]*temp[-3]

    return res


print(product(numbers=input("enter the numbers :")))
