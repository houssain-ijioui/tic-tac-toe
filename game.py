from random import randrange

board = [[1, 2, 3], [4, "X", 6], [7, 8, 9]]


def display_board(board):
    print("+-------" * 3, "+", sep="")
    for row in range(3):
        print("|       " * 3, "|", sep="")
        for col in range(3):
            print("|   " + str(board[row][col]) + "   ", end="")
        print("|")
        print("|       " * 3, "|", sep="")
        print("+-------" * 3, "+", sep="")


def make_move(board):
    while True:
        # check if the input is an integer
        try:
            move = int(input("Make move: "))
        except ValueError:
            print("Only numbers are allowed")
            continue
        else:
            # check if entered number is within 1 and 9 range
            if move not in range(1, 10):
                print("Numbers must be: 0 < numbers < 10")
                continue
            # check if entered number is still not filled
            elif not any(move in row for row in board):
                print("Entered number is already filled")
            else:
                break
    
    for row in board:
        for i in row:
            if i == move:
                board[board.index(row)][row.index(i)] = "O"


def make_list_of_free_fields(board):
    free_fields = []
    for row in board:
        for i in row:
            if i in range(1, 10):
                free_fields.append((board.index(row), row.index(i)))
    return free_fields


def draw_move(board):
    free_fields = make_list_of_free_fields(board)
    field = free_fields[randrange(len(free_fields))]
    board[field[0]][field[1]] = "X"


# make a list of possible winning combinations
def win_combinations(n):
    # Rows
    for r in range(n):
        yield [(r, c) for c in range(n)]
    # Columns
    for c in range(n):
        yield [(r, c) for r in range(n)]
    # Diagonal top left to bottom right
    yield [(i, i) for i in range(n)]
    # Diagonal top right to bottom left
    yield [(i, n - 1 - i) for i in range(n)]


global won
won = False

while len(make_list_of_free_fields(board)) > 0 and won ==  False:
    for c in win_combinations(3):
        # check if x won if true exit the program
        if board[c[0][0]][c[0][1]] == "X" and board[c[1][0]][c[1][1]] == "X" and board[c[2][0]][c[2][1]] == "X":
            won = True
            display_board(board)
            print("Computer won")
            exit()
        # check if o won if true exit the program
        elif board[c[0][0]][c[0][1]] == "O" and board[c[1][0]][c[1][1]] == "O" and board[c[2][0]][c[2][1]] == "O":
            won = True
            display_board(board)
            print("You won")
            exit()
        

    display_board(board)
    make_move(board)
    display_board(board)
    draw_move(board)

display_board(board)