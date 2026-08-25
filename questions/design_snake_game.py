# Question: Design a playable Snake game with movement, food, collisions, and scoring.
#

from collections import deque
import random

directions={
    "U": (-1,0),
    "D":(1,0),
    "L":(0,-1),
    "R":(0,1),
}

opposite_direction={
    "U": "D",
    "D": "U",
    "R": "L",
    "L": "R"
}

class SnakeGame:
    def __init__(self,row,col,winning_score):
        self.row=row
        self.col=col
        self.winning_score=winning_score
        self.current_score=0
        self.is_gameover=False

        self.current_direction=""
        self.snake_body=deque()
        self.snake_body.append((row//2,col//2))

        self.occupied_cell=set()
        self.occupied_cell.add((row//2,col//2))
        
        self.food_cell=self.generate_food()

    def generate_food(self):
        # while True:
        #     food_row = random.randint(0, self.row - 1)
        #     food_col = random.randint(0, self.col - 1)
        #     if (food_row, food_col) not in self.occupied_cell:
        #         return (food_row, food_col)       
        candidates=[]
        for row in range(self.row):
            for col in range(self.col):
                if (row,col) not in self.snake_body:
                    candidates.append((row,col))
        if not candidates:
            return None
        return random.choice(candidates)

    # check valid move
    def _valid_move(self, move_direction):
        if move_direction not in directions:
            return False, "Invalid move"
        if self.current_direction!="" and move_direction==opposite_direction[self.current_direction]:
            return False, "Invalid direction"
        return True,""

    def move_snake(self,move_direction):
        is_valid, reason = self._valid_move(move_direction)
        if not is_valid:
            return False, reason

        # set current direction
        self.current_direction=move_direction
        
        snake_head=self.snake_body[0]
        new_direction_step=directions[move_direction]
        new_row,new_col=snake_head[0]+new_direction_step[0], snake_head[1]+new_direction_step[1]

        # Check if hit boundary, if looping is possible, use %self.row
        if not 0<=new_row<self.row or not 0<=new_col<self.col:
            self.is_gameover=True
            return False, "Out of bounds"

        # direction_char="|" if move_direction=="U" or move_direction=="D" else "-"

        # check if is foodcell
        if (new_row,new_col)==self.food_cell:
            self.current_score+=1
            if self.current_score>=self.winning_score:
                self.is_gameover=True
                return True, "You Win!"
                
            self.snake_body.appendleft((new_row,new_col))
            self.occupied_cell.add((new_row,new_col))
            self.food_cell=self.generate_food()
            return True, "Food eaten"

        #check for collision if not food cell
        else:
            self.occupied_cell.remove(self.snake_body.pop())
            if (new_row,new_col) in self.occupied_cell:
                self.is_gameover=True
                return False, "Game Over"

            self.snake_body.appendleft((new_row,new_col))
            self.occupied_cell.add((new_row,new_col))

        return True, ""

    def print_board(self):
        for i in range(self.row):
            statement=[]
            for j in range(self.col):
                if (i,j)== self.snake_body[0]:
                    statement.append("H")
                elif (i,j) in self.occupied_cell:
                    statement.append("0")
                elif (i,j) == self.food_cell:
                    statement.append("*")
                else:
                    statement.append(".")
            print("".join(statement))


if __name__=="__main__":
    game=SnakeGame(5,5,5)
    while not game.is_gameover:
        game.print_board()
        user_input=input("Enter next move: ")
        is_valid, reason=game.move_snake(user_input)
        if not is_valid:
            print(reason)

    print("Points: ",game.current_score)
    if game.current_score>=game.winning_score:
        print("You win!")
    else:
        print("You lost")
    