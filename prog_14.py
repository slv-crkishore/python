'''Write a function that takes a list of words and returns longest word'''


def long_char():
    string = input("enter strings : ").split(" ")
    temp = max(string, key=len)
    return temp


print(long_char())
