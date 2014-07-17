import sys

class Board(object):
	""" Internal constants of the game of Tic Tac Toe. """
	N      = 3
	CIRCLE = 1
	EMPTY  = 0
	CROSS  = 2

	board = [[]]
	
	def __init__(self):
		self.board = [[Board.EMPTY for i in xrange(Board.N)] for i in xrange(Board.N)]
	
	def clear_board(self):
		for i in xrange(Board.N):
			for j in xrange(Board.N):
				self.board[i][j] = Board.EMPTY
	
	def draw_border(self):
		sys.stdout.write("             +")
		for i in xrange(Board.N):
			if i == Board.N - 1:
				sys.stdout.write("---")
			else:
				sys.stdout.write("----")
		sys.stdout.write("+\n")
	
	def print_board(self):
		sys.stdout.write("               ")
		for i in xrange(Board.N):
			sys.stdout.write(str(i+1) + "   ")
		print ""
		
		self.draw_border()
		row_char = 'A'
		
		for i in xrange(Board.N):
			sys.stdout.write("           " + row_char)
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
		print ""
		
	def make_move(self, row, col, seed):
		r = ord(row) - ord('a')
		c = int(col) - 1	
		self.board[r][c] = seed
		
	def is_cell_empty(self, row, col):
		r = ord(row) - ord('a')
		c = int(col) - 1	
		return self.board[r][c] == Board.EMPTY
		
	def check_for_win(self, row, col, seed):
		r = ord(row) - ord('a')
		c = int(col) - 1
	
		if self.board[r][0] == seed and self.board[r][1] == seed and self.board[r][2] == seed:
			return True
		if self.board[0][c] == seed and self.board[1][c] == seed and self.board[2][c] == seed:
			return True
		if self.board[0][0] == seed and self.board[1][1] == seed and self.board[2][2] == seed:
			return True
		if self.board[0][2] == seed and self.board[1][1] == seed and self.board[2][0] == seed:
			return True
		
		return False
		
	def check_draw(self):
		for i in xrange(Board.N):
			for j in xrange(Board.N):
				if self.board[i][j] == Board.EMPTY:
					return False
		
		return True
	
	def is_valid_move(self, move):
		if move == 'exit':
			return True
		if len(move) != 2:
			return False
		if move[0] != 'a' and move[0] != 'b' and move[0] != 'c':
			return False
		if int(move[1]) > 3 or int(move[1]) < 1:
			return False
		if not self.is_cell_empty(move[0], move[1]):
			return False
			
		return True