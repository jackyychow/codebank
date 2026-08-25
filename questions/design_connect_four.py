# Source: Tower Capital
# Question: Design Connect Four with move validation and win detection.
#

import enum

class Cell(enum.enum):
    EMPTY=0
    YELLOW=1
    RED=2
    
class ConnectFour:
    def __init__(self,row,col):
        self.board=[[Cell.EMPTY]*col for _ in range(row)]
        

    def printBoard(self):
        for i in range(len(self.board)):
            print(self.board[i])

    def dropChip(self,col,player):
        if col < 0 or col >= len(self.board[0]):
            raise ValueError('Invalid column')
        for i in range(len(self.board)-1,-1,-1):
            if self.board[i][col]==Cell.EMPTY:
                self.board[i][col]=player
                break

        return self.checkWin(player,i,col)

    def checkWin(self,player,row,col):
        #check vertical
        curr=0
        for r in range(len(self.board)):
            if self.board[r][col]==player:
                curr+=1
            else:
                curr=0
            if curr==4:
                return True
            
            
        #check hori
        curr=0
        for c in range(len(self.board[0])):
            if self.board[row][c]==player:
                curr+=1
            else:
                curr=0
            if curr==4:
                return True
            
        # Check diagonal
        count = 0
        for r in range(len(self.board)):
            c = row + col - r
            if c >= 0 and c < self._columns and self._grid[r][c] == piece:
                count += 1
            else:
                count = 0
            if count == 4:
                return True

        # Check anti-diagonal
        count = 0
        for r in range(len(self.board)):
            c = col - row + r
            if c >= 0 and c < self._columns and self._grid[r][c] == piece:
                count += 1
            else:
                count = 0
            if count == 4:
                return True
            
        
        return False
        
class Game:
    def __init__(self, board,score):
        self.board=board
        self.targetScore=score
        self.players=[Cell.RED,Cell.YELLOW]

    def play(self):
        while True:
            for players in self.players:
                row,col=self.playMove(player)


if __name__=="__main__":
    row,col=10,10
    cf=ConnectFour(row,col)
    # cf.printBoard()
    cf.dropChip(1,"X")
    cf.printBoard()