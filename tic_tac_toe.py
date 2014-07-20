from board import Board

def print_menu():
	print "     ********************************************"
	print "                    TIC TAC TOE MENU             "
	print "     ********************************************"
	print "     Commands: type in \"exit\" without quotation"
	print "     marks to exit the game. To place a circle or"
	print "     cross on the board, first type the row letter"
	print "     then the column number, e.g. A1, C3, etc..."
	print ""		

def main():
	ttt_board = Board()
	turn = Board.CIRCLE
	move_number = 0
	
	print_menu()
	ttt_board.print_board()
	
	while True:	
		move = raw_input("     Player %d what is your move? " % turn).lower()
		
		while not ttt_board.is_valid_move(move):
			move = raw_input("     Incorrect command. Try again...Player %d what is your move? " % turn).lower()
		
		if move == 'exit':
			return
			
		row = ord(move[0]) - ord('a')
		col = int(move[1]) - 1
		
		ttt_board.make_move(row, col, turn)
		ttt_board.print_board()
		
		if ttt_board.check_for_win(row, col, turn):
			print "     Player %d has won! Congratulations!" % turn
			return
		else:
			if move_number == (Board.N ** 2 - 1):
				print "     The game ended in a draw!"
				return
		
		turn = Board.CROSS if turn == Board.CIRCLE else Board.CIRCLE
		move_number += 1
		
if __name__ == '__main__':
	main()
	