
from sounds import *


def whoseSquare(square, board):
    #''' Checks who owns a square using tuple square (y,x), returning the name of the user. Prints indexing erorr!!! if error'''
    try:
        return board[square[1]][square[0]]
    except:
        print('Indexing error with whoseSquare')
        return False


def winVertical(move, user, board):
    ''' Takes in a tuple of the current move (x,y) from the user, or returns True if they won from four in a row vertically '''
    j = move[0]
    count = 1 # Count is 1 b/c current space is that player's
    # Check how many that user owns below the current move
    i = move[1] + 1
    while i != 5:
        if whoseSquare((j,i), board) == user:
            count +=1
        else:
            break
        i += 1

    # Check how many that user owns above, and add to count
    i = move[1] - 1
    while i != -1:
        if whoseSquare((j,i), board) == user:
            count +=1
        else:
            break
        i -= 1
    if count >= 4:
        return True
    #add elif count ==  3 play the sound Im looking for
    elif count == 3:
        storm_sound()
    return False


def winHorizontal(move, user, board):
    ''' Same as winVertical, but for horizontal '''
    i = move[1]
    count = 1
    j = move[0] + 1
    while j != 5:
        if whoseSquare((j,i), board) == user:
            count +=1
        else:
            break
        j += 1

    #Above is right horizontal, below is left horizontal

    j = move[0] - 1
    while j != -1:
        if whoseSquare((j,i), board) == user:
            count +=1
        else:
            break
        j -= 1
    if count >= 4:
        return True
    elif count == 3:
      storm_sound()
    return False


def winDiagonal(move, user, board):
    ''' Checks to see if the user won diagonally '''
    count = 1

    ### This code is for the top right diagonal ###
    j = move[0] + 1
    i = move[1] - 1

    while j != 5 and i != -1:
        if whoseSquare((j,i), board) == user:
            count +=1
        else:
            break
        j += 1
        i -= 1


    j = move[0] - 1
    i = move[1] + 1
    while j != -1 and i != 5:
        if whoseSquare((j,i), board) == user:
            count +=1
        else:
            break
        j -= 1
        i += 1

    if count >= 4:
        return True
    elif count == 3:
      storm_sound()
    ##############################################
    ## Now the code is for the top left diagonal##
    count = 1

    j = move[0] - 1
    i = move[1] - 1

    while j != -1 and i != -1:
        if whoseSquare((j,i), board) == user:
            count +=1
        else:
            break
        j -= 1
        i -= 1

    j = move[0] + 1
    i = move[1] + 1

    while j != 5 and i != 5:
        if whoseSquare((j,i), board) == user:
            count +=1
        else:
            break
        j += 1
        i += 1

    if count >= 4:
        return True
    elif count == 3:
      storm_sound()
    return False


def winSquare(move, user, board):

    ''' Check for each square, starting with top right '''

    j = move[0]
    i = move[1]
    ### Top right and top left squares ###
    if i-1 != -1:
        #top right
        if (j+1) != 5:
            if (whoseSquare((j+1,i-1), board) == user) and (whoseSquare((j,i-1), board) == user) and (whoseSquare((j+1,i), board) == user):
                return True

        #top left
        if (j-1) != -1:
            if (whoseSquare((j-1,i-1), board) == user) and (whoseSquare((j,i-1), board) == user) and (whoseSquare((j-1,i), board) == user):
                return True
    ### Bottom right and left squares ###
    if i+1 != 5:

        #bottom right
        if (j+1) != 5:
            if (whoseSquare((j+1,i+1), board) == user) and (whoseSquare((j,i+1), board) == user) and (whoseSquare((j+1,i), board) == user):
                return True

        #bottom left
        if (j-1) != -1:
            if (whoseSquare((j-1,i+1), board) == user) and (whoseSquare((j,i+1), board) == user) and (whoseSquare((j-1,i), board) == user):
                return True
    return False


def didMoveWin(move, user, board):
    if winVertical(move, user, board) or winHorizontal(move, user, board) or winDiagonal(move,user,board) or winSquare(move,user,board):
        win_sound()
        explosion()
        return True
    return False



  # =============================================================================
  #   print('vertical win', winVertical((x-1,y-1),evil_st[turn],board))
  #   print('whose square is',whoseSquare((x-1,y-1), board))
  #   print('win horizontal', winHorizontal((x-1,y-1),evil_st[turn],board))
  #   print('win diagonal',winDiagonal((x-1,y-1),evil_st[turn],board))
  #   print('win square', winSquare((x-1,y-1),evil_st[turn],board))
  #
  # =============================================================================
