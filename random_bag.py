import random
from TetrisBoard import GameBoard
from Tetromino import Block, TETROMINOS

class BlockBag:
	def __init__(self):
		self.bag = []
		self.refill()

	def refill(self):
		self.bag = list(TETROMINOS.keys())
		random.shuffle(self.bag)

	def get(self):
		if not self.bag:
			self.refill()
		return self.bag.pop()
	
def get_random_block(board: GameBoard, bag: BlockBag) -> Block:
	name = bag.get()
	r = random.randint(0, 3)
	x = GameBoard.MAP_WIDTH // 2 - TETROMINOS[name].shape[1] // 2
	y = 1
	return Block(x, y, name, board, r)