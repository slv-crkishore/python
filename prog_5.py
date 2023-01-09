'''find the second largest element in the given integers'''


def second_largest(numbers):

    temp = list()
    for num in numbers:
        temp.append(int(num))
    # breakpoint()
    res = sorted(list(map(int, set(temp))))[-2]
    return res


print(second_largest(numbers=input("enter the numbers:")))
