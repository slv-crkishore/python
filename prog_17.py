'''Write a function that takes a list of strings and a string as arguments, and returns the index at which the string argument first appears in the list. If the string does not appear in the list, return -1.'''


def index(strings, string):

    for i in range(len(strings)):
        if strings[i] == string:
            return i


print(index(string="bird", strings=input("enter the strings : ").split()))
