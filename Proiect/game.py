from pprint import pprint


class Game:
    def __init__(self, mouse):
        self.mouse = mouse
        self.game_board = [[0 for i in range(11)] for k in range(11)]
        self.game_board[int(self.mouse.pos.x)][int(self.mouse.pos.y)] = 1

    # def draw_board(self):
    #     # awd

    def move_mouse(self, new_x, new_y):
        if not self.validate_move(new_x, new_y):
            return False
        self.mouse.pos.x = new_x
        self.mouse.pos.y = new_y

    def validate_move(self, x, y):
        current_x = self.mouse.pos.x
        current_y = self.mouse.pos.y
        valid_moves = {(current_x, current_y - 1),
                       (current_x, current_y + 1),
                       (current_x - 1, current_y),
                       (current_x - 1, current_y + 1),
                       (current_x + 1, current_y),
                       (current_x + 1, current_y + 1)}
        return (x, y) in valid_moves