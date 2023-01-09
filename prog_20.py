'''How do you check if a number is even in Python?'''


def even_number():
    print("Enter a number")
    number = int(input())
    if number % 2 == 0:
        print("The number is even")
    else:
        print("The number is odd")


even_number()
