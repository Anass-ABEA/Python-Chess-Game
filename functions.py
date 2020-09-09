import pygame

def surroundings(window):
    pygame.draw.rect(window,(100,100,100),(0,0,800,50))
    pygame.draw.rect(window, (100, 100, 100), (600, 50, 50, 800))
    pygame.draw.rect(window, (255, 255, 255), (0, 48, 650, 4))
    pygame.draw.rect(window, (255, 255, 255), (0, 348, 650, 4))


def drawboard(window):
    for j in range (8):
        for i in range (0,8,2):
            if (j%2==0):
                pygame.draw.rect(window, (200, 100, 0), (75*i, 50+75*j, 75, 75))
                pygame.draw.rect(window, (250, 200, 150), ((i+1) * 75, 50+75*j, 75, 75))
            else:
                pygame.draw.rect(window, (200, 100, 0), (75 * (i + 1), 50+75*j, 75, 75))
                pygame.draw.rect(window, (250, 200, 150), ( i* 75, 50+75*j, 75, 75))