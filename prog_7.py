'''Write a function that takes a string as input and returns a string with the characters in reverse order. For example, if the input string is "hello", the function should return "olleh".'''


def rev(string):

    return string[::-1]


print(rev(string=input("enter the string you want to reverse:")))
