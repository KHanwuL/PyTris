import numpy as np
from Tetromino import Block

class GameBoard:
	MAP_WIDTH = 12
	MAP_HEIGHT = 22
	Board = np.zeros((MAP_HEIGHT, MAP_WIDTH), dtype=int)
	line_count = 0

	def __init__(self):
		self.Board[0, :] = 1
		self.Board[-1, :] = 1
		self.Board[:, 0] = 1
		self.Board[:, -1] = 1

	def merge(self, block: Block):
		for dy in range(block.shape.shape[0]):
			for dx in range(block.shape.shape[1]):
				if block.shape[dy, dx] != 0:
					x = block.Xpos + dx
					y = block.Ypos + dy
					if not self.isMergeable(x, y):
						break
					self.Board[y, x] = block.shape[dy, dx]

	def clearLine(self):
		lines_cleared = 0
		y = self.MAP_HEIGHT - 2
		while y > 0:
			if np.all(self.Board[y, 1:self.MAP_WIDTH-1] >= 2):
				self.Board[2:y+1, 1:self.MAP_WIDTH-1] = self.Board[1:y, 1:self.MAP_WIDTH-1]
				self.Board[1, 1:self.MAP_WIDTH-1] = 0
				lines_cleared += 1
			else:
				y -= 1
		self.line_count += lines_cleared
	
	def isMergeable(self, x, y) -> bool:
		if y <= 0 or y >= self.Board.shape[0] or x <= 0 or x >= self.Board.shape[1]:
			return False
		return True