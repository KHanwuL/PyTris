import pygame
from TetrisBoard import GameBoard
from Tetromino import Block

COLORS = {
		0: (0, 0, 0),  # 빈칸
		1: (128, 128, 128),  # 벽
		2: (0, 255, 255),  # I
		3: (255, 255, 0),  # O
		4: (128, 0, 128),  # T
		5: (0, 255, 0),  # S
		6: (255, 0, 0),  # Z
		7: (0, 0, 255),  # J
		8: (255, 165, 0),  # L
}

BLOCK_SIZE = 30
SIDE_WIDTH = 9 * BLOCK_SIZE
WIDTH = GameBoard.MAP_WIDTH * BLOCK_SIZE + 2 * SIDE_WIDTH
HEIGHT = GameBoard.MAP_HEIGHT * BLOCK_SIZE

GAME_X_OFFSET = SIDE_WIDTH
GAME_Y_OFFSET = 0

PREVIEW_X = GAME_X_OFFSET + GameBoard.MAP_WIDTH * BLOCK_SIZE + BLOCK_SIZE * 2
PREVIEW_Y = BLOCK_SIZE * 2


def draw_board(screen, board: GameBoard):
	for y in range(GameBoard.MAP_HEIGHT):
		for x in range(GameBoard.MAP_WIDTH):
			color = COLORS.get(board.Board[y, x], (255, 255, 255))
			pygame.draw.rect(screen, color,
				(GAME_X_OFFSET + x * BLOCK_SIZE,
				GAME_Y_OFFSET + y * BLOCK_SIZE,
				BLOCK_SIZE, BLOCK_SIZE))
			pygame.draw.rect(screen, (50, 50, 50),
				(GAME_X_OFFSET + x * BLOCK_SIZE,
				GAME_Y_OFFSET + y * BLOCK_SIZE,
				BLOCK_SIZE, BLOCK_SIZE), 1)

def draw_block(screen, block: Block):
	for dy in range(block.shape.shape[0]):
		for dx in range(block.shape.shape[1]):
			if block.shape[dy, dx] != 0:
				x = block.Xpos + dx
				y = block.Ypos + dy
				if 0 <= x < GameBoard.MAP_WIDTH and 0 <= y < GameBoard.MAP_HEIGHT:
					color = COLORS.get(block.shape[dy, dx], (255, 255, 255))
					pygame.draw.rect(screen, color,
						(GAME_X_OFFSET + x * BLOCK_SIZE,
						GAME_Y_OFFSET + y * BLOCK_SIZE,
						BLOCK_SIZE, BLOCK_SIZE))
					pygame.draw.rect(screen, (50, 50, 50),
						(GAME_X_OFFSET + x * BLOCK_SIZE,
						GAME_Y_OFFSET + y * BLOCK_SIZE,
						BLOCK_SIZE, BLOCK_SIZE), 1)

def draw_ghost_block(screen, ghost_block: Block, drop_y: int):
	for dy in range(ghost_block.shape.shape[0]):
		for dx in range(ghost_block.shape.shape[1]):
			if ghost_block.shape[dy, dx] != 0:
				x = ghost_block.Xpos + dx
				y = drop_y + dy
				if 0 <= x < GameBoard.MAP_WIDTH and 0 <= y < GameBoard.MAP_HEIGHT:
					original_color = COLORS.get(ghost_block.shape[dy, dx], (255, 255, 255))
					ghost_color = tuple(int(c * 0.3) for c in original_color)
					pygame.draw.rect(screen, ghost_color,
						(GAME_X_OFFSET + x * BLOCK_SIZE,
						GAME_Y_OFFSET + y * BLOCK_SIZE,
						BLOCK_SIZE, BLOCK_SIZE))
					pygame.draw.rect(screen, (50, 50, 50),
						(GAME_X_OFFSET + x * BLOCK_SIZE,
						GAME_Y_OFFSET + y * BLOCK_SIZE,
						BLOCK_SIZE, BLOCK_SIZE), 1)

def draw_preview(screen, next_block: Block):
	shape = next_block.shape
	for dy in range(shape.shape[0]):
		for dx in range(shape.shape[1]):
			if shape[dy, dx] != 0:
				color = COLORS.get(shape[dy, dx], (255, 255, 255))
				px = PREVIEW_X + dx * BLOCK_SIZE
				py = PREVIEW_Y + dy * BLOCK_SIZE
				pygame.draw.rect(screen, color, (px, py, BLOCK_SIZE, BLOCK_SIZE))
				pygame.draw.rect(screen, (50, 50, 50), (px, py, BLOCK_SIZE, BLOCK_SIZE), 1)
	font = pygame.font.SysFont("comicsans", 24)
	label = font.render("NEXT", 1, (255, 255, 255))
	screen.blit(label, (PREVIEW_X, PREVIEW_Y - BLOCK_SIZE))

def draw_ui(screen, game):
	font = pygame.font.SysFont("comicsans", 24)
	level_text = font.render(f"Level: {game.level}", True, (255, 255, 255))
	screen.blit(level_text, (10, 10))
	required_lines = 10
	remaining_lines = required_lines - game.board.line_count
	remaining_text = font.render(f"Next Level: {remaining_lines} lines", True, (255, 255, 255))
	screen.blit(remaining_text, (10, 40))