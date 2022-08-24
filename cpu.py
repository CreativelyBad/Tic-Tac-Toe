import random

class cpu_player:

    def choose_box(game_board):
        board = game_board
        invalid_move = True
        while invalid_move:
            random_num = random.randint(0, 8)
            if board[random_num] != 'x' and board[random_num] != 'o':
                invalid_move = False
        return str(random_num + 1)