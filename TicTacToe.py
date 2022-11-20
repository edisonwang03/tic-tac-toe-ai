class Board():
    """ A class to represent a Tic-Tac-Toe game
    """
    
    def __init__(self,user,computer):
        """ Constructs the grid and rules

        Args:
            user (int): unique number representing the user's mark
            computer (int): unique number representing the computer's mark
        """
        self.grid = [[0,0,0],[0,0,0],[0,0,0]]
        self.user = user
        self.computer = computer
        self.winningPositions = {((0,0), (0,1), (0,2)), ((1,0), (1,1), (1,2)), ((2,0), (2,1), (2,2)), 
                        ((0,0), (1,0), (2,0)), ((0,1), (1,1), (2,1)), ((0,2), (1,2), (2,2)),
                        ((0,0), (1,1), (2,2)), ((0,2), (1,1), (2,0))}
        
      
    def markGrid(self,i,j,mark):
        """ Marks the grid at a given tile with a given mark

        Args:
            i (int): row index of the tile
            j (int): column index of the tile
            mark (int): unique number representing the player's mark
        """
        self.grid[i][j] = mark


    def unmarkGrid(self,i,j):
        """ Unmarks the grid at a given tile

        Args:
            i (int): row index of the tile
            j (int): column index of the tile
        """
        self.grid[i][j] = 0
         
    
    def isUserWin(self):
        """ Determines whether the user has won yet or not

        Returns:
            bool: whether the user has won yet or not
        """
        for((x1,x2),(y1,y2),(z1,z2)) in self.winningPositions:
            if self.grid[x1][x2] == self.user and self.grid[y1][y2] == self.user and self.grid[z1][z2] == self.user:
                return True
            
        return False
    
    
    def isComputerWin(self):
        """ Determines whether the computer has won yet or not

        Returns:
            bool: whether the user has won yet or not
        """
        for((x1,x2),(y1,y2),(z1,z2)) in self.winningPositions:
            if self.grid[x1][x2] == self.computer and self.grid[y1][y2] == self.computer and self.grid[z1][z2] == self.computer:
                return True
            
        return False
    
  
    def isDraw(self):
        """ Determines whether the game has a draw

        Returns:
            bool: whether there is a draw or not
        """
        if self.isComputerWin() or self.isUserWin():
            return False
        
        for row in self.grid:
            for tile in row:
                if tile==0:
                    return False
                
        return True
        
        
    def possibleMoves(self):
        """ Determines the possible moves that can be made on the current grid

        Returns:
            list : list of tuples, where each tuple are the indexes of tiles
        """
        moves = set()
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if self.grid[i][j] == 0:
                    moves.add((i,j))
        return moves
                    
                    
    def minimax(self,isMaximizing):
        """ Uses minimax algorithm to calculate the outcome score for each move and the best outcome score

        Args:
            isMaximizing (bool): whether calculating the maximum or minimum score

        Returns:
            int: the best score
        """
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
        """ Makes the best move for the computer and marks the tile
        """
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
        """ Makes the move that the user wants to make and marks the tile

        Args:
            i (int): the row index of the tile
            j (int): the column index of the tile
        """
        self.markGrid(i,j,self.user)
        
                
                        
                        
        
        
        
        