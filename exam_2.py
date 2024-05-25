class Piece:
    def __init__(self, color, position):
        self.color = color
        self.position = position


class Pawn(Piece):
    def move(self):
        print("Я ПІШАК.", "Пішак може рухатись вперед на одну клітинку, або на дві клітинки, якщо це є його перший хід."
                          "Він може атакувати фігури на діагоналі вперед на одну клітинку. ")


class Rook(Piece):
    def move(self):
        print("Я ЛАДЬЯ.", "Ладья може рухатись горизонтально або вертикально на будь-яку кількість вільних клітинок. ")


class Knight(Piece):
    def move(self):
        print("Я КІНЬ.", " Кінь рухається L-подібно: дві клітинки вертикально або горизонтально, "
                         "а потім одну клітинку в бік. ")


class Bishop(Piece):
    def move(self):
        print("Я СЛОН.", " Слон може рухатись по діагоналі на будь-яку кількість вільних клітинок.")


class Queen(Piece):
    def move(self):
        print("Я ФЕРЗЬ.", "Ферзь може рухатись горизонтально, вертикально або "
                          "по діагоналі на будь-яку кількість вільних клітинок. ")


class King(Piece):
    def move(self):
        print("Я КОРОЛЬ.", "Король може рухатись на одну клітинку в будь-якому напрямку. ")


pawn_1 = Pawn('white', "A3")
pawn_1.move()
rook_1 = Rook("black", "D4")
rook_1.move()
knight_1 = Knight("black", "C2")
knight_1.move()
bishop_1 = Bishop("white", "F7")
bishop_1.move()
queen_1 = Queen("white", "E1")
queen_1.move()
king_1 = King("black", "A5")
king_1.move()
