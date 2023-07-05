
# def display(row1, row2, row3):
#     print(row1);
#     print(row2);
#     print(row3);

# #define the row 

# row1 = [' ', ' ', ' '];
# row2 = [' ', ' ', ' '];
# row3 = [' ', ' ', ' '];
# #call the function

# display(row1, row2, row3);
# print(row1[0]);

# #then  create an input for the game..using input.
# position_index = int(input('choose the index postion: '))
# print(row1[position_index]);

# def user_choice():
#     #INTIAL VALUE
#     choice = '';
#     acceptable_range = range(0,10)
#     with_range = False
#     #CHECK TWO CONDITION -> 1ST CHECK THE INPUT VALUE IF  IT IS DIGIT 
#     #-> 2ND CHECK IF IT IS BETWEEN RANGE.
#     while choice.isdigit() == False or with_range == False:

#         #GIVE AN INPUT VALUE....
#         choice = input('please enter a number between 0 and 10:  ');

#         #CHECK THE DIGIT ....
#         if choice.isdigit() == False:
#             print('this is not a digit please try again: ');
        
#         #RANGE CHECK...
#         if choice.isdigit() == True:
#             if int(choice) in acceptable_range:
#                 with_range = True;
#             else:
#                 print('please enter between acceptable range sir(0,10)')
#                 with_range = False;
#     return int(choice);

# print(user_choice())
from IPython.display import clear_output

#first we make the display board...
def display_board(board):
    clear_output() #is used to clear the output of the cell or the entire
    # output area

    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('--------------');
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('--------------');
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')


test_board = ['', 'x', 'o', 'x', 'o', 'x', 'o', 'x', 'o', 'x'];
#display_board(test_board);

def player_input():
    marker = ''
    while not (marker == 'X' or marker == 'O'): #Checking if  the spelling is not x or o 
        spelling = input('Player 1: X or O: ').upper() 

        if spelling == 'X':
            return ('X', 'O')
        else:
            return ('O','X');

# print(player_input())

def place_marking(board, player_marker, position):
    board[position]  = player_marker
place_marking(test_board, 'g', 4);
#display_board(test_board);

def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal
# print(win_check(test_board, 'X'));

#then decide which player turn it is

import random

def choose_first():
    if random.randint(0, 1)== 0:
        return 'player 2';
    else:
        return 'player 1';

def space_check(board, position):
    return board[position] ==  ' '

def full_board_check(board):
    for i in range (1,10):
        if space_check(board, i):
            return False
    return True;

def player_choice(board):
    position = 0;
    board_list = [1,2,3,4,5,6,7,8,9]
    while position not in board_list or not space_check(board, position):
        position = int(input('Please Enter your next choice: (1-9)'));

    return position;

def replay():
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y');

#intro
print('welcome to tic tac toe game..! ');

while True:
    #when we reset the board..
    the_board = [' '] *  10;
    player1_marker, player2_marker = player_input();
    #choose the biggner
    turn = choose_first()
    print(turn + ' will go first. ');
    
    #check  if he wants to play 
    play_game = input(' Are You want to the game ? Enter Yes or No.  ');

    #so if he wants to play the game..
    if play_game.lower()[0] == 'y':
         game_on = True;
    else:
        game_on = False;
    
    while game_on:
        #if it is player one turn..

        if turn == 'player 1':
            display_board(the_board);
            position = player_choice(the_board);
            place_marking(the_board, player1_marker, position);

        #check if player_1 win or draw or player2 turn..
            if win_check(the_board, player1_marker):
                display_board(the_board);
                print('Congratulation You have won the game!? ')
                game_on = False

            elif full_board_check(the_board):
                    display_board(the_board)
                    print(' the game is a draw! ')
                    break
            else:
                turn = 'player 2'
        #if it is player2 turn
        elif turn == 'player 2':
            display_board(the_board)
            position = player_choice(the_board)
            place_marking(the_board, player2_marker, position)

            #check if player2 win or draw or  player1 turn..
            if win_check(the_board, player2_marker):
                display_board(the_board);
                print(' Congratulation player 2 you have won the game: ')
                game_on = False
            elif full_board_check(the_board):
                    display_board(the_board)
                    print(' the game ends draw.. ')
                    break
            else:
                turn = 'player 1'
    if not replay():
        break