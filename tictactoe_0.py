def print_table():
    lookup = ['-', 'X', 'O']
    for row in T:
        print ' '.join([lookup[cell] for cell in row])
    print


def move(player, row, column):
    row -= 1
    column -= 1

    assert player == next_player, 'player not valid'
    assert row in range(table_size), 'row out of range'
    assert column in range(table_size), 'column out of range'
    assert T[row][column] == 0, 'illegal move'

    T[row][column] = player   # writing to global variable, why is not a problem,

    global next_player
    if next_player == 1:  # why problem here
        next_player = 2
    else:
        next_player = 1

    print_table()


def is_winner():
    # - horizontal
    # | vertical
    # \ diagonal
    # / diagonal
    # no space left -> even
    return
    


def is_winner_horizontal(row, column):
	assert column <= table_size - 5






table_size = 7

T = [[0] * table_size for _ in range(table_size)]
next_player = 1

move(1, 3, 3)
move(2, 1, 1)
move(1, 3, 4)
move(2, 2, 3)
