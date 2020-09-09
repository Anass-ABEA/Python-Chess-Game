import pygame
from functions import *
pygame.init()

window = pygame.display.set_mode((650,650))
pygame.display.set_caption("Chess Game")

gamestart = True
surroundings(window)
while gamestart:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gamestart = False

    drawboard(window)
    pygame.display.update()

