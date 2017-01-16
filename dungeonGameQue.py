import random

def nchoices(iterable, n):
    '''Take an iterable and an integer and 
    return a list of n random items from the 
    iterable, where n is the integer.
    Duplicates are allowed.
    '''
    # initialize empty list for results
    results = []
    for index in range(n): #<-- Add loop to run "n" times
        # pick random item
        pick = random.choice(iterable)
        # append pick to results list
        results.append(pick) #<-- in each loop, choose random item from "iterable" and append to results list
    # after looping complete, return results list
    return results
	
	