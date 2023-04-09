import pygame
import os

width = 600
height = 500

fps = 60

win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Mouse")

MICK = pygame.image.load('mickeyclock.jpeg')
mick = pygame.transform.scale(MICK, (width, height))

def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        win.fill((255, 255, 255))
        win.blit(mick, (0, 0))
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()