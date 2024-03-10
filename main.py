import pygame as pg
from pygame.locals import *
import random

WIDTH, HEIGHT = (900, 900)
BG = (255, 255, 255)
BOARD_COLOR = (255, 0, 0)
EMPTY_BOX = pg.image.load("Empty.png")
X_BOX = pg.image.load("X.png")
O_BOX = pg.image.load("Circles.png")

pg.init()
pg.font.init()
pg.display.set_caption("Tic Tac Toe")

class Box(pg.sprite.Sprite):
    def __init__(self, x, y, status="empty"):
        super().__init__()
        self.status = status
        self.image = EMPTY_BOX
        self.image = pg.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y

    def clicked(self, turn):
        if turn == "X" and self.status == "empty":
            self.image = X_BOX
            self.image = pg.transform.scale(self.image, (100, 100))
            self.status = "X"
        elif turn == "O" and self.status == "empty":
            self.image = O_BOX
            self.image = pg.transform.scale(self.image, (100, 100))
            self.status = "O"

board = [[None for _ in range(3)] for _ in range(3)] 

def create_grid ():
    x = WIDTH//2 - 100
    y = 150
    # do we need both the array and the sprite group???
    # add to board 2d array
    for i in range (3):
        for j in range (3):
            b = Box(x, y)
            board[i][j] = b
            x += 100
        x = WIDTH//2 - 100
        y += 100
    # add to sprite group
    for r in board:
        for c in r:
            spaces.add(c)

screen = pg.display.set_mode([WIDTH, HEIGHT])
spaces = pg.sprite.Group()

create_grid()
player_turn = random.choice(["X", "O"])

font = pg.font.Font('freesansbold.ttf', 32)
text = font.render("It's player " + player_turn + "'s turn.", True, (0,0,0))
textRect = text.get_rect()
textRect.centerx = WIDTH//2
textRect.centery = HEIGHT - 300

running = True
while running:
    text = font.render("It's player " + player_turn + "'s turn", True, (0,0,0))

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        if event.type == pg.MOUSEBUTTONDOWN:
            mouseX, mouseY = pg.mouse.get_pos()
            # check if one of the boxes was clicked
            for i in spaces:
                if i.rect.collidepoint(mouseX, mouseY):
                    i.clicked(player_turn)
                    # change turn
                    if i.status == "X":
                        player_turn = "O"
                    elif i.status == "O":
                        player_turn = "X"
    
    screen.fill(BG)
    spaces.draw(screen)
    screen.blit(text, textRect)
    pg.display.flip()

pg.quit()