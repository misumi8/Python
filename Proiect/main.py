import sys
import pygame
import pygame.display

from mouse import Mouse
from game import Game

pygame.init()
screen_height = 768
screen_width = 1024
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
frames = 60
cell_size = 50

menu_background_img = pygame.image.load("images/menu.png")
menu_background_img = pygame.transform.scale(menu_background_img, (screen_width, screen_height))

singlep_button_font = pygame.font.Font("fonts/MouseMemoirs-Regular.ttf", 52)
multip_button_font = pygame.font.Font("fonts/MouseMemoirs-Regular.ttf", 58)

def draw_button(screen, rect, text, button_color, font, text_color = (0, 0, 0)):
    pygame.draw.rect(screen, button_color, rect, border_radius=18)
    text_surf = font.render(text, True, text_color)
    text_rect = text_surf.get_rect(center=rect.center)
    screen.blit(text_surf, text_rect)

# Mouse
mouse = Mouse(screen, cell_size)

# Game & Game board
game = Game(mouse)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            print("MOUSEBUTTONUP", event.pos)
            if single_player_button_rect.collidepoint(pygame.mouse.get_pos()):
                print("Single player button clicked")
            elif multi_player_button_rect.collidepoint(pygame.mouse.get_pos()):
                print("Multi player button clicked")
            elif quit_button_rect.collidepoint(pygame.mouse.get_pos()):
                print("Quit game button clicked")
                pygame.quit()
                sys.exit()
    screen.fill((175, 215, 70))
    screen.blit(menu_background_img, (0, 0))

    # Singleplayer button
    single_player_button_rect = pygame.Rect(0, 0, 250, 75)
    single_player_button_rect.center = (screen_width * 0.46, screen_height * 0.65)
    if single_player_button_rect.collidepoint(pygame.mouse.get_pos()):
        draw_button(screen, single_player_button_rect, "Single Player", (110, 0, 0), singlep_button_font, (10, 10, 10))
    else:
        draw_button(screen, single_player_button_rect, "Single Player", (125, 0, 0), singlep_button_font)

    # Multiplayer button
    multi_player_button_rect = pygame.Rect(0, 0, 75, 75)
    multi_player_button_rect.center = (screen_width * 0.63, screen_height * 0.65)
    if multi_player_button_rect.collidepoint(pygame.mouse.get_pos()):
        draw_button(screen, multi_player_button_rect, "2P", (110, 0, 0), multip_button_font, (10, 10, 10))
    else:
        draw_button(screen, multi_player_button_rect, "2P", (125, 0, 0), multip_button_font)

    # Quit button
    quit_button_rect = pygame.Rect(0, 0, 339, 71)
    quit_button_rect.center = (screen_width * 0.502, screen_height * 0.76)
    if quit_button_rect.collidepoint(pygame.mouse.get_pos()):
        draw_button(screen, quit_button_rect, "Quit Game", (110, 0, 0), singlep_button_font, (10, 10, 10))
    else:
        draw_button(screen, quit_button_rect, "Quit Game", (125, 0, 0), singlep_button_font)

    # mouse.draw_mouse()
    pygame.display.update()
    clock.tick(frames)




