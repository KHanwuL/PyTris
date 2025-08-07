import numpy as np

TETROMINOS = {
  'I': np.array([[2, 2, 2, 2]]),

  'O': np.array([[3, 3],
                [3, 3]]),
  'T': np.array([[0, 4, 0],
                [4, 4, 4]]),
  'S': np.array([[0, 5, 5],
                [5, 5, 0]]),
  'Z': np.array([[6, 6, 0],
                [0, 6, 6]]),
  'J': np.array([[7, 0, 0],
                [7, 7, 7]]),
  'L': np.array([[0, 0, 8],
                [8, 8, 8]])
}

class Block:
  def __init__(self, Xpos, Ypos, shape_name, board, rotate=0):
    self.Xpos = Xpos
    self.Ypos = Ypos
    self.shape_name = shape_name
    self.shape = TETROMINOS[shape_name].copy()
    self.board = board
    for _ in range(rotate % 4):
      self.rotateShapeLeft()

  def setPos(self, x, y):
    self.Xpos = x
    self.Ypos = y

  def createShape(self, shape_name):
    self.shape_name = shape_name
    self.shape = TETROMINOS[shape_name].copy()

  def rotateShapeLeft(self):
    original_shape = self.shape.copy()
    self.shape = np.rot90(self.shape, 1)
    if self.isCollisionAt(self.Xpos, self.Ypos):
      self.shape = original_shape

  def rotateShapeRight(self):
    original_shape = self.shape.copy()
    self.shape = np.rot90(self.shape, -1)
    if self.isCollisionAt(self.Xpos, self.Ypos):
      self.shape = original_shape

  def moveBlock(self, move_x, move_y):
    if (self.isMoveable(move_x, move_y)):
      self.Xpos += move_x
      self.Ypos += move_y

  def isCollisionAt(self, x, y) -> bool:
    for dy in range(self.shape.shape[0]):
      for dx in range(self.shape.shape[1]):
        if self.shape[dy, dx] != 0:
          bx = x + dx
          by = y + dy
          if by < 0 or by >= self.board.Board.shape[0] or bx < 0 or bx >= self.board.Board.shape[1]:
            return True
          if self.board.Board[by, bx] >= 1:
            return True
    return False

  def isMoveable(self, move_x, move_y) -> bool:
    return not self.isCollisionAt(self.Xpos + move_x, self.Ypos + move_y)
  
  def isFallable(self) -> bool:
    return not self.isCollisionAt(self.Xpos, self.Ypos + 1)
  
  def checkDropPosition(self) -> int:
    y = self.Ypos
    while not self.isCollisionAt(self.Xpos, y + 1):
      y += 1
    return y