import pygame 
from math import floor
from main.board import board
from main.pieces import *

def switch_turn(turn):
    print(f"turn switch was {turn}")
    if turn == "white":
        turn = "black"
    else: 
        turn = "white"
    return turn

def Pos2Squareid(mouse_pos):
    square = []
    square.append(floor((mouse_pos[0]-25)*(8/450)))
    square.append(floor((mouse_pos[1]-25)*(8/450)))
    if square[0] >= 0 and square[0] <=7 and square[1] >= 0 and square[1] <= 7:
        return square 
    else:
        return False
    
def movepiece(brd, square1, square2):
    brd[square2[1]][square2[0]] = brd[square1[1]][square1[0]]
    brd[square1[1]][square1[0]] = ""
    return brd

class start_game:
    def __init__(self,side,name):
        pygame.init()
        if name == "No Engine":
            pygame.display.set_caption("Chess: No Engine")
        else:
            pygame.display.set_caption(f"Chess vs {name}")
        self.icon = pygame.image.load('assets/icon.png')
        pygame.display.set_icon(self.icon)
        self.screen = pygame.display.set_mode((800,600))  
        self.clock = pygame.time.Clock()
        self.running = True
        moves = []
        turn = "white"
        game = board(self.screen, side, 450)
        if side == "white":
            brd = [[rook("black",[0,0]),knight("black",[1,0]),bishop("black",[2,0]),king("black",[3,0]),queen("black",[4,0]),bishop("black",[5,0]),knight("black",[6,0]),rook("black",[7,0])],
                   [pawn("black",[0,1]),pawn("black",[1,1]),pawn("black",[2,1]),pawn("black",[3,1]),pawn("black",[4,1]),pawn("black",[5,1]),pawn("black",[6,1]),pawn("black",[7,1])],
                   ["","","","","","","",""],
                   ["","","","","","","",""],
                   ["","","","","","","",""],
                   ["","","","","","","",""],
                   [pawn("white",[0,6]),pawn("white",[1,6]),pawn("white",[2,6]),pawn("white",[3,6]),pawn("white",[4,6]),pawn("white",[5,6]),pawn("white",[6,6]),pawn("white",[7,6])],
                   [rook("white",[0,7]),knight("white",[1,7]),bishop("white",[2,7]),king("white",[3,7]),queen("white",[4,7]),bishop("white",[5,7]),knight("white",[6,7]),rook("white",[7,7])]]
        elif side == "black":
            brd = [[rook("white",[0,0]),knight("white",[1,0]),bishop("white",[2,0]),king("white",[3,0]),queen("white",[4,0]),bishop("white",[5,0]),knight("white",[6,0]),rook("white",[7,0])],
                   [pawn("white",[0,1]),pawn("white",[1,1]),pawn("white",[2,1]),pawn("white",[3,1]),pawn("white",[4,1]),pawn("white",[5,1]),pawn("white",[6,1]),pawn("white",[7,1])],
                   ["","","","","","","",""],
                   ["","","","","","","",""],
                   ["","","","","","","",""],
                   ["","","","","","","",""],
                   [pawn("black",[0,6]),pawn("black",[1,6]),pawn("black",[2,6]),pawn("black",[3,6]),pawn("black",[4,6]),pawn("black",[5,6]),pawn("black",[6,6]),pawn("black",[7,6])],
                   [rook("black",[0,7]),knight("black",[1,7]),bishop("black",[2,7]),king("black",[3,7]),queen("black",[4,7]),bishop("black",[5,7]),knight("black",[6,7]),rook("black",[7,7])]]

        while self.running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    index = Pos2Squareid(list(pygame.mouse.get_pos()))
                    if index:
                        print(f"piece on {brd[index[1]][index[0]]}")
                        if brd[index[1]][index[0]] != "":
                            moves = brd[index[1]][index[0]].moves(side,brd)
                            print(f"moves are {moves}")
                            piece = index
                if event.type == pygame.MOUSEBUTTONUP:
                    index = Pos2Squareid(list(pygame.mouse.get_pos()))
                    if index == False or brd[piece[1]][piece[0]] == "":
                        continue
                    if brd[piece[1]][piece[0]].colour == side or name == "No Engine":
                        allowed = True
                    else: 
                        allowed = False
                    if allowed and index in moves and turn == brd[piece[1]][piece[0]].colour:
                        brd[piece[1]][piece[0]].move_to(index)
                        brd = movepiece(brd, piece, index)
                        turn = switch_turn(turn)

                        
                    
            self.screen.fill('grey')
            game.draw(brd)
            pygame.draw.rect(self.screen, "white", rect = (550,23,200,500))

            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()

        
    



