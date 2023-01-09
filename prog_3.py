str = [19, 19, 5, 5, 5, 5, 1, 3]


def check(str):
    if str.count(19) == 2 and str.count(5) >= 3:
        return True

    else:
        return False


check(str)
