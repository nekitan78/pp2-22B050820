import pygame
import random
from pygame.locals import *
import sys

pygame.init()


#set size of the screen
height = 625
width = 625

sizeBlock = 30

font = pygame.font.Font(pygame.font.get_default_font(), sizeBlock*2)



#sert fps/ speed of the game

fps = 10
speed = 2


#making screen

def drawField():
    for x in range(0, width, sizeBlock):
        for y in range(0, height, sizeBlock):
            rect = pygame.Rect(x, y, sizeBlock, sizeBlock)
            pygame.draw.rect(win, pygame.Color('white') , rect , 1)

win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake")

runing = True

clock = pygame.time.Clock()

class Snake:
    

    def __init__(self):
        self.x, self.y = sizeBlock, sizeBlock
        self.xdir = 1
        self.ydir = 0
        self.head = pygame.Rect(self.x, self.y, sizeBlock, sizeBlock)
        self.body = [pygame.Rect(self.x - sizeBlock, self.y, sizeBlock, sizeBlock)]
        self.dead = False

    def update(self):

        

        global apple, fps
        for square in self.body:
            if self.head.x == square.x and self.head.y == square.y:
                self.dead = True
                break
            if self.head.x not in range(0, width) or self.head.y not in range(0, height):
                self.dead = True
                break
                
        
        if self.dead:
            self.x, self.y = sizeBlock, sizeBlock
            self.head = pygame.Rect(self.x, self.y, sizeBlock, sizeBlock)
            self.body = [pygame.Rect(self.x - sizeBlock, self.y, sizeBlock, sizeBlock)]
            self.xdir = 1
            self.ydir = 0
            self.dead = False
            apple = Apple()
            fps = 10



        self.body.append(self.head)
        for i in range(len(self.body)-1):
            self.body[i].x, self.body[i].y = self.body[i+1].x, self.body[i+1].y
        self.head.x += self.xdir * sizeBlock
        self.head.y += self.ydir * sizeBlock
        self.body.remove(self.head)

class Apple:

    def __init__(self):
        self.x = int(random.randint(0, width)/sizeBlock)*sizeBlock
        self.y = int(random.randint(0, height)/sizeBlock)*sizeBlock
        self.rect = pygame.Rect(self.x, self.y, sizeBlock, sizeBlock)
    
    def update(self):
        pygame.draw.rect(win, "red", self.rect)

score = font.render("1", True, "white")
level = font.render("1", True, "white")
scoreRect = score.get_rect(center=(width/2, height/20))
levelRect = level.get_rect(center=(20, height/20))


drawField()


snake = Snake()
apple = Apple()
while runing:

    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                snake.xdir = 0
                snake.ydir = 1
            elif event.key == pygame.K_UP:
                snake.xdir = 0
                snake.ydir = -1
            elif event.key == pygame.K_RIGHT:
                snake.xdir = 1
                snake.ydir = 0
            elif event.key == pygame.K_LEFT:
                snake.xdir = -1
                snake.ydir = 0
        
    snake.update()
    win.fill('black')
    drawField()

    apple.update()
    
    levelN = int((len(snake.body) + 1)/5)

    fps = 8 + (fps + levelN) / 5

    score = font.render(f"{len(snake.body) + 1}", True, "white")
    level = font.render(f"Level {levelN}", True, "white")
        
    pygame.draw.rect(win, pygame.Color('green'), snake.head)
    for square in snake.body:
        pygame.draw.rect(win, pygame.Color('green'), square)

    win.blit(score, scoreRect)
    win.blit(level, levelRect)
    
    if snake.head.x == apple.x and snake.head.y == apple.y:
        snake.body.append(pygame.Rect(square.x, square.y, sizeBlock, sizeBlock))
        apple = Apple()
        
        
    clock.tick(fps)
    pygame.display.update()



