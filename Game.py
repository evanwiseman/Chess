from Board import Board
from Player import Player

class Game:
    def __init__(self) -> None:
        self.player1 = Player()
        self.player2 = Player()
        self.board = Board()
        
        return

if __name__ == "__main__":
    print("starting game...")
    game = Game()