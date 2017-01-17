import random

CELLS = [(0,0), (0,1), (0,2),
		 (1,0), (1,1), (1,2),
		 (2,0), (2,1), (2,2)]

def get_locations():
	#monst = random
	monster = random.choice(CELLS)
	#door = random
	door = random.choice(CELLS)
	#start = random
	start = random.choice(CELLS)
	
	#if monster, door, or start at the same, do it again,
	if monster == door or monster == start or door == start:
		return get_locations()
	return monster, door, start
	
	
	
	#return monster, door , start
	
def move_player(player, move):
	#player = x, y
	x, y = player
	
	#get plkayer current location
	#if move is left, y -1
	#if move is right, y+1
	#if move is up, x-1
	#if move is down, x+1
	if move == "LEFT":
		y -= 1
	elif move == "RIGHT":
		y += 1
	elif move == "UP":
		x -= 1
	elif move == "DOWN":
		x += 1
	return x, y	
	


	
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

def draw_map(player):
	print(' - - - ')
	tile= '|{}'
	
	for idx, cell in enumerate(CELLS):
		if idx in [0,1,3,4,6,7]:
			if cell == player:
				print(tile.format('X'), end='')
			else:
				print(tile.format('_'), end='')
		else:
			if cell == player:
				print(tile.format('X|'))
			else:	
				print(tile.format('_|'))

monster, door, player = get_locations()
print("Welcome to the dungeon")

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
	#if good move change the player pos
	if move in moves:
		player = move_player(player, move)
	#if its bad move dont do anything
	else:
		print("walls are hard, stop walking into them")
		continue
	#if the new player posti is the door, they win
	if player == door:
		print("you escaped")
		break
	#if the new player pos is monster, they loose		
	elif player == monster:
		("you were eaten by the grue!")
		break

	