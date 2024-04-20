import pygame as pg
from pygame.locals import *
import random
import numpy as np
import time as t

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
    def __init__(self, x, y, row, col,  status="empty"):
        super().__init__()
        self.status = status
        self.image = EMPTY_BOX
        self.image = pg.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y

        self.row = row
        self.col = col

    def clicked(self, turn):
        if turn == "X" and self.status == "empty":
            self.image = X_BOX
            self.image = pg.transform.scale(self.image, (100, 100))
            self.status = "X"
        elif turn == "O" and self.status == "empty":
            self.image = O_BOX
            self.image = pg.transform.scale(self.image, (100, 100))
            self.status = "O"

x = WIDTH//2 - 100
y = 150           
board = np.array([[Box(x + j * 100, y + i * 100, i, j) for j in range(3)] for i in range(3)], dtype=Box)

player_turn = random.choice(["X", "O"])
font = pg.font.Font('freesansbold.ttf', 32)
text = font.render("It's player " + player_turn + "'s turn.", True, (0,0,0))
textRect = text.get_rect()
textRect.centerx = WIDTH//2
textRect.centery = HEIGHT - 300

def check_row (row):
    val = board[row][0].status
    for c in board[row]:
        if c.status != val:
            return False
    return True

def check_col (col):
    cols = [board[row][col] for row in range (3)]
    val = cols[0].status
    for r in cols:
        if r.status != val:
            return False
    return True

def check_diags(row, col):
    val = board[row][col].status
    x, y = 0, 0
    while x < 3 and y < 3:
        cur = board[x][y]
        if cur.status != val:
            return False
        x += 1 
        y += 1
    return True


screen = pg.display.set_mode([WIDTH, HEIGHT])
spaces = pg.sprite.Group()
# def game_won(winner):
#     font = pg.font.Font('freesansbold.ttf', 32)
#     win_text = font.render("Player " + winner + " won!", True, (0, 0, 0))
#     win_textRect = win_text.get_rect()
#     win_textRect.centerx = WIDTH//2
#     win_textRect.centery = HEIGHT - 300
#     screen.blit(win_text, win_textRect)
#     pg.display.flip()
#     print("win")

winner = False
running = True
while running:
    text = font.render("It's player " + player_turn + "'s turn", True, (0,0,0))

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        if event.type == pg.MOUSEBUTTONDOWN:
            mouseX, mouseY = pg.mouse.get_pos()
            for row in board:
                for item in row:
                    if item.rect.collidepoint(mouseX, mouseY) and winner == False: 
                        item.clicked(player_turn)
                        # change turn
                        if item.status == "X":
                            player_turn = "O"
                        elif item.status == "O":
                            player_turn = "X"

                        if check_row(item.row) or check_col(item.col) or check_diags(item.row, item.col):
                            win_text = font.render("Player " + player_turn + " won!", True, (0, 0, 0))
                            win_textRect = win_text.get_rect()
                            win_textRect.centerx = WIDTH//2
                            win_textRect.centery = HEIGHT - 300
                            # screen.blit(win_text, win_textRect)
                            winner = True
                            print("win")

    screen.fill(BG)
    # draw board
    for row in board:
        for i in row:
            screen.blit(i.image, i.rect)
    if winner == False:
        screen.blit(text, textRect)
    else:
        screen.blit(win_text, win_textRect)
    pg.display.flip()

pg.quit()
