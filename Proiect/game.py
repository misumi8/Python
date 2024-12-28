import random
from collections import deque
from pprint import pprint

import pygame

class Game:
    def __init__(self, mouse):
        self.mouse = mouse
        self.game_board = [[0 for i in range(11)] for k in range(11)]
        metal_walls = random.randint(6, 8)
        for i in range(metal_walls):
            x = random.randint(0, 10)
            y = random.randint(0, 10)
            while x == 5:
                x = random.randint(0, 10)
            while y == 5:
                y = random.randint(0, 10)
            self.game_board[x][y] = 2
        self.game_board[int(self.mouse.pos.x)][int(self.mouse.pos.y)] = 1
        self.score = 20000

    def get_random_mouse_move(self, mouse_x, mouse_y):
        return random.choice([(mouse_x + x, mouse_y + y) for x, y in self.get_valid_moves(mouse_x) if
                              self.game_board[mouse_x + x][mouse_y + y] == 0])

    def find_shortest_path(self, randomness):
        start_pos_x = self.mouse.pos.x
        start_pos_y = self.mouse.pos.y
        queue = deque([(start_pos_x, start_pos_y, [])])
        visited = set()
        visited.add((start_pos_x, start_pos_y))
        while True:
            if not queue:
                if not self.is_mouse_caught():
                    return self.get_random_mouse_move(start_pos_x, start_pos_y)
                else:
                    return False
            x, y, path = queue.popleft()
            if self.is_mouse_on_border(x, y):
                randomne = random.random()
                print("****************************************", randomne, randomness)
                if randomne < randomness:
                    return self.get_random_mouse_move(start_pos_x, start_pos_y)
                else:
                    if len(path) > 1:
                        return path[1][0], path[1][1]
                    else:
                        return x, y
            elif x == 0 or x == len(self.game_board) - 1 or y == 0 or y == len(self.game_board[0]) - 1:
                if len(path) > 1:
                    return path[1][0], path[1][1]
                else:
                    return x, y

            for direction in self.get_valid_moves(x):
                next_x = x + direction[0]
                next_y = y + direction[1]
                if (0 <= next_x < len(self.game_board) and
                        0 <= next_y < len(self.game_board[0]) and
                        self.game_board[next_x][next_y] == 0 and
                        (next_x, next_y) not in visited):
                    visited.add((next_x, next_y))
                    queue.append((next_x, next_y, path + [(x, y)]))

    def is_mouse_on_border(self, x, y):
        return x == 0 or x == len(self.game_board) - 1 or y == 0 or y == len(self.game_board[0]) - 1

    def move_mouse(self, new_x, new_y):
        if new_x == self.mouse.pos.x and new_y == self.mouse.pos.y:
            return False
        if not self.validate_move(new_x, new_y):
            return False
        print(f"Mouse move: {new_x}, {new_y}")
        self.game_board[self.mouse.pos.x][self.mouse.pos.y] = 0
        self.game_board[new_x][new_y] = 1
        self.mouse.pos.x = new_x
        self.mouse.pos.y = new_y
        return True

    def player_move_mouse(self, cell_size):
        offset_x = 95
        offset_y = 90
        starting_y = offset_y
        for i in range(11):
            starting_x = offset_x if i % 2 == 0 else offset_x + (cell_size / 2)
            for k in range(11):
                if (starting_x < pygame.mouse.get_pos()[0] < starting_x + cell_size and
                        starting_y < pygame.mouse.get_pos()[1] < starting_y + cell_size):
                    if self.game_board[i][k] == 0:
                        if self.move_mouse(i, k):
                            return True
                        else:
                            return False
                    else:
                        return False
                starting_x += cell_size
            starting_y += int(cell_size * 0.75)
        return False

    def raise_metal_wall(self, cell_size):
        offset_x = 95
        offset_y = 90
        starting_y = offset_y
        for i in range(11):
            starting_x = offset_x if i % 2 == 0 else offset_x + (cell_size / 2)
            for k in range(11):
                if (starting_x < pygame.mouse.get_pos()[0] < starting_x + cell_size and
                        starting_y < pygame.mouse.get_pos()[1] < starting_y + cell_size):
                    if self.game_board[i][k] == 0:
                        self.game_board[i][k] = 2
                        self.score -= 50
                        print(f"Metal hexagon placed: x {i}, y {k}")
                        return True
                    else:
                        return False
                starting_x += cell_size
            starting_y += int(cell_size * 0.75)
        return False

    def validate_move(self, x, y):
        if not (0 <= x < len(self.game_board) and 0 <= y < len(self.game_board[0])):
            print(f"[Invalid move] X or/and Y are out of table | X = {x}, Y = {y}")
            return False
        if self.game_board[x][y] != 0:
            print(f"[Invalid move] This hexagon is not available | X = {x}, Y = {y} : {self.game_board[x][y]}")
            return False
        current_x = self.mouse.pos.x
        current_y = self.mouse.pos.y
        print(current_x, current_y)
        valid_moves = {(current_x + dx, current_y + dy) for dx, dy in self.get_valid_moves(current_x)}
        print(f"Valid moves for x = {current_x} and y = {current_y}:")
        print(valid_moves)
        if (x, y) in valid_moves:
            return True
        print(f"[Invalid move] incorrect position | X = {x}, Y = {y} : {self.game_board[x][y]}")
        return False

    def get_valid_moves(self, current_x):
        if current_x % 2 == 0:
            return [(-1, -1), (-1, 0), (0, -1), (0, 1), (1, -1), (1, 0)]
        else:
            return [(-1, 0), (-1, 1), (0, -1), (0, 1), (1, 0), (1, 1)]

    def is_mouse_caught(self):
        valid_moves = {(self.mouse.pos.x + dx, self.mouse.pos.y + dy) for dx, dy in self.get_valid_moves(self.mouse.pos.x)}
        return not any([self.game_board[x][y] == 0 for x,y in valid_moves])
