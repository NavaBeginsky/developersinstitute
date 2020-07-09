board_positions = [
    [(1, 1), {'taken_by': ' '}],
    [(1, 2), {'taken_by': ' '}],
    [(1, 3), {'taken_by': ' '}],
    [(2, 1), {'taken_by': ' '}],
    [(2, 2), {'taken_by': ' '}],
    [(2, 3), {'taken_by': ' '}],
    [(3, 1), {'taken_by': ' '}],
    [(3, 2), {'taken_by': ' '}],
    [(3, 3), {'taken_by': ' '}]
]

def display_board():
    print(f'''
    TIC TAC TOE
    ************************
    *  {board_positions[0][1]['taken_by']}    |  {board_positions[1][1]['taken_by']}    | {board_positions[2][1]['taken_by']}    *
    * _____ | _____ | ____ *
    *       |       |      *
    * {board_positions[3][1]['taken_by']}     | {board_positions[4][1]['taken_by']}     | {board_positions[5][1]['taken_by']}    *
    * _____ | _____ | ____ *
    * {board_positions[6][1]['taken_by']}     |  {board_positions[7][1]['taken_by']}    | {board_positions[8][1]['taken_by']}    *
    *       |       |      *
    ************************
    ''')
def player_input(current_player):
    ''' get current player's list, ask them to choose a position, if the position is free add it to their list and add it to the 
     variable that will display on the board. If they choose a position that doesn't exist it will tell them and ask for position again'''
    print(f'It is {current_player}\'s turn')
    while True:
        row = input('choose row')
        column = input('choose column')
        chosen_position = (int(row), int(column))
        for position in board_positions:
            if position[0] == chosen_position:
                if position[1]['taken_by'] == ' ':
                    position[1]['taken_by'] = current_player
                    return
        print('Please choose a valid position')


def check_win(current_player):
    players_positions = [position[0] for position in board_positions if position[1]['taken_by'] == current_player]
    players_rows = [position[0][0] for position in board_positions if position[1]['taken_by'] == current_player]
    players_columns = [position[0][1] for position in board_positions if position[1]['taken_by'] == current_player]
    num = 1
    while num < 4: #if they have 3 of the same number in their rows or their columns it means they win
        if players_rows.count(num) == 3:
            print('here')
            return True
        elif players_columns.count(num) == 3:
            print('here1')
            return True
        num += 1
    winning_combos = [[(1, 1), (2, 2), (3, 3)], [(1, 3), (2, 2), (3, 1)]]
    if winning_combos[0][0] in players_positions and winning_combos[0][1] in players_positions and winning_combos[0][2] in players_positions or winning_combos[1][0] in players_positions and winning_combos[1][1] in players_positions and winning_combos[1][2] in players_positions:
        print('here2')
        return True
    else :
        return False

def check_if_draw():
    available_positions = []
    for position in board_positions:
        if position[1]['taken_by'] == ' ':
            available_positions.append(position)
    if available_positions == []:
        print('It\'s a draw!')
        return True
    else :
        return False

  
def play(current_player):
    current_player = current_player
    display_board()
    player_input(current_player)
    win = check_win(current_player)
    if win == True:
        print(f'{current_player} wins!')
    else:
        # draw = check_if_draw()
        if check_if_draw():
            return
        current_player = 'o' if current_player == 'x' else 'x'
        play(current_player)

play('x')