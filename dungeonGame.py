
	import random

CELLS = [(0,0), (0,1), (0,2),
		 (1,0), (1,1), (1,2),
		 (2,0), (2,1), (2,2)]

def get_locations():
	monster = random.choice(CELLS)
	#monst = random
	door = random.choice(CELLS)
	#door = random
	start = random.choice(CELLS)
	#start = random
	if monster == door or monster == start or door == start:
		return get_locations()
	return monster, door, start
	
	#if monster, door, or start at the same, do it again,
	
	#return monster, door , start
	
def move_player(player, move):
	#player = x, y
	x, y = player
	
	if move == "LEFT":
		y -= 1
	elif move == "RIGHT":
		y += 1
	elif move == "UP":
		x -= 1
	elif move == "DOWN":
		x += 1
	return x, y	
	
	#get plkayer current location
	#if move is left, y -1
	#if move is right, y+1
	#if move is up, x-1
	#if move is down, x+1
	return player
	
def get_moves(plyer):
	moves = ['LEFT', 'RIGHT', 'UP', 'DOWN']
	#player = (x,y)
	if player[1] == 0:
		moves.remove("LEFT")
	if player[1] == 2: 
		moves.remove("RIGHT")
	if player[0] == 0: 
		moves.remove("UP")
	if player[0] == 2: 
		moves.remove("DOWN")		
	
		
	#if player's y is 0, remove LEFT
	#if player's x is 0, remove UP
	#if player's y is 2, remove RIGHT
	#if player's x is 2, remove DOWN
	return moves

monster, door, player = get_locations()

while True:
	moves = get_moves(player)
	
	print("Welcome to the dungeon")
	print("your currently in room{}".format(player))
	print("you can move {}".format(moves))
	print("enter quit to quit")
	
	move = input("> ")
	move = move.upper()
	
	if move == "QUIT":
		break
		
	if move in moves:
		player = move_player(player, move)
	else:
		print("walls are hard, stop walking into them")
		continue
	
	if player == door:
		print("you escaped")
		break
	elif player == monster:
		("you were eaten by the grue!")
		break
		
	
	
	#if good move change the player pos
	
	#if its bad move dont do anything
	#if the new player posti is the door, they win
	#if the new plauer pposi is monster

	