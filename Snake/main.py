import numpy as np

class Snake:
    def initialise(self,init_body, init_direction):
        self.body = init_body
        self.direction = init_direction
    
    def take_step(self, pos):
        self.body = self.body[1:] + [pos]
    
    def set_direction(self,direction):
        self.direction = direction
    
    def head():
        return self.body[-1]
class Apple:
    print("Apple")
class Game:
    def initialize(self, height, width):
        self.height = height
        self.width = width
        self.snake = Snake([(0, 0), (1, 0), (2, 0), (3, 0)], "UP")

    def board_matrix(self):
        matrix = []
        s = ""

        for h in range(self.height):
            s = [0]*self.width
            matrix.append(s)
    
        return matrix
        #print('\n'.join([str(lst) for lst in matrix]))

    def render(self):
        matrix = self.board_matrix()

        for i in range(len(matrix)):
            if i == 0 or i == len(matrix)-1:
                print("+", " - "*(self.width),"+")
            else:
                print("|",matrix[i-1],"|")

game = Game()
game.initialize(10,20)
game.render()