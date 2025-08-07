import pygame

def handle_input():
  key_map = {
	  pygame.K_w: "input_drop",
    pygame.K_a: "input_moveL",
    pygame.K_s: "input_moveD",
    pygame.K_d: "input_moveR",
    pygame.K_q: "input_rotateL",
    pygame.K_e: "input_rotateR",
    }
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      return "quit"
    elif event.type == pygame.KEYDOWN:
      return key_map.get(event.key, None)
  return None

def handle_input_action(input, game):
  if input == "input_moveL":
    game.current_block.moveBlock(-1, 0)
  elif input == "input_moveR":
    game.current_block.moveBlock(1, 0)
  elif input == "input_moveD":
    game.current_block.moveBlock(0, 1)
  elif input == "input_rotateL":
    game.current_block.rotateShapeLeft()
  elif input == "input_rotateR":
    game.current_block.rotateShapeRight()
  elif input == "input_drop":
    drop_y = game.current_block.checkDropPosition()
    game.current_block.setPos(game.current_block.Xpos, drop_y)
    game.handle_block_landing()
