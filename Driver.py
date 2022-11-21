from TicTacToe import Board
import random
import pygame
from pygame.locals import *

# Initialize pygame
pygame.init()


# Initialize constants
SCREEN_WIDTH = 300
SCREEN_HEIGHT = 300
LINE_WIDTH = 6
GREEN = (0,255,0)
RED = (255,0,0)
BLUE = (0,0,255)
YELLOW = (255,255,200)
TEXT_FONT = pygame.font.SysFont(None, 40)

# Initialize game variables
players = [1,-1] # 1 represents the user's symbol, X, while -1 represents the computer's symbol, O
currentPlayerTurn = random.choice(players)
board = Board(1,-1)
computerProcessingTimer = 0
if currentPlayerTurn == -1:
    isProcessing = True
else:
    isProcessing = False
gameOver = False


# Initialize play again button
playAgainRectangle = Rect(SCREEN_WIDTH // 2 - 80, SCREEN_HEIGHT // 2, 160, 50)
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('TicTacToe')


# Draw the grid divisions
def drawGrid():
    grid = (50,50,50)
    screen.fill(YELLOW)
    for x in range(1,3):
        pygame.draw.line(screen,grid,(0,x*100),(SCREEN_WIDTH,x*100),LINE_WIDTH)
        pygame.draw.line(screen,grid,(x*100,0),(x*100,SCREEN_HEIGHT),LINE_WIDTH)
        

# Draw the user and computer markers
def drawMarkers():
    x_pos = 0
    for x in board.grid:
        y_pos = 0
        for y in x:
            if y == 1:
                pygame.draw.line(screen,GREEN,(x_pos*100+15,y_pos*100+15),(x_pos*100+85,y_pos*100+85),LINE_WIDTH)
                pygame.draw.line(screen,GREEN,(x_pos*100+15,y_pos*100+85),(x_pos*100+85,y_pos*100+15),LINE_WIDTH)
            if y == -1:
                pygame.draw.circle(screen,RED,(x_pos*100+50,y_pos*100+50),38,LINE_WIDTH)
            y_pos +=1
        x_pos +=1

# Draw the computer processing messages
def drawProcessing():
    processingText = "Processing..."
    processingImage = TEXT_FONT.render(processingText,True,BLUE)
    processingRectangle = pygame.draw.rect(screen,GREEN,(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 60, 200, 50))
    screen.blit(processingImage,processingImage.get_rect(center = processingRectangle.center))


# Draw the game over UI     
def drawResults(winner):
    if winner == 1:
        resultsText = "You won!"
    elif winner == -1:
        resultsText = "You lose..."
    else:
        resultsText = "It's a draw"
    resultsImage = TEXT_FONT.render(resultsText,True,BLUE)
    resultsRectangle = pygame.draw.rect(screen,GREEN,(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 60,200,50))
    screen.blit(resultsImage,resultsImage.get_rect(center = resultsRectangle.center))
    
    playAgainText = "Play again?"
    playAgainImage = TEXT_FONT.render(playAgainText,True,BLUE)
    pygame.draw.rect(screen,GREEN,playAgainRectangle)
    screen.blit(playAgainImage,playAgainImage.get_rect(center = playAgainRectangle.center))


# Game loop
done = False
while not done:
    
    # Add event handlers
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            
        # User move
        if event.type == pygame.MOUSEBUTTONDOWN and currentPlayerTurn == 1 and not gameOver:
            pos = pygame.mouse.get_pos()
            cell_x = pos[0]//100
            cell_y = pos[1]//100
            if board.grid[cell_x][cell_y] == 0:
                board.grid[cell_x][cell_y] = 1
                currentPlayerTurn *= -1
                isProcessing = True
        
        # Reset game variables
        if event.type == pygame.MOUSEBUTTONDOWN and gameOver:
            pos = pygame.mouse.get_pos()
            if playAgainRectangle.collidepoint(pos):
                currentPlayerTurn = random.choice(players)
                board = Board(1,-1)
                computerProcessingTimer = 0
                if currentPlayerTurn == -1:
                    isProcessing = True
                else:
                    isProcessing = False
                gameOver = False     
    
    # Draw the game
    drawGrid()
    drawMarkers()
    
    # Draws the processing message and updates the timer
    if isProcessing:
        drawProcessing()
        computerProcessingTimer+=1
    
    # Check if the game is over
    if board.isUserWin() or board.isComputerWin() or board.isDraw():
        gameOver = True
        
         
    # Computer move     
    if currentPlayerTurn == -1 and not gameOver and computerProcessingTimer == 5000:
        board.computerMove()
        currentPlayerTurn*=-1
        computerProcessingTimer = 0
        isProcessing = False
    
    # Draw the game over UI
    if gameOver:
        if board.isUserWin():
            drawResults(1)
        elif board.isComputerWin():
            drawResults(-1)
        else:
            drawResults(0)
    
    
    # Update the screen      
    pygame.display.update()


# Close pygame
pygame.quit()