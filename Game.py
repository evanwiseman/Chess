from Board import Board
from Player import Player

class Game:
    def __init__(self):
        self.player1 = Player()
        self.player2 = Player()
        self.board = Board()
            

if __name__ == "__main__":
    print("starting game")