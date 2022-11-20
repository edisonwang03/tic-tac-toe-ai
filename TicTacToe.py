import random

class Board():
    """A class to simulate a Tic-Tac-Toe board"""
    
    def __init__(self,user,computer):

        self.grid = [[1,2,3],[4,5,6],[7,8,9]]
        self.user = user
        self.computer = computer
       
       
    def display(self):
        print(" " + str(self.grid[0][0]) + " | " + str(self.grid[0][1]) + " | " + str(self.grid[0][2]))
        print("-----------")
        print(" " + str(self.grid[1][0]) + " | " + str(self.grid[1][1]) + " | " + str(self.grid[1][2]))
        print("-----------")
        print(" " + str(self.grid[2][0]) + " | " + str(self.grid[2][1]) + " | " + str(self.grid[2][2]))
        
      
    def markGrid(self,cell_number,mark):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if self.grid[i][j]==cell_number:
                    self.grid[i][j]=mark


    def unmarkGrid(self,cell_number):
        counter = 1
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if counter == cell_number:
                    self.grid[i][j] = cell_number
                counter+=1
         
    
    def isPlayerWin(self):
        winningPositions = {((0,0), (0,1), (0,2)), ((1,0), (1,1), (1,2)), ((2,0), (2,1), (2,2)), 
                        ((0,0), (1,0), (2,0)), ((0,1), (1,1), (2,1)), ((0,2), (1,2), (2,2)),
                        ((0,0), (1,1), (2,2)), ((0,2), (1,1), (2,0))}
        for((x1,x2),(y1,y2),(z1,z2)) in winningPositions:
            if self.grid[x1][x2] == self.user and self.grid[y1][y2] == self.user and self.grid[z1][z2] == self.user:
                return True
        return False
    
    
    def isComputerWin(self):
        winningPositions = {((0,0), (0,1), (0,2)), ((1,0), (1,1), (1,2)), ((2,0), (2,1), (2,2)), 
                        ((0,0), (1,0), (2,0)), ((0,1), (1,1), (2,1)), ((0,2), (1,2), (2,2)),
                        ((0,0), (1,1), (2,2)), ((0,2), (1,1), (2,0))}
        for((x1,x2),(y1,y2),(z1,z2)) in winningPositions:
            if self.grid[x1][x2] == self.computer and self.grid[y1][y2] == self.computer and self.grid[z1][z2] == self.computer:
                return True
        return False
    
  
    def isDraw(self):
        for i in self.grid:
            for j in i:
                if j in range(1,10):
                    return False
        return True
        
        
    def possibleMoves(self):
        moves = []
        for i in self.grid:
            for j in i:
                if j in range(1,10):
                    moves.append(j)
        return moves
                    
                    
    def minimax(self,isMaximizing):
        if self.isComputerWin():
            return 1
        elif self.isPlayerWin():
            return -1
        elif self.isDraw():
            return 0
        
        if isMaximizing:
            bestScore = float("-inf")
            
            for i in self.grid:
                for j in i:
                    if j in self.possibleMoves():
                        self.markGrid(j,self.computer)
                        score = self.minimax(False)
                        self.unmarkGrid(j)
                        if score>bestScore:
                            bestScore = score
            return bestScore
        
        else:
            bestScore = float("inf")
            
            for i in self.grid:
                for j in i:
                    if j in self.possibleMoves():
                        self.markGrid(j,self.user)
                        score = self.minimax(True)
                        self.unmarkGrid(j)
                        if score<bestScore:
                            bestScore = score
            return bestScore
         
            
    def computerMove(self):
        bestScore = float("-inf")
        moves = self.possibleMoves()
        for i in moves:
            self.markGrid(i,self.computer)
            score = self.minimax(False)
            self.unmarkGrid(i)
            if score>bestScore:
                bestScore = score
                bestMove = i
        self.markGrid(bestMove,self.computer)
        
        
    def userMove(self,cellNumber):
        self.markGrid(cellNumber,self.user)
        
                
                        
                        
        
        
        
        