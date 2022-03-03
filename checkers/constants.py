import pygame

OFFSET = 80
WIDTH, HEIGHT = 640, 640
ROWS, COLS = 8, 8

#size of each square on the board
SQUARE_SIZE = WIDTH//COLS

# rgb
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREY = (128, 128, 128)
BROWN = (139, 69, 19)

PIECE_SIZE = 60
WHITE_PIECE = pygame.transform.scale(
    pygame.image.load('assets/whitePiece.png'), (PIECE_SIZE, PIECE_SIZE))
BLACK_PIECE = pygame.transform.scale(
    pygame.image.load('assets/blackPiece.png'), (PIECE_SIZE, PIECE_SIZE))
CROWN = pygame.transform.scale(pygame.image.load(
    'assets/crown.png'), (PIECE_SIZE*0.7, PIECE_SIZE*0.7))
BOARD = pygame.transform.scale(
    pygame.image.load('assets/board.png'), (800, 800))
