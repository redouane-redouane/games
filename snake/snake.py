import pygame
import random

WINDOW_HEIGHT = 760
WINDOW_WIDTH = 480
BACKGROUND_COLOR = "black"
SQUARE_HEIGHT = 5
SQUARE_WIDTH = 5
SQUARE_COLOR = "red"
SNAKE_COLOR = "blue"

pygame.init()
screen = pygame.display.set_mode((WINDOW_HEIGHT, WINDOW_WIDTH))
clock = pygame.time.Clock()
running = True

screen.fill(BACKGROUND_COLOR) # fill the screen with a color to wipe away anything from last frame

while running:    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # The user clicked X to close the window
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(screen,SQUARE_COLOR,pygame.Rect(random.randint(0, WINDOW_HEIGHT), random.randint(0, WINDOW_WIDTH),SQUARE_WIDTH,SQUARE_HEIGHT))

    pygame.display.flip() # flip() the display to put your work on screen

pygame.quit()