import pygame

from pygame.locals import *
import random


pygame.init()

height = 500
width = 500

speed = 2
score = 0
gameover = False

leftLane = 150
midLane = 250
rigthLane = 350
lanes = [leftLane, midLane, rigthLane]

laneMoveY = 0


win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Car racing")

running = True

clock = pygame.time.Clock()
fps = 120

class Vehicle(pygame.sprite.Sprite):

    def __init__(self, image, x, y):
        pygame.sprite.Sprite.__init__(self)

        imageScale = 100 / image.get_rect().width
        newWidth = image.get_rect().width * imageScale
        newHeight = image.get_rect().height * imageScale
        self.image = pygame.transform.scale(image, (newWidth, newHeight))

        self.rect = self.image.get_rect()
        self.rect.center = [x,y]

class PlayersVehicle(Vehicle):
    def __init__(self, x, y):
        image = pygame.image.load("car.png")
        super().__init__(image, x, y)

playerX = 250
playerY = 400

player_group = pygame.sprite.Group()

player = PlayersVehicle(playerX, playerY)
player_group.add(player)

vehicle_group = pygame.sprite.Group()


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and player.rect.center[0] < rigthLane:
                player.rect.x += 100
            if event.key == pygame.K_LEFT and player.rect.center[0] > leftLane:
                player.rect.x -= 100

            for vehicle in vehicle_group:
                if pygame.sprite.collide_rect(player, vehicle):
                    gameover = True

                    if event.key == pygame.K_LEFT:
                        player.rect.left = vehicle.rect.right
                    elif event.key == pygame.K_RIGHT:
                        player.rect.right = vehicle.rect.left

    

    win.fill((76,208,56))

    #draw marks
    pygame.draw.rect(win, (125,125,125), (100, 0, 300, height))
    pygame.draw.rect(win, (255, 232, 0), (95, 0, 15, height))
    pygame.draw.rect(win, (255, 232, 0), (395, 0, 15, height))

    laneMoveY += speed * 2
    if laneMoveY >= 50 * 2:
        laneMoveY = 0

    for y in range(-2 * 50, height, 50 * 2):
        pygame.draw.rect(win, (255,255,255), (45 + leftLane, y + laneMoveY, 15, 50))
        pygame.draw.rect(win, (255,255,255), (45 + midLane, y + laneMoveY, 15, 50))
    
    player_group.draw(win)

    addVehicle = True

    for vehicle in vehicle_group:
        if vehicle.rect.top < vehicle.rect.height * 1.5:
            addVehicle = False
    
    if addVehicle:
        lane = random.choice(lanes)

        image = pygame.image.load("carvec.png")

        vehicle = Vehicle(image, lane, height/-2)
        vehicle_group.add(vehicle)
    
    for vehicle in vehicle_group:
            
        vehicle.rect.y += speed

        if vehicle.rect.top >= height:
            vehicle.kill()

            score += 1

            if score > 0 and score % 5 == 0:
                speed +=1 

    vehicle_group.draw(win)

    font = pygame.font.Font(pygame.font.get_default_font(), 16)
    text = font.render('Score ' + str(score), True, (0,0,0))
    textRect = text.get_rect()
    textRect.center = (50, 400)
    win.blit(text, textRect)

    if pygame.sprite.spritecollide(player, vehicle_group, True):
        gameover = True

    if gameover:
        pygame.draw.rect(win, (255,0,0), (0,50,width,100))

        font = pygame.font.Font(pygame.font.get_default_font(), 16)
        text = font.render('Game over. Play again? (Enter Y or N)', True, (0,0,0))
        textRect = text.get_rect()
        textRect.center = (width/2, 100)
        win.blit(text, textRect)

    pygame.display.update()

    while gameover:
        clock.tick(fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameover = False
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_y:
                    gameover = False
                    speed = 2
                    score = 0
                    vehicle_group.empty()
                    player.rect.center = [playerX, playerY]
                elif event.key == pygame.K_n:
                    gameover = False
                    running = False

    

    
    clock.tick(fps)
pygame.quit()
        
    