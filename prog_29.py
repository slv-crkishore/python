'''Write a function that takes in a list of strings and returns a new list with all the strings reversed.'''


def rev_str():
    string = input("enter strings : ").split(" ")
    temp = []
    for ch in string:
        temp.append(ch[::-1])

    return temp


print(rev_str())
