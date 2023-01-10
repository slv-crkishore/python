'''Write a function that takes in a string and returns a new string with all the letters in alphabetical order.'''


def alphabetic_order(string):
    temp = [letter for letter in string]
    temp1 = []
    while temp:
        min = temp[0]
        for i in temp:
            if i < min:
                min = i
        temp1.append(min)
        temp.remove(min)

    return "".join(temp1)


print(alphabetic_order(string=input("enter the string :")))
