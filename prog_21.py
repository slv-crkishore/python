'''How do you sort a list of dictionaries by a value in the dictionary in Python?'''


# def sort_dict_by_value(dictionary):

#     return sorted(dictionary, key=lambda x: x[1]['name'])


# print(sort_dict_by_value(dictionary=[{'name': 'Alice', 'age': 30},
#                                      {'name': 'Bob', 'age': 25},
#                                      {'name': 'Charlie', 'age': 35},
#                                      ]))

my_list = [{'name': 'Alice', 'age': 30},    {
    'name': 'Bob', 'age': 25},    {'name': 'Charlie', 'age': 35}, ]
sorted_list = sorted(my_list, key=lambda x: x['name'])
print(sorted_list)
