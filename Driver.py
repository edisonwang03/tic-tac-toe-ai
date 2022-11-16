from TicTacToe import Board
from time import sleep
import random

board = Board()
user = input("Choose one of the two marks (X or O): ")
if user == "X":
    computer = "O"
elif user == "O":
    computer = "X"
x = random.randint(0,1)
if x == 0:
    y = 1
elif x == 1:
    y = 0
order = {user:x, 
            computer:y}
board = Board()
turn = 1

"""Game loop"""
while turn<=9:
    print("Turn #" + str(turn))
    board.display()
    if turn%2==order[user]:
        position = int(input("It's your turn! Choose a number between 1-9 to place your mark: "))
        board.human_move(position, user)
        if(board.is_winner(user)):
            board.display()
            print("You won")
            break
    elif turn%2==order[computer]:
        print("The computer is making a move...")
        sleep(3) 
        board.ai_move(computer)
        if(board.is_winner(computer)):
            board.display()
            print("You lose")
            break
    turn+=1
    if board.is_tie():
        board.display()
        print("It's a tie")
