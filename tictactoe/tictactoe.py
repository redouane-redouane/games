import pygame

WINDOW_HEIGHT = 760
WINDOW_WIDTH = 480
BACKGROUND_COLOR = "black"

SQUARE_COLOR = "gray"
SQUARE_WIDTH = 100
SQUARE_HEIGHT = 100

CROSS_COLOR = "red"
CIRCLE_COLOR = "blue"

pygame.init()
screen = pygame.display.set_mode((WINDOW_HEIGHT, WINDOW_WIDTH))
clock = pygame.time.Clock()
running = True

screen.fill(BACKGROUND_COLOR) # fill the screen with a color to wipe away anything from last frame
matrix = [[pygame.draw.rect(screen, SQUARE_COLOR, pygame.Rect(100 + col * (SQUARE_WIDTH + 10), 100 + row * (SQUARE_HEIGHT + 10), SQUARE_WIDTH, SQUARE_HEIGHT)) for col in range(3)] for row in range(3)]
turn = 0
win = False
matrix_g = [[-1,-1,-1],[-1,-1,-1],[-1,-1,-1]]

def check_for_win():
    win_x_row_1 = (matrix_g[0][0] == 1 and matrix_g[0][1] == 1 and matrix_g[0][2] == 1)
    win_x_row_2 = (matrix_g[1][0] == 1 and matrix_g[1][1] == 1 and matrix_g[1][2] == 1)
    win_x_row_3 = (matrix_g[2][0] == 1 and matrix_g[2][1] == 1 and matrix_g[2][2] == 1)
    win_x_col_1 = (matrix_g[0][0] == 1 and matrix_g[1][0] == 1 and matrix_g[2][0] == 1)
    win_x_col_2 = (matrix_g[0][1] == 1 and matrix_g[1][1] == 1 and matrix_g[2][1] == 1)
    win_x_col_3 = (matrix_g[0][2] == 1 and matrix_g[1][2] == 1 and matrix_g[2][2] == 1)
    win_x_diag_1 = (matrix_g[0][0] == 1 and matrix_g[1][1] == 1 and matrix_g[2][2] == 1)
    win_x_diag_2 = (matrix_g[0][2] == 1 and matrix_g[1][1] == 1 and matrix_g[2][0] == 1)

    win_o_row_1 = (matrix_g[0][0] == 0 and matrix_g[0][1] == 0 and matrix_g[0][2] == 0)
    win_o_row_2 = (matrix_g[1][0] == 0 and matrix_g[1][1] == 0 and matrix_g[1][2] == 0)
    win_o_row_3 = (matrix_g[2][0] == 0 and matrix_g[2][1] == 0 and matrix_g[2][2] == 0)
    win_o_col_1 = (matrix_g[0][0] == 0 and matrix_g[1][0] == 0 and matrix_g[2][0] == 0)
    win_o_col_2 = (matrix_g[0][1] == 0 and matrix_g[1][1] == 0 and matrix_g[2][1] == 0)
    win_o_col_3 = (matrix_g[0][2] == 0 and matrix_g[1][2] == 0 and matrix_g[2][2] == 0)
    win_o_diag_1 = (matrix_g[0][0] == 0 and matrix_g[1][1] == 0 and matrix_g[2][2] == 0)
    win_o_diag_2 = (matrix_g[0][2] == 0 and matrix_g[1][1] == 0 and matrix_g[2][0] == 0)

    global win 
    if win_x_row_1 or win_x_row_2 or win_x_row_3 or win_x_col_1 or win_x_col_2 or win_x_col_3 or win_x_diag_1 or win_x_diag_2:
        pygame.draw.line(screen, CROSS_COLOR, (0,0), (WINDOW_HEIGHT,WINDOW_WIDTH), 7)
        pygame.draw.line(screen, CROSS_COLOR, (0,WINDOW_WIDTH), (WINDOW_HEIGHT,0), 7)
        win = True
    elif win_o_row_1 or win_o_row_2 or win_o_row_3 or win_o_col_1 or win_o_col_2 or win_o_col_3 or win_o_diag_1 or win_o_diag_2:
        pygame.draw.circle(screen, CIRCLE_COLOR, (WINDOW_HEIGHT / 2, WINDOW_WIDTH / 2), 200, 5)
        win = True

while running:    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # The user clicked X to close the window
            running = False
        if (event.type == pygame.MOUSEBUTTONDOWN) and (win == False):
            print(win)
            for row in range(3):
                for col in range(3):
                    if matrix[row][col].collidepoint(pygame.mouse.get_pos()):
                        if turn == 0 and matrix_g[row][col] == -1:
                            pygame.draw.circle(screen, CIRCLE_COLOR, matrix[row][col].center, 30, 5)
                            matrix_g[row][col] = 0
                            check_for_win()
                            turn = 1
                        elif turn == 1 and matrix_g[row][col] == -1:
                            pygame.draw.line(screen, CROSS_COLOR, (matrix[row][col].topright[0] - 20, matrix[row][col].topright[1] + 20), (matrix[row][col].bottomleft[0] + 20, matrix[row][col].bottomleft[1] - 20), 7)
                            pygame.draw.line(screen, CROSS_COLOR, (matrix[row][col].topleft[0] + 20, matrix[row][col].topleft[1] + 20), (matrix[row][col].bottomright[0] - 20, matrix[row][col].bottomright[1] - 20), 7)
                            matrix_g[row][col] = 1
                            check_for_win()
                            turn = 0

    pygame.display.flip() # flip() the display to put your work on screen

pygame.quit()