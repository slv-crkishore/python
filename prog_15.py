'''Write a function that takes a list of words and returns the number of words that are longer than 5 characters'''


def long():
    string = input("enter strings : ").split()
    temp = [i for i in string if len(i) > 5]
    return temp


print(long())
