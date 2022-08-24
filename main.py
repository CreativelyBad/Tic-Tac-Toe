from board import game_board as b

playing = True
round_in_progress = False
while playing:
    user_input = input('Would you like to start a new round (y/n): ')
    if user_input == 'n':
        playing = False
        exit
    elif user_input == 'y':         
        b.reset_board()
        round_in_progress = True
        while round_in_progress:
            print('')
            b.print_board()
            user_input = input('Choose a box: ')
            b.new_move(user_input)
            round_in_progress = not b.move_result()

        b.print_board()
        b.print_message()
        print('')
    else:
        print('------Invalid answer------')