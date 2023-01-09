'''find all the palindromes in the given strings'''


# def palindrome(list_items):

#     # for items in list_items:
#     if list_items == list_items[::-1]:
#         print(list_items + " "+"is a palindrome")

#     else:
#         print(list_items + " " + "is" + " not a palindrome")


# palindrome(list_items=input("enter the strings:"))


def pal(list_it):
    temp = ""
    # temp1 = ""
    for items in list_it:
        temp += items
    if temp == list_it:
        # print(temp + " is a palindrome")
        return True
    else:
        # print(list_it + " is not a palindrome")
        return False


print(pal(list_it=input("enter the strings:")))
