# Source: Tower Capital
# Question: Design Tic-Tac-Toe with move validation and win detection.
#

import enum
class Cell(enum.Enum):
    EMPTY=0
    X=1
    O=2

class TicTacToe:
    def __init__(self):
        self.board=[[Cell.EMPTY]*3 for _ in range(3)]
        self._numRow=len(self.board)
        self._numCol=len(self.board[0])
        self.freeSpace=3*3


    # def initBoard(self):


    def occupySpace(self,row,col,playerPiece):
        if not 0<=row<self._numRow or not 0<=col<self._numCol or self.board[row][col]!=Cell.EMPTY:
            raise ValueError("Cell already occupied")

        self.board[row][col]=playerPiece
        self.freeSpace-=1

        return True

    def checkDraw(self):
        return self.freeSpace==0

    def checkWin(self, r, c,playerPiece):

        # check vertical
        currCount=0
        for row in range(self._numRow):
            if self.board[row][c]==playerPiece:
                currCount+=1
            else:
                currCount=0
            if currCount>=3:
                return True

        # check horizontal
        currCount=0
        for col in range(self._numCol):
            if self.board[r][col]==playerPiece:
                currCount+=1
            else:
                currCount=0
            if currCount>=3:
                return True

        # check diagonal
        currCount=0
        for row in range(self._numRow):
            col=c+r-row
            if 0<=col<self._numCol and self.board[row][col]==playerPiece:
                currCount+=1
            if currCount>=3:
                return True

        #check antidiagonal
        currCount=0
        for row in range(self._numRow):
            col=c-r+row
            if 0<=col<self._numCol and self.board[row][col]==playerPiece:
                currCount+=1
            if currCount>=3:
                return True

        return False

    def printBoard(self):
        for r in range(self._numRow):
            print([x.name for x in self.board[r]])

class Game:
    def __init__(self):
        self.game=TicTacToe()
        self.players=[Cell.X, Cell.O]

    def playRound(self):
        self.game.printBoard()
        while True:
            for player in self.players:
                row=int(input(f"Enter row for Player {player.value}:"))
                col=int(input(f"Enter col for Player {player.value}:"))
                self.game.occupySpace(row,col,player)
                self.game.printBoard()
                if self.game.checkDraw():
                    print(f"Game Over, Draw")
                    return
                if self.game.checkWin(row,col,player):
                    print(f"Game Over, Winner: {player.value}")
                    return



if __name__=="__main__":
    ttt=Game()
    ttt.playRound()


# ============================================================
# IMPROVED VERSION (commented out for reference)
# ============================================================

# import enum
# import itertools
#
# class Cell(enum.Enum):
#     EMPTY=0
#     X=1
#     O=2
#
# class TicTacToe:
#     # IMPROVEMENT 1: Precompute all 8 winning lines as flat indices (row*3+col).
#     # This replaces the 4 manual loop checks in checkWin with a single O(1) subset check.
#     WIN_CONDITIONS = [
#         {0,1,2}, {3,4,5}, {6,7,8},  # rows
#         {0,3,6}, {1,4,7}, {2,5,8},  # cols
#         {0,4,8}, {2,4,6},            # diagonals
#     ]
#
#     def __init__(self):
#         # IMPROVEMENT 2: Track each player's occupied positions as a set of flat indices
#         # instead of a 2D board array. Eliminates _numRow/_numCol/_board/_freeSpace.
#         self.moves = {Cell.X: set(), Cell.O: set()}
#         self._total_moves = 0
#
#     def occupySpace(self, row, col, player):
#         pos = row * 3 + col
#         all_occupied = self.moves[Cell.X] | self.moves[Cell.O]
#         if not (0 <= row < 3 and 0 <= col < 3) or pos in all_occupied:
#             raise ValueError("Invalid or occupied cell")
#         self.moves[player].add(pos)
#         self._total_moves += 1
#
#     def checkDraw(self):
#         return self._total_moves == 9
#
#     # IMPROVEMENT 3: checkWin no longer needs row/col args — it just checks if any
#     # win condition is a subset of that player's moves. Clean and extensible.
#     def checkWin(self, player):
#         return any(condition <= self.moves[player] for condition in self.WIN_CONDITIONS)
#
#     def printBoard(self):
#         all_moves = {pos: p for p, positions in self.moves.items() for pos in positions}
#         for row in range(3):
#             print([all_moves.get(row*3+col, Cell.EMPTY).name for col in range(3)])
#
# class Game:
#     def __init__(self):
#         self.game = TicTacToe()
#         # IMPROVEMENT 4: itertools.cycle replaces the `while True: for player` nesting.
#         # Each iteration is one player's turn — no double-loop needed.
#         self.players = itertools.cycle([Cell.X, Cell.O])
#
#     def playRound(self):
#         self.game.printBoard()
#         for player in self.players:
#             row = int(input(f"Enter row for Player {player.name}: "))
#             col = int(input(f"Enter col for Player {player.name}: "))
#             self.game.occupySpace(row, col, player)
#             self.game.printBoard()
#             if self.game.checkWin(player):
#                 print(f"Game Over, Winner: {player.name}")
#                 return
#             if self.game.checkDraw():
#                 print("Game Over, Draw")
#                 return
#
# if __name__=="__main__":
#     ttt = Game()
#     ttt.playRound()