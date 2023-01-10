'''Write a function that takes in a dictionary and returns a new dictionary with all the keys and values reversed.'''


def rev_dict():
    dic = {
        'name': "kishore",
        "age": "26"
    }
    temp = {(value, key) for key, value in dic.items()}
    return temp


print(rev_dict())
