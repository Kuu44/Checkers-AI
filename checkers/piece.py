from .constants import RED, WHITE, SQUARE_SIZE, GREY, CROWN, OFFSET, WHITE_PIECE, BLACK_PIECE, PIECE_SIZE
import pygame


class Piece:
    PADDING = 10
    OUTLINE = 2

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.king = False
        self.x = 0
        self.y = 0
        self.calc_pos()

    def calc_pos(self):
        #to draw the pieces from the center of the square
        #this sets the position as center of the square
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    def make_king(self):
        self.king = True

    def draw(self, win):
        radius = SQUARE_SIZE//2 - self.PADDING
        correctionFactor = OFFSET-PIECE_SIZE//2
        pygame.draw.circle(
            win, GREY, (self.x+OFFSET+self.OUTLINE, self.y+OFFSET+self.OUTLINE), radius)
        if self.color == WHITE:
            win.blit(WHITE_PIECE, (self.x+correctionFactor,
                     self.y+correctionFactor))
        else:
            win.blit(BLACK_PIECE, (self.x+correctionFactor,
                     self.y+correctionFactor))
        # pygame.draw.circle(
        #     win, self.color, (self.x+OFFSET, self.y+OFFSET), radius)
        if self.king:
            win.blit(CROWN, (self.x - CROWN.get_width() //
                             2+OFFSET, self.y - CROWN.get_height()*0.6+OFFSET))

    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_pos()


    '''
    THis function is used to create a string representation of the object.
    '''
    def __repr__(self):
        return str(self.color)
