import random

class Board():
    
    def __init__(self):
        self.grid = [[1,2,3],[4,5,6],[7,8,9]]
       
       
    def display(self):
        print(" " + str(self.grid[0][0]) + " | " + str(self.grid[0][1]) + " | " + str(self.grid[0][2]))
        print("-----------")
        print(" " + str(self.grid[1][0]) + " | " + str(self.grid[1][1]) + " | " + str(self.grid[1][2]))
        print("-----------")
        print(" " + str(self.grid[2][0]) + " | " + str(self.grid[2][1]) + " | " + str(self.grid[2][2]))
        
        
    def human_move(self,cell_number,mark):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if self.grid[i][j]==cell_number:
                    self.grid[i][j]=mark
         
         
    def ai_move(self,mark):
        done = False
        while not done:
            cell_number = random.randint(1,9)
            for i in range(len(self.grid)):
                for j in range(len(self.grid[i])):
                    if self.grid[i][j]==cell_number:
                        self.grid[i][j]=mark
                        done = True
     
     
    def is_winner(self,mark):
        winningPositions = {((0,0), (0,1), (0,2)), ((1,0), (1,1), (1,2)), ((2,0), (2,1), (2,2)), 
                        ((0,0), (1,0), (2,0)), ((0,1), (1,1), (2,1)), ((0,2), (1,2), (2,2)),
                        ((0,0), (1,1), (2,2)), ((0,2), (1,1), (2,0))}
        for((x1,x2),(y1,y2),(z1,z2)) in winningPositions:
            if self.grid[x1][x2] == mark and self.grid[y1][y2] == mark and self.grid[z1][z2] == mark:
                return True
        return False
    
    
    def is_tie(self):
        for i in self.grid:
            for j in i:
                if j in range(1,10):
                    return False
        return True