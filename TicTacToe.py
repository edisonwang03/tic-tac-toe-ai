class Board():
    """A class to simulate a Tic-Tac-Toe board"""
    
    def __init__(self,user,computer):

        self.grid = [[0,0,0],[0,0,0],[0,0,0]]
        self.user = user
        self.computer = computer
        self.winningPositions = {((0,0), (0,1), (0,2)), ((1,0), (1,1), (1,2)), ((2,0), (2,1), (2,2)), 
                        ((0,0), (1,0), (2,0)), ((0,1), (1,1), (2,1)), ((0,2), (1,2), (2,2)),
                        ((0,0), (1,1), (2,2)), ((0,2), (1,1), (2,0))}
       
       
    def display(self):
        print(" " + str(self.grid[0][0]) + " | " + str(self.grid[0][1]) + " | " + str(self.grid[0][2]))
        print("-----------")
        print(" " + str(self.grid[1][0]) + " | " + str(self.grid[1][1]) + " | " + str(self.grid[1][2]))
        print("-----------")
        print(" " + str(self.grid[2][0]) + " | " + str(self.grid[2][1]) + " | " + str(self.grid[2][2]))
        
      
    def markGrid(self,i,j,mark):
        self.grid[i][j] = mark


    def unmarkGrid(self,i,j):
        self.grid[i][j] = 0
         
    
    def isUserWin(self):
        for((x1,x2),(y1,y2),(z1,z2)) in self.winningPositions:
            if self.grid[x1][x2] == self.user and self.grid[y1][y2] == self.user and self.grid[z1][z2] == self.user:
                return True
        return False
    
    
    def isComputerWin(self):
        for((x1,x2),(y1,y2),(z1,z2)) in self.winningPositions:
            if self.grid[x1][x2] == self.computer and self.grid[y1][y2] == self.computer and self.grid[z1][z2] == self.computer:
                return True
        return False
    
  
    def isDraw(self):
        if self.isComputerWin() or self.isUserWin():
            return False
        for row in self.grid:
            for tile in row:
                if tile==0:
                    return False
        return True
        
        
    def possibleMoves(self):
        moves = set()
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if self.grid[i][j] == 0:
                    moves.add((i,j))
        return moves
                    
                    
    def minimax(self,isMaximizing):
        if self.isComputerWin():
            return 1
        elif self.isUserWin():
            return -1
        elif self.isDraw():
            return 0
        
        if isMaximizing:
            bestScore = float("-inf")
            
            for (i,j) in self.possibleMoves():
                    self.markGrid(i,j,self.computer)
                    score = self.minimax(False)
                    self.unmarkGrid(i,j)
                    if score>bestScore:
                        bestScore = score
            return bestScore
        
        else:
            bestScore = float("inf")
            
            for (i,j) in self.possibleMoves():
                self.markGrid(i,j,self.user)
                score = self.minimax(True)
                self.unmarkGrid(i,j)
                if score<bestScore:
                    bestScore = score
            return bestScore
         
            
    def computerMove(self):
        bestScore = float("-inf")
        moves = self.possibleMoves()
        
        if len(moves) != 0:
            for (i,j) in moves:
                self.markGrid(i,j,self.computer)
                score = self.minimax(False)
                self.unmarkGrid(i,j)
                if score>bestScore:
                    bestScore = score
                    bestI = i
                    bestJ = j
            self.markGrid(bestI, bestJ,self.computer)
        
        
    def userMove(self,i,j):
        self.markGrid(i,j,self.user)
        
                
                        
                        
        
        
        
        