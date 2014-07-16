import sys

class Board(object):
	""" Internal constants of the game of Tic Tac Toe. """
	N      = 3
	CIRCLE = 1
	EMPTY  = 0
	CROSS  = -1

	board = [[]]
	
	def init_board(self):
		self.board = [[Board.CROSS for i in xrange(self.N)] for i in xrange(self.N)]
	
	def draw_border(self):
		sys.stdout.write("   +")
		for i in xrange(Board.N):
			if i == Board.N - 1:
				sys.stdout.write("---")
			else:
				sys.stdout.write("----")
		sys.stdout.write("+\n")
	
	def print_board(self):
		sys.stdout.write("     ")
		for i in xrange(Board.N):
			sys.stdout.write(str(i+1) + "   ")
		print ""
		
		self.draw_border()
		row_char = 'A'
		
		for i in xrange(Board.N):
			sys.stdout.write(" " + row_char)
			sys.stdout.write(" | ")
			for j in xrange(Board.N):
				if self.board[i][j] == Board.CROSS:
					sys.stdout.write("X" + " | ")
				elif self.board[i][j] == Board.EMPTY:
					sys.stdout.write(" " + " | ")
				else:
					sys.stdout.write("O" + " | ")
			print ""
			row_char = chr(ord(row_char) + 1)
		
		self.draw_border()
		
tic = Board()
tic.init_board()
tic.print_board()