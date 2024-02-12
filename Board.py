import numpy as np

class Board:
    size = (0, 0)
    
    def __init__(self) -> None:
        super().__init__()
        
        return
    
    def initial_setup(self) -> None:
        self.size = (8, 8)
        
if __name__ == "__main__":
    board = Board()
    board.initial_setup()
    
    print(board.size)
    print(board.piece_locations)