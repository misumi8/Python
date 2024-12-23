import pygame
from position import Position

class Mouse:
    def __init__(self, screen, cell_size):
        self.cell_size = cell_size
        self.screen = screen
        self.pos = Position(5, 5)

    def draw_mouse(self):
        mouse_rect = pygame.Rect(self.pos.x * self.cell_size, self.pos.y * self.cell_size, self.cell_size, self.cell_size)
        pygame.draw.rect(self.screen, (200, 50, 20), mouse_rect)

