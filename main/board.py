import pygame 
from main.pieces import *
class board:

    def __init__(self, surface, side, length):
        self.surface = surface
        self.side = side
        self.length = length
        self.positions = [int(i*self.length/8) for i in range(8)]
        self.draw_board()
        self.draw_numbers()
        bis = pygame.image.load("assets/Chess_wq.png")
        self.surface.blit(bis,(23,23))

    def draw(self, brd):
        self.draw_board()
        self.draw_numbers()
        for i in brd:
            for j in i:
                if j == "":
                    continue
                self.surface.blit(j.img,(23+(self.length/8)*j.square[0],23+(self.length/8)*j.square[1]))


    def draw_board(self):
        pygame.draw.rect(self.surface, 'blue', rect = (23,23, self.length+4, self.length+4))
        for i in range(8):
            for j in range(8):
                if (i+j)%2 == 0:
                    colour = "white"
                else:
                    colour = "navy"
                pygame.draw.rect(self.surface, colour, rect = (25+self.positions[i],25+self.positions[j], self.length/8, self.length/8))  

    def draw_numbers(self):
        nums = ["1.","2.","3.","4.","5.","6.","7.","8."]
        letters = ["a.","b.","c.","d.","e.","f.","g.","h."]
        if self.side == "white":
            nums.reverse()
        elif self.side == "black":
            letters.reverse()
        number_font = pygame.font.SysFont( None, 16 )
        nums_2draw = [number_font.render( i, True, 'black', 'gray') for i in nums]
        letters_2draw = [number_font.render( i, True, 'black', 'gray') for i in letters]
            
        for i,char_img in enumerate(nums_2draw):
            self.surface.blit(char_img, (10,30+i*self.length/8))
        for i,char_img in enumerate(letters_2draw):
            self.surface.blit(char_img, (55+i*self.length/8,30+self.length))

    


        
