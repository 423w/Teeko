
from scripts import *
from turt import turt_time, turt_plop, write_win, write_text_keep
from sounds import jazz
import sys

# if there is a permission error, it is because you module is not downloaded correctly.
# We can't figure out how to fix it
# it works for some people it doesn't for some so if it doesn't,
# search for @sound and comment the function immediately after

#@sound
jazz()

###set up###
board = [["O", "O", "O", "O", "O"], ["O", "O", "O", "O", "O"],
         ["O", "O", "O", "O", "O"], ["O", "O", "O", "O", "O"],
         ["O", "O", "O", "O", "O"]]

inp = False
turt = False

##Trap until good answer##
while inp not in ['No', 'no']:
    inp = input('Would you like turtle to draw this game? (fr for file replay) ')
    ##Turn on turt/break loop##
    if inp in ['yes', 'Yes']:
        turt = True
        turt_time()
        write_text_keep(250, "Teeko!", size=30)
        write_text_keep(200, "By: your favorite group", size=20)
        break

    ##Replay##
    elif inp == 'fr':
        inp = input('name the valid game file or e for exit ')
        if inp != 'e':
            try:
                with open(inp, 'r') as FR:
                    turt_time()
                    for line in FR:
                        line = line.split(',')
                        color = line[0]
                        cord = line[-1].split('-')
                        x = int(cord[0])
                        y = int(cord[1])
                        # y human to list#
                        y += 4 - ((y - 1) * 2)

                        if len(line) == 2:
                            turt_plop(x, y, color, 3, False)

                        elif len(line) == 3:
                            ##move calculate##

                            if line[1] == 'v':
                                a = x
                                b = y + 1

                            elif line[1] == '^':
                                a = x
                                b = y - 1

                            elif line[1] == '<':
                                a = x - 1
                                b = y

                            elif line[1] == '>':
                                a = x + 1
                                b = y

                            elif line[1] == '^>':
                                a = x + 1
                                b = y - 1

                            elif line[1] == '<^':
                                a = x - 1
                                b = y - 1

                            elif line[1] == '<v':
                                a = x - 1
                                b = y + 1

                            elif line[1] == 'v>':
                                a = x + 1
                                b = y + 1

                            turt_plop(x, y, 'White', 3, False)
                            turt_plop(a, b, color, 3, False)

            except:
                print('Error with file')

            input('Press enter to end replay ')

        sys.exit()

move_arch = []

st = {"Black": 'b', "Red": 'r'}
evil_st = {"Black": 'r', "Red": 'b'}
lawful_st = {"r": 'Red', "b": 'Black'}
turn = 'Black'
i = 0

GO = True

bt = 0
rt = 0

###Drop Phase###
while i < 8:
    if not turt:
        for x in board:
            print(x)
    ###Get and check input###
    inp = input(f'Place a {turn} piece at x,y or f for forfeit and r for rules: ')
    if inp == 'f':
        print(f"{turn} lost")
        GO = False
        break

    if inp == 'r':
        print(
            "The Teeko board consists of twenty-five spaces arranged in a five-by-five grid. There are eight markers in a Teeko game, four black and four red. One player, Black plays the black markers, and the other, Red, plays the red. Black moves first and places one marker on any space on the board. Red then places a marker on any unoccupied space; black does the same; and so on until all eight markers are on the board. The object of the game is for either player to win by having all four of their markers in a straight line (vertical, horizontal, or diagonal) or on a square of four adjacent spaces. (Adjacency is horizontal, vertical, or diagonal, but does not wrap around the edges of the board.) If neither player has won after the drop (when all eight pieces are on the board), then they move their pieces one at a time, with Black playing first. A piece may be moved only to an adjacent or diagonal space.")
        continue

    try:
        x = int(inp.split(',')[0])
        y = int(inp.split(',')[1])
        ##from human y to list y##
        y += (4 - ((y - 1) * 2))
    except:
        print('invalid input')
        continue
    ###Check if going to empty/valid space###
    if ((not 1 <= x <= 5) or (not 1 <= y <= 5)):
        print('invalid input')
        continue

    if board[y - 1][x - 1] != 'O':
        print('Occupied space')
        continue

    # y list to human#
    move_arch += [f'{turn},{x}-{y + (4 - ((y - 1) * 2))}']

    ###Place and switch turn###
    #@sound
    place()
    if turn == "Black":
        bt += 1
        i += 1
        turn = 'Red'
        board[y - 1][x - 1] = 'b'
        if turt:
            turt_plop(x, y, 'Black')
    elif turn == "Red":
        rt += 1
        i += 1
        turn = 'Black'
        board[y - 1][x - 1] = 'r'
        if turt:
            turt_plop(x, y, 'Red')

    if (didMoveWin((x - 1, y - 1), evil_st[turn], board)):
        print(f"{lawful_st[evil_st[turn]]} won")
        GO = False
        break

###Change to move mode###
if GO:
    print('DROP COMPLETE')

while GO:
    if not turt:
        for x in board:
            print(x)
    ###Get and check input(target piece)###
    inp = input(f'Pick a {turn} piece location x,y to move it, f to forfeit, r for rules: ')

    if inp == 'f':
        print(f"{turn} lost")
        GO = False
        break

    if inp == 'r':
        print(
            "The Teeko board consists of twenty-five spaces arranged in a five-by-five grid. There are eight markers in a Teeko game, four black and four red. One player, Black plays the black markers, and the other, Red, plays the red. Black moves first and places one marker on any space on the board. Red then places a marker on any unoccupied space; black does the same; and so on until all eight markers are on the board. The object of the game is for either player to win by having all four of their markers in a straight line (vertical, horizontal, or diagonal) or on a square of four adjacent spaces. (Adjacency is horizontal, vertical, or diagonal, but does not wrap around the edges of the board.) If neither player has won after the drop (when all eight pieces are on the board), then they move their pieces one at a time, with Black playing first. A piece may be moved only to an adjacent or diagonal space.")
        continue

    try:
        x = int(inp.split(',')[0])
        y = int(inp.split(',')[1])
        ##from human y to list y##
        y += (4 - ((y - 1) * 2))

    except:
        print('invalid input')
        continue

    ###Check if you own spot###
    if ((not 1 <= x <= 5) or (not 1 <= x <= 5)):
        print('invalid input')
        continue

    if board[y - 1][x - 1] == 'O':
        print('Empty space')
        continue

    if board[y - 1][x - 1] != st[turn]:
        print('Not your piece')
        continue

    ##The block rule, check for boxed corners to force free##
    if (board[0][1], board[1][1], board[1][0]) == (st[turn], st[turn], st[turn]):
        if board[0][0] == evil_st[turn] and (y - 1, x - 1) not in [(0, 1), (1, 1), (1, 0)]:
            print('Boxing is cheap')
            continue

    elif (board[4][1], board[3][1], board[3][0]) == (st[turn], st[turn], st[turn]):
        if board[4][0] == evil_st[turn] and (y - 1, x - 1) not in [(4, 1), (3, 1), (3, 0)]:
            print('Boxing is cheap')
            continue

    elif (board[4][3], board[3][3], board[3][4]) == (st[turn], st[turn], st[turn]):
        if board[4][4] == evil_st[turn] and (y - 1, x - 1) not in [(4, 3), (3, 3), (3, 4)]:
            print('Boxing is cheap')
            continue

    elif (board[0][3], board[1][3], board[1][4]) == (st[turn], st[turn], st[turn]):
        if board[0][4] == evil_st[turn] and (y - 1, x - 1) not in [(0, 3), (1, 3), (1, 4)]:
            print('Boxing is cheap')
            continue

    ###Get and check input(direction) or go back###
    inp = input('pick <,>,^,v,^>,<^,<v,v> to move, b to go back: ')

    if inp == 'b':
        print('Going back')
        continue

    if inp == 'v':
        a = x
        b = y + 1

    elif inp == '^':
        a = x
        b = y - 1

    elif inp == '<':
        a = x - 1
        b = y

    elif inp == '>':
        a = x + 1
        b = y

    elif inp == '^>':
        a = x + 1
        b = y - 1

    elif inp == '<^':
        a = x - 1
        b = y - 1

    elif inp == '<v':
        a = x - 1
        b = y + 1

    elif inp == 'v>':
        a = x + 1
        b = y + 1

    else:
        print('invalid input, going back')
        continue

    ###Check if new spot empty###
    if ((not 1 <= a <= 5) or (not 1 <= b <= 5)):
        print('Out of bounds, going back')
        continue

    if board[b - 1][a - 1] != 'O':
        print('Occupied space, going back')
        continue

    ##The turn repeat rule##
    moveid = f'{turn},{inp},{x}-{y + (4 - ((y - 1) * 2))}'
    if moveid in move_arch[-4:]:
        print('Do something new')
        continue
    move_arch += [moveid]

    ###Move and switch turn###
    #@sound
    place()
    if turn == "Black":
        turn = 'Red'
        board[y - 1][x - 1], board[b - 1][a - 1] = "O", 'b'
        if turt:
            turt_plop(x, y, 'White')
            turt_plop(a, b, 'Black')
    elif turn == "Red":
        turn = 'Black'
        board[y - 1][x - 1], board[b - 1][a - 1] = "O", 'r'
        if turt:
            turt_plop(x, y, 'White')
            turt_plop(a, b, 'Red')

    if (didMoveWin((a - 1, b - 1), evil_st[turn], board)):
        print(f"{lawful_st[evil_st[turn]]} won")
        GO = False
        break

if turt:
    #@sound
    win_sound()
    write_win(0, -250, f"{lawful_st[evil_st[turn]]} won!! Congrats!!")
    end = input('Press enter to end match: ')

with open('Game_Archive.txt', 'w') as GA:
    for line in move_arch:
        GA.write(line + '\n')