# Source: Tower Capital
# Question: Design a Battleship game board.
#

class BattleShip:
    def __init__(self,size):
        self.grid=[[0] * size for _ in range(size)]
    def printBoard(self):
        for i in range(len(self.grid)):
            print(self.grid[i])




if __name__=="__main__":
    bs=BattleShip(5)
    bs.printBoard()
