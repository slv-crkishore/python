'''find all the palindromes in the given strings'''


def palindrome():
    list_items = list(input("enter the strings:").split())
    for items in list_items:
        if items == items[::-1]:
            print(items + " "+"is a palindrome")


palindrome()
