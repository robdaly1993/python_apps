import random

#make a list of words
words = ["apples", "banana","coconut", "lime", "orange", "kumquat"]
#start game
while True:
	start = input("please press enter/return to start, or enter Q to quit")
	if(start.lower() == 'q'):
		break
		 
	#pick a random word
	#random.choice picks a random item out of a iterable -> in this case it takes a random word out of our list of words
	secret_word = random.choice(words)
	bad_guesses = []
	good_guesses = []
	
	#while the number of guesses is less than 7 and the number of right guesses is not equal to secret word play.
	#change secret word into list to make sure there the same
	while len(bad_guesses) < 7 and len(good_guesses) != len(list(secret_word)):
		
			#draw spaces
			#draw guessed letters, spaces and strikes
			for letter in secret_word:
				if letter in good_guesses:
					#end=""  print muliple times on the same line 
					print(letter, end="")
				else:
					print("_", end="")
			print("")
			print("Strikes: {}/7".format(len(bad_guesses)))
			print("")	
			
			#take guess
			guess = input("guess a letter: ".lower())
			
			#if user enter more than one char
			if len(guess) !=1:
				print("You can only guess a single letter!")
				continue
			#if guess is in the bad guess or good guess then tell user they entered that char already
			elif guess in bad_guesses or guess in good_guesses:
				print("You've already guessed that letter!")
				continue
			elif not guess.isalpha():
				print("you can only guess letters!")
				continue
			
			if guess in secret_word:
				good_guesses.append(guess)
				if len(good_guesses) == len(secret_word):
					print("You win! The word was {}".format(secret_word))
					break
			else:
				bad_guesses.append(guess)
	else:
			print("you didnt guess it! my secret word was{}".format(secret_word))	