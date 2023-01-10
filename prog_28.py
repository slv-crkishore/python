'''Write a function that takes in a string and returns the string with all vowels removed.'''


def rem_vowels():
    string = input("enter the string : ")
    temp = [i for i in string]
    for ch in temp:
        if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
            temp.remove(ch)

    return ''.join(temp)


print(rem_vowels())
