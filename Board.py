import numpy as np

class Board:
    size = (0, 0)
    piece_locations = np.empty((0, 0), dtype=str)
    
    def __init__(self):
        super().__init__()
        
        return
    
    def initial_setup(self):
        self.size = (8, 8)
        self.piece_locations = np.empty(self.size, dtype=str)
        
if __name__ == "__main__":
    board = Board()
    board.initial_setup()
    
    print(board.size)
    print(board.piece_locations)