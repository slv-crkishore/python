'''Write a function that takes a list of strings and returns a new list with all strings that start with the letter 'a'.'''


def starts_with(string):

    res = [ch for ch in string if ch.startswith('a')]
    # for ch in string:
    #     if ch.startswith('a'):
    #         res.append(ch)

    return res


print(starts_with(string=input("enter strings : ").split(" ")))
