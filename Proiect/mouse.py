import pygame
from position import Position

class Mouse:
    def __init__(self, screen, cell_size):
        self.cell_size = cell_size
        self.screen = screen
        self.pos = Position(5, 5)
        self.mouse_img = pygame.image.load("images/mouse.png")
        self.mouse_img = pygame.transform.scale(self.mouse_img, (cell_size, cell_size))

    def draw_mouse(self, x, y):
        self.screen.blit(self.mouse_img, (x - 5, y))
