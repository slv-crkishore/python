'''counting the occurences of integer 19 in a list of items'''


def count(list_items):

    count = 0
    for items in list_items:
        if items == 19:
            count += 1

    print(count)


count(list_items=[10, 11, 12, 19, 19, 19, 5, 4, 2, 5])
