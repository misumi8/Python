import pygame
from position import Position

class Mouse:
    """
    Represents the mouse character in the game.
    """
    def __init__(self, screen, cell_size):
        """
        Initialize the mouse character.

        :param screen: The surface on which the mouse will be drawn
        :param cell_size: The size of the cell on the map
        """
        self.cell_size = cell_size
        self.screen = screen
        self.pos = Position(5, 5)
        self.mouse_img = pygame.image.load("images/mouse.png")
        self.mouse_img = pygame.transform.scale(self.mouse_img, (cell_size, cell_size))

    def draw_mouse(self, x, y):
        """
        Draws the mouse character on the screen.

        :param x: X coordinate of the mouse on the mao
        :param y: Y coordinate of the mouse on the map
        """
        self.screen.blit(self.mouse_img, (x - 5, y))
