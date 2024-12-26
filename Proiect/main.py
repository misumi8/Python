import sys
import pygame
import pygame.display

from mouse import Mouse
from game import Game

pygame.init()
screen_height = 768
screen_width = 1024
screen = pygame.display.set_mode((screen_width, screen_height))
game_state = "singleplayer"
clock = pygame.time.Clock()
frames = 60
cell_size = 74

menu_background_img = pygame.image.load("images/menu.png")
menu_background_img = pygame.transform.scale(menu_background_img, (screen_width, screen_height))

map_hexagon_img = pygame.image.load("images/hexagon.png")
map_hexagon_img = pygame.transform.scale(map_hexagon_img, (cell_size, cell_size))

map_hexagon_metal_img = pygame.image.load("images/hexagon_metal.png")
map_hexagon_metal_img = pygame.transform.scale(map_hexagon_metal_img, (cell_size, cell_size))

map_hexagon_hover_img = pygame.image.load("images/hexagon_hover.png")
map_hexagon_hover_img = pygame.transform.scale(map_hexagon_hover_img, (cell_size, cell_size))

singlep_button_font = pygame.font.Font("fonts/MouseMemoirs-Regular.ttf", 52)
multip_button_font = pygame.font.Font("fonts/MouseMemoirs-Regular.ttf", 58)
score_font = pygame.font.Font("fonts/Roboto-Black.ttf", 45)

def draw_button(screen, rect, text, button_color, font, text_color = (0, 0, 0)):
    pygame.draw.rect(screen, button_color, rect, border_radius=18)
    text_surf = font.render(text, True, text_color)
    text_rect = text_surf.get_rect(center=rect.center)
    screen.blit(text_surf, text_rect)

def draw_menu():
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

    return single_player_button_rect, multi_player_button_rect, quit_button_rect

def draw_singlep_game(game):
    screen.fill((175, 215, 70))

    text_surf = score_font.render("Score: " + str(game.score), True, (255, 255, 255))
    text_shadow = score_font.render("Score: " + str(game.score), True, (46, 46, 46))
    score_rect = pygame.Rect(0, 0, 1024, 100)
    text_rect = text_surf.get_rect(center=score_rect.center)
    screen.blit(text_shadow, text_rect.move(2,2))
    screen.blit(text_surf, text_rect)

    offset_x = 95
    offset_y = 90
    starting_y = offset_y
    hex_hovered = False
    for i in range(11):
        starting_x = offset_x if i % 2 == 0 else offset_x + (cell_size / 2)
        for k in range(11):
            screen.blit(map_hexagon_img, (starting_x, starting_y))
            if mouse.pos.y == i and mouse.pos.x == k:
                mouse.draw_mouse(starting_x, starting_y)
            elif game.game_board[i][k] == 2:
                screen.blit(map_hexagon_metal_img, (starting_x, starting_y))
            elif (starting_x < pygame.mouse.get_pos()[0] < starting_x + cell_size and
                  starting_y < pygame.mouse.get_pos()[1] < starting_y + cell_size and
                  not hex_hovered):
                screen.blit(map_hexagon_hover_img, (starting_x, starting_y))
                hex_hovered = True
            starting_x += cell_size
        starting_y += int(cell_size * 0.75)

def raise_metal_wall(game):
    offset_x = 95
    offset_y = 90
    starting_y = offset_y
    for i in range(11):
        starting_x = offset_x if i % 2 == 0 else offset_x + (cell_size / 2)
        for k in range(11):
            if (starting_x < pygame.mouse.get_pos()[0] < starting_x + cell_size and
                    starting_y < pygame.mouse.get_pos()[1] < starting_y + cell_size and
                    game.game_board[i][k] == 0):
                game.game_board[i][k] = 2
                game.score -= 50
                return
            starting_x += cell_size
        starting_y += int(cell_size * 0.75)

def draw_multip_game():
    print()

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
            if game_state == "menu":
                if single_player_button_rect.collidepoint(pygame.mouse.get_pos()):
                    print("Single player button clicked")
                    game_state = "singleplayer"
                elif multi_player_button_rect.collidepoint(pygame.mouse.get_pos()):
                    print("Multi player button clicked")
                    game_state = "multiplayer"
                elif quit_button_rect.collidepoint(pygame.mouse.get_pos()):
                    print("Quit game button clicked")
                    pygame.quit()
                    sys.exit()
            elif game_state == "singleplayer":
                raise_metal_wall(game,)
            elif game_state == "multiplayer":
                print()

    if game_state == "menu":
        single_player_button_rect, multi_player_button_rect, quit_button_rect = draw_menu()
    elif game_state == "singleplayer":
        draw_singlep_game(game)
    elif game_state == "multiplayer":
        draw_multip_game()

    # mouse.draw_mouse()
    pygame.display.update()
    clock.tick(frames)




