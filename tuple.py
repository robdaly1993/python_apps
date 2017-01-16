New Terms

dict.items() - A method that returns a list of tuples from a dictionary. Each tuple contains a key and its value.

enumerate() - A function that takes a iterable, like a list, and gives back a list of tuples where each tuple holds the index of the item and its value.

Examples

dict.items()

>>> my_dict = {'name': 'Kenneth', 'age': 33}

>>> for key, value in my_dict.items():

. . . print("{}: {}".format(key, value))

age: 33

name: Kenneth

Since dict.items() gives us a list of tuples, we could do this with unpacking a single variable into str.format().

>>> for group in my_dict.items():

. . . print("{}: {}".format(*group))

enumerate()

>>> my_list = [5, 2, 4, 1, 3]

>>> for index, value in enumerate(my_list):

. . . print("{}: {}".format(index, value))

0: 5

1: 2

2: 4

3: 1

4: 3

We have the same ability here since, again, we're getting a list of tuples.

>>> for group in enumerate(my_list):

. . . print("{}: {}".format(*group))