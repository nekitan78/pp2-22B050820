import pygame
import os

pygame.init()

#set size

width = 600
height = 500

x = width/2
y = height/2

fps = 60
#set display
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("BAll")


def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        global x,y
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and y - 25 > 0:
            y -= 20
        if keys[pygame.K_DOWN] and y + 25 < height:
            y += 20
        if keys[pygame.K_RIGHT] and x + 25 < width:
            x += 20
        if keys[pygame.K_LEFT] and x - 25 > 0:
            x -= 20

        win.fill((255,255,255))
        pygame.draw.circle(win, (255,0,0), (x, y), 25)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()


main()