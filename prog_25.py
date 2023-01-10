'''Write a function that takes in a string and returns a new string with all the letters in uppercase.'''


def upper():
    string = input("enter the string :").split()
    temp = []
    for ch in string:
        temp.append(ch.upper())

    return " ".join(temp)


print(upper())
