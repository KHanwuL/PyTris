import pygame
import sys
from TetrisBoard import GameBoard
from Tetromino import Block
from random_bag import BlockBag, get_random_block
from input_handler import handle_input, handle_input_action
from renderer import draw_board, draw_block, draw_ghost_block, draw_preview, draw_hold, draw_ui, WIDTH, HEIGHT

class Pytris:
  def __init__(self):
    pygame.init()
    pygame.font.init()
    
    self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Pytris")
    self.clock = pygame.time.Clock()
    self.board = GameBoard()
    self.bag = BlockBag()
    self.current_block = get_random_block(self.board, self.bag)
    self.next_block = get_random_block(self.board, self.bag)
    self.hold_block = None
    self.can_hold = True
    self.fall_time = 0
    self.game_over = False
    self.level = 1
    self.fall_speed = 1000 / (1 + self.level)
    
  def spawn_new_block(self):
    self.current_block = self.next_block
    self.next_block = get_random_block(self.board, self.bag)
    self.can_hold = True
    if self.current_block.isCollisionAt(self.current_block.Xpos, self.current_block.Ypos):
      self.game_over = True
  
  def hold_current_block(self):
    if not self.can_hold:
      return
    
    if self.hold_block is None:
      self.hold_block = self.current_block.shape_name
      self.current_block = self.next_block
      self.next_block = get_random_block(self.board, self.bag)
    else:
      temp_shape = self.hold_block
      self.hold_block = self.current_block.shape_name
      self.current_block = Block(GameBoard.MAP_WIDTH // 2 - 1, 1, temp_shape, self.board)
    self.can_hold = False
  
  def handle_block_landing(self):
    self.board.merge(self.current_block)
    self.board.clearLine()
    if self.board.line_count >= 10:
      self.level += 1
      self.fall_speed = 1000 / (1 + self.level)
      self.board.line_count = 0
    self.spawn_new_block()
  
  def update(self, dt):
    if self.game_over:
      return
    self.fall_time += dt
    if self.fall_time >= self.fall_speed:
      if self.current_block.isFallable():
        self.current_block.moveBlock(0, 1)
      else:
        self.handle_block_landing()
      self.fall_time = 0
  
  def draw(self):
    self.screen.fill((0, 0, 0))
    draw_board(self.screen, self.board)
    if not self.game_over:
      ghost_drop_y = self.current_block.checkDropPosition()
      draw_ghost_block(self.screen, self.current_block, ghost_drop_y)
      draw_block(self.screen, self.current_block)
      draw_preview(self.screen, self.next_block)
      draw_hold(self.screen, self.hold_block)
      draw_ui(self.screen, self)
    pygame.display.flip()
  
  def run(self):
    running = True
    while running:
      dt = self.clock.tick(60)
      action = handle_input()
      if action == "quit":
        running = False
      elif action and not self.game_over:
        handle_input_action(action, self)
      self.update(dt)
      self.draw()
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
  game = Pytris()
  game.run()
