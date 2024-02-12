from Rules import PieceRules

class Piece:
    name: str = ""
    notation: str = ""
    value: int = 0
    pieceRules: PieceRules = None
    
    def __init__(self) -> None:
        super().__init__()
        
        return
    
    def __str__(self) -> str:
        return self.name
    
    def printInfo(self) -> None:
        print("name=" + self.name)
        print("notation=" + self.notation)
        print("value=" + str(self.value))
        self.pieceRules.printRules()
        print("")
        
        return

class King(Piece):
    name = "King"
    notation = "K"
    value = 0
    pieceRules = PieceRules(
        horizontal=True,
        vertical=True,
        diagonal=True,
        l_shape=False,
        min_spaces=1,
        max_spaces=1
    )
    
    def __init__(self) -> None:
        super().__init__()
    
        return    
    
class Queen(Piece):
    name = "Queen"
    notation = "Q"
    value = 9
    pieceRules = PieceRules(
        horizontal=True,
        vertical=True,
        diagonal=True,
        l_shape=False,
        min_spaces=1,
        max_spaces=8
    )
        
    def __init__(self) -> None:
        super().__init__()
        
        return
    
class Rook(Piece):
    name = "Rook"
    notation = "R"
    value = 5
    pieceRules = PieceRules(
        horizontal=True,
        vertical=True,
        diagonal=False,
        l_shape=False,
        min_spaces=1,
        max_spaces=8
    )
    
    def __init__(self) -> None:
        super().__init__()
                
        return
    
class Bishop(Piece):
    name = "Bishop"
    notation = "B"
    value = 3
    pieceRules = PieceRules(
        horizontal=False,
        vertical=False,
        diagonal=True,
        l_shape=False,
        min_spaces=1,
        max_spaces=8
    )
    
    def __init__(self) -> None:
        super().__init__()
        return
    
class Knight(Piece):
    name = "Knight"
    notation = "N"
    value = 3
    pieceRules = PieceRules(
        horizontal=False,
        vertical=False,
        diagonal=False,
        l_shape=True,
        min_spaces=1,
        max_spaces=1
    )
    
    def __init__(self) -> None:
        super().__init__()
        
        return

class Pawn(Piece):
    name = "Pawn"
    notation = "P"
    value = 1
    pieceRules = PieceRules(
        horizontal=False,
        vertical=True,
        diagonal=True,
        l_shape=False,
        min_spaces=1,
        max_spaces=2
    )
    
    def __init__(self) -> None:
        super().__init__()
        
        return
    
if __name__ == "__main__":
    king = King()
    queen = Queen()
    rook = Rook()
    bishop = Bishop()
    knight = Knight()
    pawn = Pawn()
    
    king.printInfo()
    queen.printInfo()
    rook.printInfo()
    bishop.printInfo()
    knight.printInfo()
    pawn.printInfo()