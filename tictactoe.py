def print_table():
    lookup = ['-', 'X', 'O']
    for row in T:
        print ' '.join([lookup[cell] for cell in row])
    print


def move(player, row, column):
    global next_player

    row -= 1
    column -= 1

    assert player == next_player, 'player not valid'
    assert row in range(table_size), 'row out of range'
    assert column in range(table_size), 'column out of range'
    assert T[row][column] == 0, 'illegal move'

    T[row][column] = player   # writing to global variable, why is not a problem,

    lookup_next_player = [0, 2, 1]

    '''
        dict----
        
        lookup_next_player = {
        1: 2,
        2: 1
        }
    '''    
    next_player = lookup_next_player[next_player]

    print_table()




def is_winner_cell(row, column):
    for row in range(table_size):
        for column in range(table_size):
            possible_winner = check_winner_horizontal_start(row, column)
            if possible_winner:
                return possible_winner

            possible_winner = check_winner_vertical_start(row, column)
            if possible_winner:
                return possible_winner





    # | vertical
    # \ diagonal
    # / diagonal
    # no space left -> even
    pass




def check_winner_horizontal_start(row, column):
    winner = T[row][column]
    if column + winning_size > table_size:
        return 0

    for i in range(1, winning_size):
        if T[row][column + i] != winner:
            return 0

    return winner


def check_winner_vertical_start(row, column):
    winner = T[row][column]
    if row + winning_size > table_size:
        return 0

    for i in range(1, winning_size):
        if T[row + i][column] != winner:
            return 0

    return winner


def check_winner_diag_se_start(row, column):
    winner = T[row][column]
    if row + winning_size > table_size or \
            column + winning_size > table_size:
        return 0

    for i in range(1, winning_size):
        if T[row + i][column + i] != winner:
            return 0

    return winner



def check_winner_diag_sw_start(row, column):
    winner = T[row][column]
    if row + winning_size > table_size or \
            column - winning_size < 0:
        return 0

    for i in range(1, winning_size):
        if T[row + i][column - i] != winner:
            return 0

    return winner




table_size = 7
winning_size = 5

T = [[0] * table_size for _ in range(table_size)]
next_player = 1

move(1, 3, 3)
move(2, 1, 1)
move(1, 3, 4)
move(2, 2, 3)




