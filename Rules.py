from enum import Enum, auto

class DirectionalRules:
    def __init__(
        self,
        horizontal: bool = False,
        vertical: bool = False,
        diagonal: bool = False,
        l_shape = False,
    ) -> None:
        super().__init__()
        
        self.horizontal = horizontal
        self.vertical = vertical
        self.diagonal = diagonal
        self.l_shape = l_shape
        
        return
    
    def __str__(self) -> str:        
        return (("horizontal = " + str(self.horizontal)) + "\n" +
                ("vertical = " + str(self.vertical)) + "\n" +
                ("diagonal = " + str(self.diagonal)) + "\n" +
                ("l_shape = " + str(self.l_shape)))

class MovementRules:
    def __init__(
        self,
        min_spaces: int = 0,
        max_spaces: int = 0,
    ) -> None: 
        self.min_spaces = min_spaces
        self.max_spaces = max_spaces
        
        return
    
    def __str__(self) -> str:
        return (("min_spaces = " + str(self.min_spaces)) + "\n" +
                ("max_spaces = " + str(self.max_spaces)))
    
class SpecialRules:
    def __init__(
        self,
        en_passant: bool = False,
        double_move: bool = False,
        castling: bool = False
    ) -> None: 
        self.en_passant = en_passant
        self.double_move = double_move
        self.castling = castling
        
        return
    
    def __str__(self) -> str:
        return (("en_passant = " + str(self.en_passant)) + "\n" +
                ("double_move = " + str(self.double_move)) + "\n" +
                ("castling = " + str(self.castling)))
