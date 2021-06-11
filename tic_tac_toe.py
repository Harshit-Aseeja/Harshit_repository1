board=(" 1 | 2 | 3 \n-----------\n 4 | 5 | 6 \n-----------\n 7 | 8 | 9 ")
updated_board=board
player1_sym='x'
player2_sym='O'
possible_index=[1,2,3,4,5,6,7,8,9,10]
updated_board=board
game_over=False

def display_board():
	global updated_board
	print(updated_board)

def choose_symbol():
	
	valid_input=False
	while valid_input==False:
		global player1_sym
		player1_sym=input("Player 1: do you wanna be X or O ?\n\n")
		if player1_sym not in ['x','o','X','O']:
			print("Invalid input")
		elif player1_sym in ['x','o','X','O']:
			valid_input=True
	global player2_sym
	if player1_sym=="X" or player1_sym=="x":
		player2_sym= 'O'
	else:
		player2_sym='X'
	print(f'player 1 is {player1_sym} and player 2 is {player2_sym}\n\n')

def choose_index():
	valid_input=False
	global used_index
	used_index=[]
	global turn
	while valid_input==False:
		global index_pos
		index_pos='y'
		
		global possible_index
		if turn%2==0:
			print("\nPlayer 2:")
		else:
			print("\nPlayer 1:")
		
		
		index_pos=input("\nWhere do you wanna place your mark ?\n\n")

		if index_pos.isdigit()==False:
			print("invalid valid_input")
		if index_pos.isdigit()==True:
			if int(index_pos) not in possible_index:
				print("Invalid input")
			elif int(index_pos) in possible_index:
				if int(index_pos) not in used_index:
					valid_input=True
				elif int(index_pos) in used_index:
					print("Invalid input")
				
				used_index.append(int(index_pos))
			
def mark_placer():
	global updated_board
	global used_index
	if (turn+1)%2==0:
		updated_board=updated_board.replace(f"{index_pos}",f"{player1_sym}")
		
	elif (turn+1)%2!=0:
		updated_board=updated_board.replace(f"{index_pos}",f"{player2_sym}")
	

	display_board()
	print(f'\n\nturn:{turn}')
	# print(used_index)

def winner():
	#1,5,9,25,29,33,49,53,57
	global game_over
	global updated_board
	global turn
	
	if updated_board[1]==updated_board[5] and updated_board[5]==updated_board[9]:
		game_over=True
	elif updated_board[25]==updated_board[29] and updated_board[29]==updated_board[33]:
		game_over=True
	elif updated_board[49]==updated_board[53] and updated_board[53]==updated_board[57]:
		game_over=True
	elif updated_board[1]==updated_board[29] and updated_board[29]==updated_board[57]:
		game_over=True
	elif updated_board[1]==updated_board[25] and updated_board[25]==updated_board[49]:
		game_over=True
	elif updated_board[5]==updated_board[29] and updated_board[29]==updated_board[53]:
		game_over=True
	elif updated_board[9]==updated_board[33] and updated_board[33]==updated_board[57]:
		game_over=True
	elif updated_board[9]==updated_board[29] and updated_board[29]==updated_board[49]:
		game_over=True
	elif turn >9:
		game_over=True

def ttt():
	global turn
	turn=1
	print("Welcome to tic tac toe\n\n")
	choose_symbol()
	print(board,"\n\n")
	
	global game_over
	while game_over==False :
		choose_index()
		mark_placer()
		winner()
		# print(game_over)
		turn+=1
	if turn > 9:
		print("It's a Draw!")
	elif turn%2==0:
		print("Congratulations!, Player 1 won\n")
	else:
		print("Congratulations! Player 2 won\n")

	
	play_again()

def play_again():
	global game_over
	game_over=False
	global turn
	turn=1
	global updated_board
	updated_board=board
	valid_input=False
	while valid_input==False:
		game_continue=input("Do you wanna play again(y/n) ? ")
		if game_continue not in ['y','n']:
			print("Invalid input")
		elif game_continue in ['y','n']:
			valid_input=True
	if game_continue=="y":
		ttt()
	elif game_continue=='n':
		print("Goodbye")
		pass
	else:
		pass


ttt()
