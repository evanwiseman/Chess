import numpy as np
from Pieces import King, Queen, Rook, Bishop, Knight, Pawn

class Player:
    def __init__(self):
        super().__init__()
        self.name = ""
        self.color = ""
        self.elo = 0
        
        self.pawns = [Pawn() for _ in range(8)]
        self.knights = [Knight() for _ in range(2)]
        self.bishops = [Bishop() for _ in range(2)]
        self.rooks = [Rook() for _ in range(2)]
        self.queens = [Queen() for _ in range(1)]
        self.kings = [King() for _ in range(1)]
        
        
        
        
    def pieces(self) -> int:
        return (len(self.pawns) + 
                len(self.knights) + 
                len(self.bishops) + 
                len(self.rooks) + 
                len(self.queens) + 
                len(self.kings))
    
    def points(self) -> int:
        return ((len(self.pawns) * Pawn.value) + 
                (len(self.knights) * Knight.value) + 
                (len(self.bishops) * Bishop.value) + 
                (len(self.rooks) * Rook.value) + 
                (len(self.queens) * Queen.value))
        
if __name__ == "__main__":
    player1 = Player()
    print(player1.pieces())
    print(player1.points())