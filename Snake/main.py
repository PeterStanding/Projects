class Snake:
    print("Snake")
class Apple:
    print("Apple")
class Game:
    def initialize(self, height, width):
        self.height = height
        self.width = width

    def render(self):
        print(f"Height: {self.height}")
        print(f"Width: {self.width}")

game = Game()
game.initialize(10,20)
game.render()