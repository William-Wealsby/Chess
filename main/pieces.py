import pygame

class pieces:
    def __init__(self, colour, square = [0,0]):
        self.square = square
        self.colour = colour
        self.value = int
        self.img = pygame.image.load("assets/Chess_wp.png")

    def moves(self, side, board = None):
        return []

    def move_to(self, new_square):
        self.square = new_square 

#wQueen = pygame.image.load("assets/Chess_wq")

class pawn(pieces):
    def __init__(self, colour, square):
        super().__init__(colour, square)
        self.value = 1
        if self.colour == "white":
            self.img = pygame.image.load("assets/Chess_wp.png")
        else: 
            self.img = pygame.image.load("assets/Chess_bp.png")

    def moves(self, side, brd):
        squares = []
        if side == self.colour:
            if brd[self.square[1]-1][self.square[0]] == "":
                squares.append([self.square[0],self.square[1]-1])
                if self.square[1] == 6 and brd[4][self.square[0]] == "":  
                    squares.append([self.square[0], 4])
            if self.square[0]+1<=7 and brd[self.square[1]-1][self.square[0]+1] != "" and brd[self.square[1]-1][self.square[0]+1].colour != self.colour:
                squares.append([self.square[0]+1,self.square[1]-1])
            if self.square[0]-1>=0 and brd[self.square[1]-1][self.square[0]-1] != "" and brd[self.square[1]-1][self.square[0]-1].colour != self.colour:
                squares.append([self.square[0]-1,self.square[1]-1])
        else:
            if brd[self.square[1]+1][self.square[0]] == "":
                squares.append([self.square[0],self.square[1]+1])
            if self.square[1] == 1: 
                if brd[3][self.square[0]] == "":
                    squares.append([self.square[0], 3])
            if self.square[0]+1<=7 and brd[self.square[1]+1][self.square[0]+1] != "" and brd[self.square[1]+1][self.square[0]+1].colour != self.colour:
                squares.append([self.square[0]+1,self.square[1]+1])
            if self.square[0]-1>=0 and brd[self.square[1]+1][self.square[0]-1] != "" and brd[self.square[1]+1][self.square[0]-1].colour != self.colour:
                squares.append([self.square[0]-1,self.square[1]+1])

        
        return squares

    
class bishop(pieces):
    def __init__(self, colour, square):
        super().__init__(colour, square)
        self.value = 3
        if self.colour == "white":
            self.img = pygame.image.load("assets/Chess_wb.png")
        else: 
            self.img = pygame.image.load("assets/Chess_bb.png")


class knight(pieces):
    def __init__(self, colour, square):
        super().__init__(colour, square)
        self.value = 3
        if self.colour == "white":
            self.img = pygame.image.load("assets/Chess_wn.png")
        else: 
            self.img = pygame.image.load("assets/Chess_bn.png")


class rook(pieces):
    def __init__(self, colour, square):
        super().__init__(colour, square)
        self.value = 5
        if self.colour == "white":
            self.img = pygame.image.load("assets/Chess_wr.png")
        else: 
            self.img = pygame.image.load("assets/Chess_br.png")

class queen(pieces):
    def __init__(self, colour, square):
        super().__init__(colour, square)
        self.value = 9
        if self.colour == "white":
            self.img = pygame.image.load("assets/Chess_wq.png")
        else: 
            self.img = pygame.image.load("assets/Chess_bq.png")


class king(pieces):
    def __init__(self, colour, square):
        super().__init__(colour, square)
        self.value = 100
        if self.colour == "white":
            self.img = pygame.image.load("assets/Chess_wk.png")
        else: 
            self.img = pygame.image.load("assets/Chess_bk.png")

    def pos_moves(self, brd):
        moves=[]
        for i in [-1, 0, 1]:
            for j in [-1, 0 ,1]:
                moves.append([self.square[0]+i, self.square[1]+j])
        moves.remove(self.square)
        return moves
    
    def moves(self, side, brd):
        movelist=[]
        moves = self.pos_moves(brd)
        for move in moves:
            if move[0]<0 or move[0]>7 or move[1]<0 or move[1]>7:
                continue
            if brd[move[1]][move[0]] == "":
                movelist.append(move) 
            elif brd[move[1]][move[0]].colour != self.colour:
                movelist.append(move)
        return movelist
