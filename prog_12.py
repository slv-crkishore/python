'''Write a function that takes a list of strings and returns a new list with all strings in lowercase.'''


def lower_case():
    string = input("enter strings : ").split(" ")
    temp = [ch.lower() for ch in string]
    return temp


print(lower_case())
