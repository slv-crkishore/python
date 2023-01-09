'''Write a function that takes a list of integers and returns the sum of the elements in the list.'''


def sum_of_list(list_of_ints):

    temp = [int(num) for num in list_of_ints]
    return sum(temp)


print(sum_of_list(list_of_ints=input("enter the numbers : ")))
