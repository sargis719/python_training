import random

class Error(Exception):
    """Base class for other exceptions"""
    pass
class Not_Available(Error):
    """Raised when the given position on the board is not available"""
    pass
class Out_Of_Range(Error):
    """Raised when the input is out of a certain range"""
    pass

class CustomException(Error):
    """Custom made Exception for handling multiple type of exceptions"""
    pass

def print_board(brd):
    print(brd[1] + '|' + brd[2] + '|' + brd[3])
    print(brd[4] + '|' + brd[5] + '|' + brd[6])
    print(brd[7] + '|' + brd[8] + '|' + brd[9])

def play_again():
    """
    This function asks the player if they want to play again
    and returns a boolean True if they do want to play again.
    """
    while True:
        try:
            answer = input("Do you want to play again y/n? ")
            if answer != 'y' and answer != 'Y' and answer != 'n' and answer != 'N':
                raise CustomException
            break
        except CustomException:
            print("Please Enter Y or N")
    if answer == 'y' or answer == 'Y':
        return True
    else:
        return False

def is_available(brd1, aspace):
    """
    This function returns a boolean indicating whether a space
    on the board is freely available.
    """
    if brd1[aspace] == " ":
        return True
    return False

def next_step(brd2, name):
    """
    This function asks for a player's next position (as a number 1-9)
    and then uses is_available to check if its a free position.
    If it is, then return the position for later use.
    """
    while True:
        try:
            next_pos = int(input("{} please enter your position (number 1-9): ".format(name)))
            if next_pos < 1 or next_pos > 9:
                raise Out_Of_Range
            else:
                if is_available(brd2, next_pos) == False:
                    raise Not_Available
            break
        except ValueError:
            print("Not a valid entry!")
        except Out_Of_Range:
            print("Please enter a number between 1-9")
        except Not_Available:
            print("The position is not available!")
    return next_pos

def is_full(brd3):
    """
    This function checks if the board is full and returns a boolean value.
    True if full, False otherwise.
    """
    for i in range(1, len(brd3), 1):
        if brd3[i] == ' ':
            return False
    print("There is no winner!")
    return True

def who_goes_first():
    """
    This function uses the random module to randomly decide which player goes first
    and returns a string of which player went first.
    """
    rand_num = random.randint(1, 2)
    return rand_num

def user_marker():
    """
    This function takes in a player input and assign their marker as 'X' or 'O'.
    """
    while True:
        try:
            marker = input("Please select 'x' or 'o': ")
            if marker != 'x' and marker != 'X' and marker != 'o' and marker != 'O':
                raise CustomException
            break
        except CustomException:
            print("Invalid Entry!")
    return marker

def board_assign(brd4, mark, pos):
    """
    This function takes in the board list object, a marker ('X' or 'O'),
    and a desired position (number 1-9) and assigns it to the board.
    """
    brd4[pos] = mark

def is_winner(my_board):
    """
    This function takes in a board and checks to see if someone has won
    """
    if my_board[1] == 'x' and my_board[2] == 'x' and my_board[3] == 'x' or \
        my_board[4] == 'x' and my_board[5] == 'x' and my_board[6] == 'x' or \
        my_board[7] == 'x' and my_board[8] == 'x' and my_board[9] == 'x' or \
        my_board[1] == 'x' and my_board[4] == 'x' and my_board[7] == 'x' or \
        my_board[2] == 'x' and my_board[5] == 'x' and my_board[8] == 'x' or \
        my_board[3] == 'x' and my_board[6] == 'x' and my_board[9] == 'x' or \
        my_board[1] == 'x' and my_board[5] == 'x' and my_board[9] == 'x' or \
        my_board[3] == 'x' and my_board[5] == 'x' and my_board[7] == 'x':
        return (True, 'x')
    elif my_board[1] == 'o' and my_board[2] == 'o' and my_board[3] == 'o' or \
        my_board[4] == 'o' and my_board[5] == 'o' and my_board[6] == 'o' or \
        my_board[7] == 'o' and my_board[8] == 'o' and my_board[9] == 'o' or \
        my_board[1] == 'o' and my_board[4] == 'o' and my_board[7] == 'o' or \
        my_board[2] == 'o' and my_board[5] == 'o' and my_board[8] == 'o' or \
        my_board[3] == 'o' and my_board[6] == 'o' and my_board[9] == 'o' or \
        my_board[1] == 'o' and my_board[5] == 'o' and my_board[9] == 'o' or \
        my_board[3] == 'o' and my_board[5] == 'o' and my_board[7] == 'o':
        return(True, 'o')
    return False

print("Hello, let's play Tic Tac Toe")
new_game = True
player1 = {"name": " ", "mark": " ", "first": False, "winner": False}
player2 = {"name": " ", "mark": " ", "first": False, "winner": False}
player1["name"] = input("Please enter first player name: ")
player2["name"] = input("Please enter second player name: ")
if who_goes_first() == 1:
    player1["first"] = True
    print(player1["name"], " starts the game")
    mark = user_marker()
    if mark == 'x' or mark == 'X':
        player1["mark"] = 'x'
        player2["mark"] = 'o'
    else:
        player1["mark"] = 'o'
        player2["mark"] = 'x'
else:
    player2["first"] = True
    print(player2["name"], " starts the game")
    mark = user_marker()
    if mark == 'x' or mark == 'X':
        player2["mark"] = 'x'
        player1["mark"] = 'o'
    else:
        player2["mark"] = 'o'
        player1["mark"] = 'x'
while new_game:
    board = ['*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    while is_full(board) == False and is_winner(board) == False:
        if player1["first"] == True:
            board_assign(board, player1["mark"], next_step(board, player1["name"]))
            print_board(board)
            if is_winner(board) == False and is_full(board) == False:
                board_assign(board, player2["mark"], next_step(board, player2["name"]))
                print_board(board)
            else:
                break
        else:
            board_assign(board, player2["mark"], next_step(board, player2["name"]))
            print_board(board)
            if is_winner(board) == False and is_full(board) == False:
                board_assign(board, player1["mark"], next_step(board, player1["name"]))
                print_board(board)
            else:
                break
    if is_winner(board):
        if is_winner(board)[1] == 'x':
            if player1["mark"] == 'x':
                player1["winner"] = True
                player2["winner"] = False
                print("Congratulations {}, you won!".format(player1["name"]))
            else:
                player2["winner"] = True
                player1["winner"] = False
                print("Congratulations {}, you won!".format(player2["name"]))
        else:
            if player1["mark"] == 'o':
                player1["winner"] = True
                player2["winner"] = False
                print("Congratulations {}, you won!".format(player1["name"]))
            else:
                player2["winner"] = True
                player1["winner"] = False
                print("Congratulations {}, you won!".format(player2["name"]))
    if play_again():
        new_game = True
        if player1["winner"] == True:
            player1["first"] = True
            player2["first"] = False
            print(player1["name"], " starts the game")
        else:
            player2["first"] = True
            player1["first"] = False
            print(player2["name"], " starts the game")
    else:
        print("Thank you for playing. Bye!")
        new_game = False