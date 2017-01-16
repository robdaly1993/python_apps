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
            
			
			
example 2:
Create a function named word_count() that takes a string. Return a dictionary with
 each word in the string as the key and the number of times it appears as the value

# E.g. word_count("I am that I am") gets back a dictionary like:
# {'i': 2, 'am': 2, 'that': 1}
# Lowercase the string to make it easier.
# Using .split() on the sentence will give you a list of words.
# In a for loop of that list, you'll have a word that you can
# check for inclusion in the dict (with "if word in dict"-style syntax).
# Or add it to the dict with something like word_dict[word] = 1.


def word_count(iterable):
    list_of_words = []
    iterable.lower()
    list_of_words =  iterable.spilt()     
    
    for word in list_of_words:
        count = 0
        if word in iterable.keys():
            iterable[word] = count
            count = count +1
        return iterable
		
example 4:
Create a function named string_factory that accepts a list of dictionaries and a string.
 Return a new list built by using .
format() on the string, filled in by each of the dictionaries in the list.

dicts = [
    {'name': 'Michelangelo',
     'food': 'PIZZA'},
    {'name': 'Garfield',
     'food': 'lasanga'},
    {'name': 'Walter',
     'food': 'pancakes'},
    {'name': 'Galactus',
     'food': 'worlds'}
]

string = "Hi, I'm {name} and I love to eat {food}!"

def string_factory(dicts, string):
    strings = []
    for a_dict in dicts:
        strings.append(string.format(**dicts))
    return strings    

	
	
example 5:
Create a function named most_classes that takes a dictionary of teachers.
 Each key is a teacher's name and their value is a list of classes they've taught. 
most_classes should return the teacher with the most classes.

# The dictionary will be something like:
# {'Jason Seifer': ['Ruby Foundations', 'Ruby on Rails Forms', 'Technology Foundations'],
#  'Kenneth Love': ['Python Basics', 'Python Collections']}
#
# Often, it's a good idea to hold onto a max_count variable.
# Update it when you find a teacher with more classes than
# the current count. Better hold onto the teacher name somewhere
# too!
#
# Your code goes below here.
dict_of_tech = {'Jason Seifer': ['Ruby Foundations', 'Ruby on Rails Forms', 'Technology Foundations'],
                'Kenneth Love': ['Python Basics', 'Python Collections']}

def most_classes(dict_of_tech):
    most_class = ""
    max_count = 0
    
    for teacher in dict_of_tech:
        
        if len(dict_of_tech[teacher]) > max_count:
            max_count =len(dict_of_tech[teacher])
            most_class = teacher
    
    return most_class

	
	
	
	
	
	
	Now, create a function named stats that takes the teacher dictionary. Return a list of lists in the format [<teacher name>, <number of classes>].
	For example, one item in the list would be ['Dave McFarland', 1].
	
	
	
	
def num_teachers(dicts):
    count = 0
    for key in dicts:
        count = count +1
    return count 
        			
					
					Challenge Task 3 of 4

Now, create a function named stats that takes the teacher dictionary. Return a list of lists in the format [<teacher name>, <number of classes>].
For example, one item in the list would be ['Dave McFarland', 1].

def  stats(dicts):
    num_classes = []
    for k,v in dicts.items():
        new_list = [k, len(v)]
        num_classes.append(new_list)
    return num_classes    



