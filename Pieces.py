class Piece:
    name = ""
    notation = ""
    value = 0
    location = ("", 0)
    
    def __init__(self):
        super().__init__()
        
        return
    
    def __str__(self) -> str:
        return self.name

class King(Piece):
    name = "King"
    notation = "K"
    value = 0
    
    def __init__(self) -> None:
        super().__init__()
        
        return    
    
class Queen(Piece):
    name = "Queen"
    notation = "Q"
    value = 9
        
    def __init__(self):
        super().__init__()
        
        return
    
class Rook(Piece):
    name = "Rook"
    notation = "R"
    value = 5
    
    def __init__(self):
        super().__init__()
                
        return
    
class Bishop(Piece):
    name = "Bishop"
    notation = "B"
    value = 3
    
    def __init__(self):
        super().__init__()
        return
    
class Knight(Piece):
    name = "Knight"
    notation = "N"
    value = 3
    
    def __init__(self):
        super().__init__()
        
        return

class Pawn(Piece):
    name = "Pawn"
    notation = "P"
    value = 1
    
    def __init__(self):
        super().__init__()
        
        return