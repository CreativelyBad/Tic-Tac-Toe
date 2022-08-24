from cpu import cpu_player as c

board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
out_message = 'message'
score = [0, 0, 0]

class game_board:

    def print_message():
        print(out_message)
        print('')
        print('Wins: ' + str(score[0]))
        print('Loses: ' + str(score[1]))
        print('Ties: ' + str(score[2]))

    def get_board():
        return board

    def reset_board():
            board.clear()
            for i in range(9):
                board.append(str(i+1))

    def print_board():
        for i in range(0, 9, 3):
            print('   |   |   ')
            print(' ' + board[i] + ' | ' + board[i+1] + ' | ' + board[i+2] + ' ')
            print('   |   |   ')
            if i < 6:
                print('-----------')

    def new_move(box):
        if box.isnumeric():
            if int(box) > 0 and int(box) < 10:
                if board[int(box) - 1] != 'x' and board[int(box) - 1] != 'o':
                    board.remove(box)
                    board.insert(int(box) - 1, 'x')
                    if not game_board.check_tie():
                        cpu_move = c.choose_box(board)
                        board.remove(cpu_move)
                        board.insert(int(cpu_move) - 1, 'o')
                else:
                    print("Box is taken")
            else:
                print('Please enter a valid number')
        else:
            print('Please enter a valid number')

    def move_result():
        game_over = False
        global out_message

        if game_board.check_tie():
            score[2] += 1
            out_message = 'Tie'
            game_over = True

        # check if row is the same
        if board[0] == 'x' and board[1] == 'x' and board[2] == 'x' or board[3] == 'x' and board[4] == 'x' and board[5] == 'x' or board[6] == 'x' and board[7] == 'x' and board[8] == 'x':
            out_message = 'You Won!'
            game_over = True
            score[0] += 1
        elif board[0] == 'o' and board[1] == 'o' and board[2] == 'o' or board[3] == 'o' and board[4] == 'o' and board[5] == 'o' or board[6] == 'o' and board[7] == 'o' and board[8] == 'o':
            out_message = 'You Lost :('
            game_over = True
            score[1] += 1

        # check if column is the same
        if board[0] == 'x' and board[3] == 'x' and board[6] == 'x' or board[1] == 'x' and board[4] == 'x' and board[7] == 'x' or board[2] == 'x' and board[5] == 'x' and board[8] == 'x':
            out_message = 'You Won!'
            game_over = True
            score[0] += 1
        elif board[0] == 'o' and board[3] == 'o' and board[6] == 'o' or board[1] == 'o' and board[4] == 'o' and board[7] == 'o' or board[2] == 'o' and board[5] == 'o' and board[8] == 'o':
            out_message = 'You Lost :('
            game_over = True
            score[1] += 1
        
        # check if diagnol is the same
        if board[0] == 'x' and board[4] == 'x' and board[8] == 'x' or board[2] == 'x' and board[4] == 'x' and board[6] == 'x':
            out_message = 'You Won!'
            game_over = True
            score[0] += 1
        elif board[0] == 'o' and board[4] == 'o' and board[8] == 'o' or board[2] == 'o' and board[4] == 'o' and board[6] == 'o':
            out_message = 'You Lost :('
            game_over = True
            score[1] += 1

        return game_over

    def check_tie():
        full_boxes = 0
        for i in range(9):
            if board[i] == 'x' or board[i] == 'o':
                full_boxes += 1
        if full_boxes == 9:
            return True