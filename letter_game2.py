import os
import random
import sys

#make a list of words
words = ["apples", "banana","coconut", "lime", "orange", "kumquat"]


def clear():
	if os.name =="nt":
		os.system("cls")
	else:
		os.system("clear")
		
def draw(bad_guesses, good_guesses, secret_word):
	clear()
	print("")
	print("Strikes: {}/7".format(len(bad_guesses)))
	
	for letter in bad_guesses:
		print(letter, end=" ")
	print("\n\n")	
		
	
	for letter in secret_word:
		if letter in good_guesses:
			#end="" does is allow print to print muliple times on the same line 
			print(letter, end="")
		else:
			print("_", end="")

	print("")	
	
def get_guess(bad_guesses, good_guesses):
		#take guess
		while True:
			guess = input("guess a letter: ".lower())
				
			#if user enter more than one char
			if len(guess) !=1:
				print("You can only guess a single letter!")
				
			#if guess is in the bad guess or good guess then tell user they entered that char already
			elif guess in bad_guesses or guess in good_guesses:
				print("You've already guessed that letter!")
				
			elif not guess.isalpha():
				print("you can only guess letters!")
				
			else:
				return guess
    	
def welcome():
	start = input("Press enter/return to start or Q to quit").lower()
	if start == "q":
		print("Bye")
		sys.exit()
	else:
		return True		
	
def play(done):
	clear()
	secret_word = random.choice(words)
	bad_guesses = []
	good_guesses = []
	
	while True:
		draw(bad_guesses, good_guesses, secret_word)
		guess = get_guess(bad_guesses, good_guesses)
		
		if guess in secret_word:
			good_guesses.append(guess)
			found = True
			for letter in secret_word:
				if letter not in good_guesses:
					found= False
			if found: 
				print("You win! The word was {}".format(secret_word))
				done = True
		else:
			bad_guesses.append(guess)
			if len(bad_guesses) == 7:
				draw(bad_guesses, good_guesses, secret_word)
				print("You lost!")
				print("The secret word was {}".format(secret_word))
				done = True
			
		if done:
			play_again = input("play again Y/n").lower()
			if play_again != "n":
				return play(done=False)
			else:
				sys.exit()

print("welcome to letter guess!")

done = False
while True:
	clear()
	welcome()
	play(done)
	