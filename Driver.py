from TicTacToe import Board
from time import sleep
import random
import pygame


pygame.init()

screen_width = 300
screen_height = 300

screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('TicTacToe')

line_width = 6

green = (0,255,0)
red = (255,0,0)

def displayGrid():
    bg = (255,255,200)
    grid = (50,50,50)
    screen.fill(bg)
    for x in range(1,3):
        pygame.draw.line(screen,grid,(0,x*100),(screen_width,x*100),line_width)
        pygame.draw.line(screen,grid,(x*100,0),(x*100,screen_height),line_width)
        

def drawMarkers():
    x_pos = 0
    for x in board.grid:
        y_pos = 0
        for y in x:
            if y == 1:
                pygame.draw.line(screen,green,(x_pos*100+15,y_pos*100+15),(x_pos*100+85,y_pos*100+85),line_width)
                pygame.draw.line(screen,green,(x_pos*100+15,y_pos*100+85),(x_pos*100+85,y_pos*100+15),line_width)
            if y == -1:
                pygame.draw.circle(screen,red,(x_pos*100+50,y_pos*100+50),38,line_width)
            y_pos +=1
        x_pos +=1
            
# Initialize game variables
players = [1,-1]
# currentPlayerTurn = random.choice(players)
board = Board(1,-1)
currentPlayerTurn = -1
    
    


playing = True
done = False
while not done:
    
    # Add event handlers
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN and currentPlayerTurn == 1 and playing:
            pos = pygame.mouse.get_pos()
            cell_x = pos[0]//100
            cell_y = pos[1]//100
            if board.grid[cell_x][cell_y] == 0:
                board.grid[cell_x][cell_y] = 1
                currentPlayerTurn *= -1
    
    if board.isUserWin():
        print("Win")
        playing = False
    if board.isComputerWin():
        print("Loss")
        playing = False
    if board.isDraw():
        print("Draw")
        playing = False
              
    if currentPlayerTurn == -1 and playing:
        board.computerMove()
        currentPlayerTurn*=-1
    
    displayGrid()
    drawMarkers()
    
    pygame.display.update()

pygame.quit()
    
"""

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
board = Board(user,computer)
turn = 1


while turn<=9:
    print("Turn #" + str(turn))
    board.display()
    if turn%2==order[user]:
        position = int(input("It's your turn! Choose a number between 1-9 to place your mark: "))
        board.userMove(position)
        if(board.isPlayerWin()):
            board.display()
            print("You won")
            break
    elif turn%2==order[computer]:
        print("The computer is making a move...")
        sleep(1)
        board.computerMove()
        if(board.isComputerWin()):
            board.display()
            print("You lose")
            break
    turn+=1
    if board.isDraw():
        board.display()
        print("It's a tie")
"""