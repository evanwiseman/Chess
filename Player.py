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
        return ((self.pawns * Pawn.value) +
                (self.knights * Knight.value) + 
                (self.bishops * Bishop.value) +
                (self.rooks * Rook.value) +
                (self.queens * Queen.value) +
                (self.kings) * King.value)