'''Write a function that takes a list of strings and a string as arguments, and returns the number of times the string appears in the list.'''


def string_appear(string, strings):
    count = 0
    for ch in strings:
        if ch == string:
            count += 1
    return count


print(string_appear(string="bird", strings=input("enter the strings : ").split()))
