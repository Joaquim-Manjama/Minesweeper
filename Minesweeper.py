import pygame, sys
import random as r
import os

pygame.init()

#WINDOW DIMENSIONS
WIDTH = 540
HEIGHT = 500
TAB_HEIGHT = 80
CELL = 30

#COLOURS
TAB_GREEN = (74,117,44)
LIGHT_GREEN = (170,215,81)
DARK_GREEN = (162,209,73)
SELECTED_GREEN = (185,221,119)
LIGHT_BROWN = (229,194,159)
DARK_BROWN = (215,184,153)

#SCREEN
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("JmD's Minesweeper")
current_path = os.path.dirname(os.path.abspath(__file__))

#GRAPHICS
flag_image = pygame.image.load(current_path+"\\FLAG.png")
big_flag_image = pygame.transform.scale(flag_image, (40, 40))
small_flag_image = pygame.transform.scale(flag_image, (20, 20))
clock_image = pygame.image.load(current_path+"\\CLOCK.png") 
clock_image = pygame.transform.scale(clock_image, (40, 45))



#SOUND
sound1 = pygame.mixer.Sound(current_path+"\\Sound\\1.wav")
sound2 = pygame.mixer.Sound(current_path+"\\Sound\\2.wav")
sound3 = pygame.mixer.Sound(current_path+"\\Sound\\3.wav")
sound4 = pygame.mixer.Sound(current_path+"\\Sound\\4.wav")
sound5 = pygame.mixer.Sound(current_path+"\\Sound\\5.wav")
sound6 = pygame.mixer.Sound(current_path+"\\Sound\\6.wav")
sound7 = pygame.mixer.Sound(current_path+"\\Sound\\7.wav")
sound8 = pygame.mixer.Sound(current_path+"\\Sound\\8.wav")
sound_crack = pygame.mixer.Sound(current_path+"\\Sound\\crack.wav")
sound_flag_out = pygame.mixer.Sound(current_path+"\\Sound\\flag_out.wav")
sound_flag_in = pygame.mixer.Sound(current_path+"\\Sound\\flag_in.wav")
sound_win = pygame.mixer.Sound(current_path+"\\Sound\\win.wav")

#GAME VARIABLES
gameOver = False
clicked = False
clock = pygame.time.Clock()
time_frame = 0
time = 0
start = False
board = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

flag_board = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

num_board = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

num_bombs = 30

def draw_board(surface, f, c):
    global num_bombs
    surface.fill(LIGHT_GREEN)
    tab = pygame.Rect(0, 0, 540, 80)
    pygame.draw.rect(surface, TAB_GREEN, tab)
    draw_image(surface, f, 175, 20)
    draw_image(surface, c, 300, 18)
    font = pygame.font.SysFont('Comis Sans MS', 40)
    flag_count = font.render(f"{num_bombs}", False, 'white')
    surface.blit(flag_count, (220, 30))

    
    for rows in range(0, 14):
        for cols in range(0, 18):
            if rows % 2 == 0:
                if cols % 2 != 0:
                    cell = pygame.Rect(cols*CELL, rows*CELL + TAB_HEIGHT , CELL, CELL)
                    pygame.draw.rect(surface, DARK_GREEN, cell)
            else:
                if cols % 2 == 0:
                    cell = pygame.Rect(cols*CELL, rows*CELL + TAB_HEIGHT , CELL, CELL)
                    pygame.draw.rect(surface, DARK_GREEN, cell)

def draw_image(surface, img, x, y):
    surface.blit(img, (x, y))

def generate_bombs(b, nb, x, y):
    xpos = x
    ypos = y
    for i in range(0, nb):
        y = r.randint(0, 13)
        x = r.randint(0, 17)
        if r.random() <= 0.2 and b[y][x] != 10 and b[y][x] != -1 and y != ypos and x != xpos:
            b[y][x] = 10
            nb -= 1
        else:
            generate_bombs(b, nb, xpos, ypos)
            return

def colour_selected_squares(surface):
    x, y = pygame.mouse.get_pos()
    if y > TAB_HEIGHT:
        x = int(x / CELL)
        y = int((y - TAB_HEIGHT) / CELL)
        cell = pygame.Rect((x * CELL), ((y * CELL) + TAB_HEIGHT), CELL, CELL)
        pygame.draw.rect(surface, SELECTED_GREEN, cell)

def draw_flags(surface, sf, fb):
    y = 0
    for i in fb:
        x = 0
        for j in i:
            if fb[y][x] == 1:
                draw_image(surface, sf, ((x * CELL) + 5) , ((y * CELL) + TAB_HEIGHT + 5))
            x += 1
        y += 1

def draw_bottom_board(surface, b, fb):
    for rows in range(0, 14):
        for cols in range(0, 18):
            if b[rows][cols] == -1:
                cell = pygame.Rect(cols*CELL, rows*CELL + TAB_HEIGHT , CELL, CELL)
                pygame.draw.rect(surface, LIGHT_BROWN, cell)
                if rows % 2 == 0:
                    if cols % 2 != 0:
                        cell = pygame.Rect(cols*CELL, rows*CELL + TAB_HEIGHT , CELL, CELL)
                        pygame.draw.rect(surface, DARK_BROWN, cell)
                else:
                    if cols % 2 == 0:
                        cell = pygame.Rect(cols*CELL, rows*CELL + TAB_HEIGHT , CELL, CELL)
                        pygame.draw.rect(surface, DARK_BROWN, cell)

def calculate_help_numbers(b, nb):
#CORNERS
    #TOP LEFT
    acc = 0
    if b[0][1] == 10:
        acc += 1
    if b[1][0] == 10:
        acc += 1
    if b[1][1] == 10:
        acc += 1
    nb[0][0] = acc

    #BOTTOM LEFT
    acc = 0
    if b[13][1] == 10:
        acc += 1
    if b[12][1] == 10:
        acc += 1
    if b[12][0] == 10:
        acc += 1
    nb[13][0] = acc

    #BOTTOM RIGHT
    acc = 0
    if b[12][16] == 10:
        acc += 1
    if b[13][16] == 10:
        acc += 1
    if b[12][17] == 10:
        acc += 1
    nb[13][17] = acc

#SIDES
    #LEFT
    for i in range(1, 13):
        acc = 0
        if b[i - 1][0] == 10:
            acc += 1
        if b[i - 1][1] == 10:
            acc += 1
        if b[i][1] == 10:
            acc += 1
        if b[i + 1][1] == 10:
            acc += 1
        if b[i + 1][0] == 10:
            acc += 1
        nb[i][0] = acc
    #RIGHT
    for i in range(1, 13):
        acc = 0
        if b[i - 1][17] == 10:
            acc += 1
        if b[i - 1][16] == 10:
            acc += 1
        if b[i][16] == 10:
            acc += 1
        if b[i + 1][16] == 10:
            acc += 1
        if b[i + 1][17] == 10:
            acc += 1
        nb[i][17] = acc
    #UP
    for i in range(1, 17):
        acc = 0
        if b[0][i - 1] == 10:
            acc += 1
        if b[1][i - 1] == 10:
            acc += 1
        if b[1][i] == 10:
            acc += 1
        if b[1][i + 1] == 10:
            acc += 1
        if b[0][i + 1] == 10:
            acc += 1
        nb[0][i] =  acc

    #BOTTOM
    for i in range(1, 17):
        acc = 0
        if b[13][i - 1] == 10:
            acc += 1
        if b[12][i - 1] == 10:
            acc += 1
        if b[12][i] == 10:
            acc += 1
        if b[12][i + 1] == 10:
            acc += 1
        if b[13][i + 1] == 10:
            acc += 1
        nb[13][i] =  acc
    
#MIDDLE
    #MIDDLE
    for i in range(1, 13):
        for j in range(1, 17):
            acc = 0
            if b[i - 1][j - 1] == 10:
                acc += 1
            if b[i - 1][j] == 10:
                acc += 1
            if b[i - 1][j + 1] == 10:
                acc += 1
            if b[i][j - 1] == 10:
                acc += 1
            if b[i][j + 1] == 10:
                acc += 1
            if b[i + 1][j - 1] == 10:
                acc += 1
            if b[i + 1][j] == 10:
                acc += 1
            if b[i + 1][j + 1] == 10:
                acc += 1
            nb[i][j] = acc

def draw_numbers(surface, b, nb):
    y = 0
    for i in nb:
        x = 0
        for j in i:
            if b[y][x] == -1 and nb[y][x] != 0:
                font = pygame.font.SysFont('Comis Sans MS', 30)
                number = font.render(f"{j}", False, 'black')
                surface.blit(number, ((x * CELL) + 10, (y * CELL) + TAB_HEIGHT + 5))
            x += 1
        y += 1

def game_over(surface, b, fb):
    y = 0
    for i in b:
        x = 0
        for j in i:
            if b[y][x] == 10 and fb[y][x] == 0:
                cell = pygame.Rect(x *CELL, y *CELL + TAB_HEIGHT , CELL, CELL)
                pygame.draw.rect(surface, 'black', cell)
            x += 1
        y += 1

def crack_up(b, nb, fb, x, y):
    #UP
    if nb[y][x] == 0 and y > 0:
        if b[y - 1][x] == 0 and fb[y - 1][x] == 0:
            b[y - 1][x] = -1
            if nb[y - 1][x] != 0:
                return
            else:
                crack_left(b, nb, fb, x, y - 1)
                crack_right(b, nb, fb, x, y - 1)
                crack_up(b, nb, fb, x, y - 1)
            
        else:
            return

def crack_down(b, nb, fb, x, y):
    #DOWN
    if nb[y][x] == 0 and y < 13: 
        if b[y + 1][x] == 0 and fb[y + 1][x] == 0:
            b[y + 1][x] = -1
            if nb[y + 1][x] != 0:
                return
            else:
                crack_left(b, nb, fb, x, y + 1)
                crack_right(b, nb, fb, x, y + 1)
                crack_down(b, nb, fb, x, y + 1)
        else:
            return

def crack_left(b, nb, fb, x, y):
    #LEFT
    if nb[y][x] == 0 and x > 0:
        if b[y][x - 1] == 0 and fb[y][x - 1] == 0:
            b[y][x - 1] = -1
            if nb[y][x - 1] != 0:
                return
            else: 
                crack_up(b, nb, fb, x - 1, y)
                crack_down(b, nb, fb, x - 1, y)
                crack_left(b, nb, fb, x - 1, y)
        else:
            return

def crack_right(b, nb, fb, x, y):
    #RIGHT
    if nb[y][x] == 0 and x < 16:
        if b[y][x + 1] == 0 and fb[y][x + 1] == 0:
            b[y][x + 1] = -1
            if nb[y][x + 1] != 0:
                return
            else:
                crack_up(b, nb, fb, x + 1, y)
                crack_down(b, nb, fb, x + 1, y)
                crack_right(b, nb, fb, x + 1, y)
        else:
            return

def crack(b, nb, fb, x, y):
    global gameOver
    global start
    global num_bombs
    if not start:
        generate_bombs(board, num_bombs, x, y)
        calculate_help_numbers(board, nb)
        if nb[y][x] != 0:
            crack(b, nb, fb, x, y)
            return
        start = True

    if b[y][x] == 0:

        if nb[y][x] == 1:
            sound1.play()
        elif nb[y][x] == 2:
            sound2.play()
        elif nb[y][x] == 3:
            sound3.play()
        elif nb[y][x] == 4:
            sound4.play()
        elif nb[y][x] == 5:
            sound5.play()
        elif nb[y][x] == 6:
            sound6.play()
        elif nb[y][x] == 7:
            sound7.play()
        elif nb[y][x] == 8:
            sound8.play()
        else:
            sound_crack.play()

        #CRACK
        b[y][x] = -1

        crack_up(b, nb, fb, x, y)
        crack_down(b, nb, fb, x, y)
        crack_left(b, nb, fb, x, y)
        crack_right(b, nb, fb, x, y)
        

    elif b[y][x] == 10 and fb[y][x] == 0:
        game_over(screen, b, fb)
        gameOver = True
        return
    
def display_time(surface, t):
    font = pygame.font.SysFont('Comis Sans MS', 35)
    number = font.render(f"{t}", False, 'white')
    surface.blit(number, (350, 33))

def detect_win(b, fb):
    y = 0
    for i in b:
        x = 0
        for j in i:
            if j == 0:
                return False
            if j == 10:
                if fb[y][x] != 1:
                    return False
            x += 1
        y += 1
    return True

while True:
    if clicked == True:
        time_frame += 1
        if time_frame % 30 == 0:
            time += 1
    if not gameOver:
        draw_board(screen, big_flag_image, clock_image)
        display_time(screen, time)
        colour_selected_squares(screen)
        draw_bottom_board(screen, board, flag_board)
        draw_numbers(screen, board, num_board)
        draw_flags(screen, small_flag_image, flag_board)

    if gameOver:
        time_frame = 0
        if time_frame % 240 == 0:
            font = pygame.font.SysFont('Comis Sans MS', 70)
            txt = font.render(f"GAME OVER!", False, 'white')
            screen.blit(txt, (120, 250))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            clicked = True
            xpos, ypos = pygame.mouse.get_pos()
            if ypos > TAB_HEIGHT:
                xpos = int(xpos / CELL)
                ypos = int((ypos - TAB_HEIGHT) / CELL)
                if event.button == 1 and flag_board[ypos][xpos] == 0:
                    crack(board, num_board, flag_board, xpos, ypos)   
                elif event.button == 3:
                    if board[ypos][xpos] != -1 and flag_board[ypos][xpos] == 0 and num_bombs > 0:
                        flag_board[ypos][xpos] = 1
                        sound_flag_in.play()
                        num_bombs -= 1
                    elif flag_board[ypos][xpos] == 1:
                        flag_board[ypos][xpos] = 0
                        sound_flag_out.play()
                        num_bombs += 1

    if detect_win(board, flag_board):
        time_frame = 0
        if time_frame % 240 == 0:
            sound_win.play()
            font = pygame.font.SysFont('Comis Sans MS', 70)
            txt = font.render(f"YOU WIN!", False, 'white')
            screen.blit(txt, (120, 250))
            gameOver = False

    clock.tick(30)
    pygame.display.update()