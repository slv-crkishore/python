'''count the number of vowel characters in a string'''


def count_vowels(string_input):

    count = 0
    for items in string_input:
        if items.lower() == 'a' or items.lower() == 'e' or items.lower() == 'i' or items.lower() == 'o' or items.lower() == 'u':
            count += 1

    if count >= 1:
        return count
    else:
        print("No vowel found")


print(count_vowels(string_input=input(
    "enter the string to count the number of vowels:")))
