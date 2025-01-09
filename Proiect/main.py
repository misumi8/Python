import sys
from pprint import pprint
from random import random
import pygame
import pygame.display
from mouse import Mouse
from game import Game

# Init and set up display
pygame.init()
pygame.display.set_caption("Trap the Mouse")
screen_height = 768
screen_width = 1024
screen = pygame.display.set_mode((screen_width, screen_height))

# Game initial settings/states
game_state = "menu"
clock = pygame.time.Clock()
frames = 60
cell_size = 74
is_mouse_turn = False
player_win_state = 0
multiplayer_win_state = 0
singlep_randomness = -1

# Images
step_back_img = pygame.image.load("images/step_back.png")
step_back_img = pygame.transform.scale(step_back_img, (50, 50))
step_back_hover_img = pygame.image.load("images/step_back_hover.png")
step_back_hover_img = pygame.transform.scale(step_back_hover_img, (50, 50))
step_back_button_rect = step_back_img.get_rect()
step_back_button_rect.center = (screen_width * 0.96, screen_height * 0.05)

menu_background_img = pygame.image.load("images/menu.png")
menu_background_img = pygame.transform.scale(menu_background_img, (screen_width, screen_height))

background_img = pygame.image.load("images/background.png")
background_img = pygame.transform.scale(background_img, (screen_width, screen_height))

map_hexagon_img = pygame.image.load("images/hexagon.png")
map_hexagon_img = pygame.transform.scale(map_hexagon_img, (cell_size, cell_size))

map_hexagon_metal_img = pygame.image.load("images/hexagon_metal.png")
map_hexagon_metal_img = pygame.transform.scale(map_hexagon_metal_img, (cell_size, cell_size))

map_hexagon_hover_img = pygame.image.load("images/hexagon_hover.png")
map_hexagon_hover_img = pygame.transform.scale(map_hexagon_hover_img, (cell_size, cell_size))

# Fonts
singlep_button_font = pygame.font.Font("fonts/MouseMemoirs-Regular.ttf", 52)
multip_button_font = pygame.font.Font("fonts/MouseMemoirs-Regular.ttf", 58)
score_font = pygame.font.Font("fonts/Roboto-Black.ttf", 45)
player_alert_font = pygame.font.Font("fonts/Roboto-Black.ttf", 80)
difficulty_selection_title_font = pygame.font.Font("fonts/Roboto-Black.ttf", 55)
difficulty_selection_font = pygame.font.Font("fonts/MouseMemoirs-Regular.ttf", 45)

def draw_button(screen, rect, text, button_color, font, text_color = (0, 0, 0)):
    """
    Draws a button with shadow and text in center.

    Args:
        screen (pygame.Surface): The screen to draw on
        rect (pygame.Rect): The rectangle defining the button
        text (str): Button central text
        button_color (tuple): RGB color
        font (pygame.font.Font): Button text font
        text_color (tuple): RGB text color. Defaults to black
    """
    shadow_rect = rect.copy()
    shadow_rect.x += 3
    shadow_rect.y += 3
    pygame.draw.rect(screen, (126, 156, 53), shadow_rect, border_radius=18)
    pygame.draw.rect(screen, button_color, rect, border_radius=18)

    text_surf = font.render(text, True, text_color)
    text_rect = text_surf.get_rect(center=rect.center)
    screen.blit(text_surf, text_rect)

def draw_menu():
    """
    Draws the main menu with single player, multiplayer and quit buttons.

    :return: A tuple of three rectangles for single player, multiplayer and quit buttons
    """
    # screen.fill((175, 215, 70))
    screen.blit(background_img, (0, 0))
    screen.blit(menu_background_img, (0, 0))

    # Singleplayer button
    single_player_button_rect = pygame.Rect(0, 0, 250, 75)
    single_player_button_rect.center = (screen_width * 0.46, screen_height * 0.65)
    if single_player_button_rect.collidepoint(pygame.mouse.get_pos()):
        draw_button(screen, single_player_button_rect, "Single Player", (110, 0, 0), singlep_button_font, (149, 184, 62))
    else:
        draw_button(screen, single_player_button_rect, "Single Player", (125, 0, 0), singlep_button_font, (149, 184, 62))

    # Multiplayer button
    multi_player_button_rect = pygame.Rect(0, 0, 75, 75)
    multi_player_button_rect.center = (screen_width * 0.63, screen_height * 0.65)
    if multi_player_button_rect.collidepoint(pygame.mouse.get_pos()):
        draw_button(screen, multi_player_button_rect, "2P", (110, 0, 0), multip_button_font, (149, 184, 62))
    else:
        draw_button(screen, multi_player_button_rect, "2P", (125, 0, 0), multip_button_font, (149, 184, 62))

    # Quit button
    quit_button_rect = pygame.Rect(0, 0, 339, 71)
    quit_button_rect.center = (screen_width * 0.502, screen_height * 0.76)
    if quit_button_rect.collidepoint(pygame.mouse.get_pos()):
        draw_button(screen, quit_button_rect, "Quit Game", (110, 0, 0), singlep_button_font, (149, 184, 62))
    else:
        draw_button(screen, quit_button_rect, "Quit Game", (125, 0, 0), singlep_button_font, (149, 184, 62))

    return single_player_button_rect, multi_player_button_rect, quit_button_rect

def draw_difficulty_level_selection(game):
    """
    Draws the difficulty level selection box and 3 difficulty buttons (easy, medium, hard).

    :param game: The game object
    :return: A tuple of three difficulty button rectangles
    """
    # screen.fill((175, 215, 70))
    screen.blit(background_img, (0, 0))
    text_difficulty = difficulty_selection_title_font.render("DIFFICULTY", True, (245, 245, 245))
    shadow_text_difficulty = difficulty_selection_title_font.render("DIFFICULTY", True, (4, 0, 54))


    difficulty_box_rect = pygame.Rect(0, 0, 395, 400)
    difficulty_box_rect.center = (screen_width * 0.5, screen_height * 0.48)
    text_rect = text_difficulty.get_rect(center=(difficulty_box_rect.center[0], difficulty_box_rect.midtop[1] + 80))
    # pygame.draw.rect(screen, (255,0,0), difficulty_box_rect)
    selection_box_background = pygame.image.load("images/selection_box_background.png")
    selection_box_background = pygame.transform.scale(selection_box_background, (difficulty_box_rect.width, difficulty_box_rect.height))
    screen.blit(selection_box_background, difficulty_box_rect.topleft)
    screen.blit(shadow_text_difficulty, text_rect.move(1,4))
    screen.blit(text_difficulty, text_rect)

    easy_rect = pygame.Rect(0, 0, 200, 62)
    easy_rect.center = (screen_width * 0.5, screen_height * 0.44)
    if easy_rect.collidepoint(pygame.mouse.get_pos()):
        draw_button(screen, easy_rect, "Easy", (25, 145, 69), difficulty_selection_font, (245, 245, 245))
    else:
        draw_button(screen, easy_rect, "Easy", (27, 161, 76), difficulty_selection_font, (245, 245, 245))

    medium_rect = pygame.Rect(0, 0, 200, 62)
    medium_rect.center = (screen_width * 0.5, screen_height * 0.53)
    if medium_rect.collidepoint(pygame.mouse.get_pos()):
        draw_button(screen, medium_rect, "Medium", (179, 83, 0), difficulty_selection_font, (245, 245, 245))
    else:
        draw_button(screen, medium_rect, "Medium", (199, 93, 0), difficulty_selection_font, (245, 245, 245))

    hard_rect = pygame.Rect(0, 0, 200, 62)
    hard_rect.center = (screen_width * 0.5, screen_height * 0.62)
    if hard_rect.collidepoint(pygame.mouse.get_pos()):
        draw_button(screen, hard_rect, "Hard", (143, 0, 0), difficulty_selection_font, (245, 245, 245))
    else:
        draw_button(screen, hard_rect, "Hard", (158, 0, 0), difficulty_selection_font, (245, 245, 245))

    return easy_rect, medium_rect, hard_rect

def draw_game(game):
    """
    Draws the game map with the mouse and simple/occupied hexagons

    :param game: The game object
    """
    # screen.fill((175, 215, 70))
    screen.blit(background_img, (0, 0))
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
            if mouse.pos.y == k and mouse.pos.x == i:
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

def draw_player_alert(font, text, color):
    """
    Draws a text alert in the center of the screen. Called after the game achieved a final state.

    :param font: Text font
    :param text: Text string
    :param color: Text color
    """
    win_alert = pygame.Rect(0, 0, 250, 75)
    win_alert.center = (screen_width * 0.5, screen_height * 0.47)
    text_surf = font.render(text, True, color)
    text_shadow = font.render(text, True, (35, 35, 35))
    text_rect = text_surf.get_rect(center=win_alert.center)
    screen.blit(text_shadow, text_rect.move(2, 2))
    screen.blit(text_surf, text_rect)

mouse = Mouse(screen, cell_size)

game = Game(mouse)

# Game loop
while True:
    # Events handling
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
                if singlep_randomness == -1:
                    if easy_rect.collidepoint(pygame.mouse.get_pos()):
                        singlep_randomness = 0.35
                    elif medium_rect.collidepoint(pygame.mouse.get_pos()):
                        singlep_randomness = 0.15
                    elif hard_rect.collidepoint(pygame.mouse.get_pos()):
                        singlep_randomness = 0
                    elif step_back_button_rect.collidepoint(pygame.mouse.get_pos()):
                        game_state = "menu"
                        mouse = Mouse(screen, cell_size)
                        game = Game(mouse)
                elif player_win_state == 0 and game.raise_metal_wall(cell_size):
                    path = game.find_shortest_path(singlep_randomness)
                    print(path)
                    pprint(game.game_board)
                    if path:
                        print(game.move_mouse(path[0], path[1]))
                    if game.is_mouse_on_border(game.mouse.pos.x, game.mouse.pos.y):
                        player_win_state = 2
                    elif game.is_mouse_caught():
                        player_win_state = 1
                    pprint(game.game_board)
                    print("--------------------------------------------------------")
                elif step_back_button_rect.collidepoint(pygame.mouse.get_pos()):
                    game_state = "menu"
                    mouse = Mouse(screen, cell_size)
                    game = Game(mouse)
                    singlep_randomness = -1
                    player_win_state = 0
            elif game_state == "multiplayer":
                if step_back_button_rect.collidepoint(pygame.mouse.get_pos()):
                    game_state = "menu"
                    mouse = Mouse(screen, cell_size)
                    game = Game(mouse)
                    multiplayer_win_state = 0
                    is_mouse_turn = False
                if not is_mouse_turn:
                    if multiplayer_win_state == 0 and game.raise_metal_wall(cell_size):
                        pprint(game.game_board)
                        is_mouse_turn = True
                        if game.is_mouse_on_border(game.mouse.pos.x, game.mouse.pos.y):
                            multiplayer_win_state = 2
                        elif game.is_mouse_caught():
                            multiplayer_win_state = 1
                else:
                    if game.player_move_mouse(cell_size):
                        pprint(game.game_board)
                        is_mouse_turn = False
                        if game.is_mouse_on_border(game.mouse.pos.x, game.mouse.pos.y):
                            multiplayer_win_state = 2
                        elif game.is_mouse_caught():
                            multiplayer_win_state = 1

    if game_state == "menu":
        single_player_button_rect, multi_player_button_rect, quit_button_rect = draw_menu()
    elif game_state == "singleplayer":
        if singlep_randomness == -1:
            easy_rect, medium_rect, hard_rect = draw_difficulty_level_selection(game)
            if step_back_button_rect.collidepoint(pygame.mouse.get_pos()):
                screen.blit(step_back_hover_img, step_back_button_rect)
            else:
                screen.blit(step_back_img, step_back_button_rect)
        else:
            draw_game(game)
            if step_back_button_rect.collidepoint(pygame.mouse.get_pos()):
                screen.blit(step_back_hover_img, step_back_button_rect)
            else:
                screen.blit(step_back_img, step_back_button_rect)

            if player_win_state == 1:
                draw_player_alert(player_alert_font, "YOU WIN", (49, 204, 18))
            elif player_win_state == 2:
                draw_player_alert(player_alert_font, "YOU LOSE", (173, 9, 38))
    elif game_state == "multiplayer":
        draw_game(game)
        if multiplayer_win_state == 1:
            draw_player_alert(player_alert_font, "PLAYER WINS", (49, 204, 18))
        elif multiplayer_win_state == 2:
            draw_player_alert(player_alert_font, "MOUSE WINS", (173, 9, 38))

        if step_back_button_rect.collidepoint(pygame.mouse.get_pos()):
            screen.blit(step_back_hover_img, step_back_button_rect)
        else:
            screen.blit(step_back_img, step_back_button_rect)
    # Update display
    pygame.display.update()
    # Limit of frames per second
    clock.tick(frames)




