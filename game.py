import pygame

from scripts.devfw.elems import Singleton

from scripts.devfw.window import Window
from scripts.devfw.inp    import Input
from scripts.devfw.render import Render, DEFAULT

class Game(Singleton):
  def __init__(self):
    super().__init__()
    self.APP_WIDTH  : int = 500
    self.APP_HEIGHT : int = 800

  def load(self) -> None:
    app_name = 'Game'
    Window(self.APP_WIDTH, self.APP_HEIGHT, app_name)
    Input(app_name)
    Render()

  def update(self) -> None:
    self.elements['Window'].update()
    self.elements['Input'].update()

  def run(self) -> None:
    self.load()
    self.running : bool = True
    while self.running:
      self.update()
    pygame.quit()

Game().run()