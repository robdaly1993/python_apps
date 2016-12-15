#pyhton dictionarys:


example1:

#Write a function named members that takes two 
arguments, a dictionary and a list of keys. Return a
 count of how many of the items in 
 the list are also keys in the dictionary.
 
 # You can check for dictionary membership using the
# "key in dict" syntax from lists.

### Example
# my_dict = {'apples': 1, 'bananas': 2, 'coconuts': 3}
# my_list = ['apples', 'coconuts', 'grapes', 'strawberries']
# members(my_dict, my_list) => 2

some_dict = {'apples': 1, 'bananas': 2, 'coconuts': 3}
key_list = ['apples', 'coconuts', 'grapes', 'strawberries']

def members(some_dict, key_list):
    counter = 0
    for value in key_list:
        for key in some_dict.keys():
            if key == value:
                counter = counter +1
    return counter            
            