# Assets: https://techwithtim.net/wp-content/uploads/2020/09/assets.zip
import pygame
from checkers.constants import OFFSET, WIDTH, HEIGHT, SQUARE_SIZE, RED, WHITE
from checkers.game import Game
from minimax.algorithm import minimax

FPS = 60

#main game loop
WIN = pygame.display.set_mode((WIDTH+OFFSET*2, HEIGHT+OFFSET*2))
pygame.display.set_caption('Checkers')


class NegMouse(Exception):
    pass

#returns what rows or column we are in based on 
#the mouse position
def get_row_col_from_mouse(pos):
    x, y = pos
    row = (y-OFFSET) // SQUARE_SIZE
    col = (x-OFFSET) // SQUARE_SIZE
    return row, col


def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)

    while run:
        clock.tick(FPS)

        if game.turn == WHITE:
            value, new_board = minimax(game.get_board(), 4, WHITE, game)
            game.ai_move(new_board)

        if game.winner() != None:
            print(game.winner())
            run = False
        #check for any events happening
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                try:
                    pos = pygame.mouse.get_pos()
                    if (pos[0] < OFFSET or pos[0] > (WIDTH+OFFSET) or pos[1] < OFFSET or pos[1] > (HEIGHT+OFFSET)):
                        raise NegMouse()
                    row, col = get_row_col_from_mouse(pos)
                    game.select(row, col)
                except NegMouse:
                    print("Negative val")

        game.update()

    pygame.quit()


main()
