from Rules import DirectionalRules, MovementRules, SpecialRules

class Piece:
    name: str = ""
    notation: str = ""
    points: int = 0
    moved: bool = False
    direction_rules: DirectionalRules = DirectionalRules()
    movement_rules: MovementRules = MovementRules()
    special_rules: SpecialRules = SpecialRules()
    
    def __init__(self) -> None:
        super().__init__()
        
        return
    
    def __str__(self) -> str:
        return self.name
    
    def print_info(self) -> None:
        print("name = " + self.name)
        print("notation = " + self.notation)
        print("value = " + str(self.points))
        print("direction_rules = {\n" + str(self.direction_rules) + "\n}")
        print("movement_rules = {\n" + str(self.movement_rules) + "\n}")
        print("special_rules = {\n" + str(self.special_rules) + "\n}")
        print()
        
        return

class King(Piece):
    name = "King"
    notation = "K"
    points = 0
    direction_rules = DirectionalRules(
        horizontal = True,
        vertical = True,
        diagonal = True,
        l_shape = True
    )
    movement_rules = MovementRules(
        min_spaces=1,
        max_spaces=1
    )
    special_rules = SpecialRules(
        en_passant=False,
        double_move=False,
        castling=True
    )
    
    def __init__(self) -> None:
        super().__init__()
        
        return    
    
class Queen(Piece):
    name = "Queen"
    notation = "Q"
    points = 9
    direction_rules = DirectionalRules(
        horizontal=True,
        vertical=True,
        diagonal=True,
        l_shape=False,
    )
    movement_rules = MovementRules(
        min_spaces=1,
        max_spaces=8
    )
    special_rules = SpecialRules(
        en_passant=False,
        double_move=False,
        castling=False
    )
        
    def __init__(self) -> None:
        super().__init__()
        
        return
    
class Rook(Piece):
    name = "Rook"
    notation = "R"
    points = 5
    direction_rules = DirectionalRules(
        horizontal=True,
        vertical=True,
        diagonal=False,
        l_shape=False,
    )
    movement_rules = MovementRules(
        min_spaces=1,
        max_spaces=8
    )
    special_rules = SpecialRules(
        en_passant=False,
        double_move=False,
        castling=False
    )
    
    def __init__(self) -> None:
        super().__init__()
                
        return
    
class Bishop(Piece):
    name = "Bishop"
    notation = "B"
    points = 3
    direction_rules = DirectionalRules(
        horizontal=False,
        vertical=False,
        diagonal=True,
        l_shape=False,
    )
    movement_rules = MovementRules(
        min_spaces=1,
        max_spaces=8
    )
    special_rules = SpecialRules(
        en_passant=False,
        double_move=False,
        castling=False
    )
    
    def __init__(self) -> None:
        super().__init__()
        return
    
class Knight(Piece):
    name = "Knight"
    notation = "N"
    points = 3
    direction_rules = DirectionalRules(
        horizontal=False,
        vertical=False,
        diagonal=False,
        l_shape=True,
    )
    movement_rules = MovementRules(
        min_spaces=1,
        max_spaces=8
    )
    special_rules = SpecialRules(
        en_passant=False,
        double_move=False,
        castling=False
    )
    
    def __init__(self) -> None:
        super().__init__()
        
        return

class Pawn(Piece):
    name = "Pawn"
    notation = "P"
    points = 1
    direction_rules = DirectionalRules(
        horizontal=False,
        vertical=True,
        diagonal=True,
        l_shape=False,
    )
    movement_rules = MovementRules(
        min_spaces=1,
        max_spaces=1
    )
    special_rules = SpecialRules(
        en_passant=True,
        double_move=True,
        castling=False
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
    
    king.print_info()
    queen.print_info()
    rook.print_info()
    bishop.print_info()
    knight.print_info()
    pawn.print_info()