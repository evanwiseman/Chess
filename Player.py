import numpy as np
from Pieces import King, Queen, Rook, Bishop, Knight, Pawn

class Player:
    def __init__(self, name="", color="") -> None:
        super().__init__()
        self.name = name
        self.color = color
        
        self.pawns = 8
        self.knights = 2
        self.bishops = 2
        self.rooks = 2
        self.queens = 1
        self.kings = 1
        
        return
        
    def pieces(self) -> int:
        return (self.pawns +
                self.knights +
                self.bishops +
                self.rooks +
                self.queens +
                self.kings)
    
    def points(self) -> int:
        return ((self.pawns * Pawn.points) +
                (self.knights * Knight.points) + 
                (self.bishops * Bishop.points) +
                (self.rooks * Rook.points) +
                (self.queens * Queen.points) +
                (self.kings) * King.points)