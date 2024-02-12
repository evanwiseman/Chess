from enum import Enum, auto

class PieceRules:
    def __init__(
        self,
        horizontal: bool = False,
        vertical: bool = False,
        diagonal: bool = False,
        l_shape = False,
        min_spaces: int = 0,
        max_spaces: int = 0,
        en_passant: bool = False,
        double_move: bool = False,
        castling: bool = False
    ) -> None:
        super().__init__()
        
        self.horizontal = horizontal
        self.vertical = vertical
        self.diagonal = diagonal
        self.l_shape = l_shape
        self.min_spaces = min_spaces
        self.max_spaces = max_spaces
        self.en_passant = en_passant
        self.double_move = double_move
        self.castling = castling
        
        return
    
    def printRules(self) -> None:
        print("horizontal=" + str(self.horizontal))
        print("vertical=" + str(self.vertical))
        print("diagonal=" + str(self.diagonal))
        print("l_shape=" + str(self.l_shape))
        print("min_spaces=" + str(self.min_spaces))
        print("max_spaces=" + str(self.max_spaces))
        print("en_passant=" + str(self.en_passant))
        print("double_move=" + str(self.double_move))
        print("castling=" + str(self.castling))
        
        return
        
class GameRules:
    def __init(self) -> None:
        super().__init__()
        
        return