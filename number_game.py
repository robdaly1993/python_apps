import random	

# generate a random number between 1 and 10



def game():
	secret_num = random.randint(1,10)
	guesses = []
	
	while len(guesses) < 5:
		#get a number guess from the player
		try:
			guess = int(input("Guess a number between 1 and 10: "))
			if(guess > 10 or guess < 0 ):
				print("out of range")
				continue
		except ValueError:
			print("{} isnt a number!".format(guess))
			
		else:	
			#compare guess to secret number
			
			if guess == secret_num:
				print("you guess correctly! My number was {}".format(secret_num))
				break
			elif guess < secret_num:
				print("My number is higher than {}".format(guess))
			else:
				print("My number is lower than {}".format(guess))
			guesses.append(guess)
	else:
		print("you didnt guess the right number! the number was {}".format(secret_num))
	play_again = input("do you want to play again? Y/n ")
	if play_again.lower() !="n":
		game()
	else:
		print("Bye!")
		
	
game()