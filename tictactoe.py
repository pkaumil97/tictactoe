"""
Tic Tac Toe Player
"""
import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    countX = 0
    countO = 0
    for row in board:
        for cell in row:
            if cell == X:
                countX += 1
            elif cell == O:
                countO += 1

    if terminal(board):
        return None
    else:
        if countX > countO:
            return O
        elif countX == countO:
            return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    result_of_action = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                result_of_action.add((i, j))
    return result_of_action


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise ValueError("Invalid action.")
    else:
        new_board = copy.deepcopy(board)
        new_board[action[0]][action[1]] = player(board)
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    count_o_row = 0
    count_x_row = 0

    count_o_col = 0
    count_x_col = 0

    count_o_diag = 0
    count_x_diag = 0

    count_o_diag_1 = 0
    count_x_diag_1 = 0

    for i in range(3):
        for j in range(3):

            if board[i][j] == X:
                count_x_row += 1
            elif board[i][j] == O:
                count_o_row += 1

            if board[j][i] == X:
                count_x_col += 1
            elif board[j][i] == O:
                count_o_col += 1

            if i == j and board[i][j] == X:
                count_x_diag += 1
            elif i == j and board[i][j] == O:
                count_o_diag += 1

            if i + j == 2 and board[i][j] == X:
                count_x_diag_1 += 1
            elif i + j == 2 and board[i][j] == O:
                count_o_diag_1 += 1

        if count_o_row == 3 or count_o_col == 3:
            return O
        elif count_x_row == 3 or count_x_col == 3:
            return X

        """
        reset the count for row and col
        """
        count_o_col = 0
        count_o_row = 0
        count_x_row = 0
        count_x_col = 0

    if count_o_diag == 3 or count_o_diag_1 == 3:
        return O
    elif count_x_diag == 3 or count_x_diag_1 == 3:
        return X
    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    count = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] != EMPTY:
                count += 1
    if count == 9 and winner(board) is None:
        return True
    if winner(board) == X or winner(board) == O:
        return True
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0



def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if player(board) == X:
        value = float('-inf')
        best_action = None

        for action in actions(board):
            minValueResult = minValue(result(board, action))

            if minValueResult > value:
                value = minValueResult
                best_action = action

    elif player(board) == O:
        value = float('inf')
        best_action = None

        for action in actions(board):
            maxValueResult = maxValue(result(board, action))

            if maxValueResult < value:
                value = maxValueResult
                best_action = action

    return best_action


def minValue(board):
    if terminal(board):
        return utility(board)
    v = float('inf')

    for action in actions(board):
        v = min(v, maxValue(result(board, action)))
    return v


def maxValue(board):
    if terminal(board):
        return utility(board)
    v = float('-inf')

    for action in actions(board):
        v = max(v, minValue(result(board, action)))
    return v


# board1 = [[X, O, EMPTY],
#           [EMPTY, EMPTY, EMPTY],
#           [EMPTY, EMPTY, EMPTY]]
# print(player(board1))
# # print(terminal(board1))
