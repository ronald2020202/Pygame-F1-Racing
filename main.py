import pygame
import random
import math
import time
pygame.font.init()
pygame.init()
width, height = (500, 500)
screen = pygame.display.set_mode((width, height))
screen.fill((160, 160, 160))
on = True

car_x = 225
car_y = 390
CAR_L = 100
CAR_W = 50
LIVES = 3
frames = 0

#obstacle_L =
right = False
left = False
up = False
down = False

beginning = False
collision = False

counter = 0
SCORE = 0
HIGHSCORE = 0

spawnx = [0, 25, 125, 225, 325, 425]


pygame.draw.rect(screen, (0,0,0), (car_x, car_y, CAR_W, CAR_L))

obs_list = []

class obstacle:
    y = 0
    x = 0
    length = 100
    width = 50
    def __init__(self, lane):
        self.y = -100
        self.x = spawnx[random.randint(1, 5)]
        #self.length = 50
        #self.width = 100

    def getY():
        return self.y

    def setY(newVal):
        self.y = newVal
       
pygame.display.set_caption("F1 Racing")

font1 = pygame.font.SysFont("freesanbold.ttf", 50)
font2 = pygame.font.SysFont("freesanbold.ttf", 50)
font3 = pygame.font.SysFont("freesanbold.ttf", 70)


while True:
    frames += 1
    if frames % 100 == 0:
        if beginning:
            SCORE += 1
    #text1 = font1.render("Lives: " + str(LIVES), True, (0, 0, 0), (160, 160, 160))
    #textRect = text1.get_rect()
    #textRect.center = (400, 50)

    #text2 = font2.render("Score: " + str(SCORE), True, (0, 0, 0), (160, 160, 160))
    #textRect1 = text2.get_rect()
    #textRect1.center = (125, 50)
    if LIVES < 1:
        if SCORE > HIGHSCORE:
            text3 = font3.render("New High Score: " + str(SCORE), True, (0, 0, 0), (160, 160, 160))
            textRect2 = text3.get_rect()
            textRect2.center = (250, 250)
            screen.blit(text3, textRect2)
            HIGHSCORE = SCORE
            pygame.display.update()
        time.sleep(3)
        LIVES = 3
        car_x = 225
        car_y = 390
        CAR_L = 100
        CAR_W = 50
        SCORE = 0
        obs_list = []
        beginning = False
        frames = 0
    screen.fill((160, 160, 160))
    pygame.draw.rect(screen, (250,250,25), (95, 0, 5, 500))
    pygame.draw.rect(screen, (250,250,25), (195, 0, 5, 500))
    pygame.draw.rect(screen, (250,250,25), (295, 0, 5, 500))
    pygame.draw.rect(screen, (250,250,25), (395, 0, 5, 500))

    #o1 = obstacle(random.randint(1, 5))

    if collision:
        counter += 1
    if counter == 350:
        collision = False

    chance = random.random()
    if chance < 0.005 and len(obs_list) < 5:
        o2 = obstacle(random.randint(1, 5))
        obs_list.append(o2)

    i = 0
    length = len(obs_list)
    while i < length:
        if obs_list[i].y > 500:
            del obs_list[i]
            length -= 1
            i -= 1
        else:
             obs_list[i].y += 0.8 + 0.00002 * frames
             pygame.draw.rect(screen, (0,0,255), (obs_list[i].x, obs_list[i].y, obs_list[i].width, obs_list[i].length))
             #check if this obstacle(obs_list[i]) is overlapping with the car
             obsminx = obs_list[i].x
             obsmaxx = obs_list[i].x + obs_list[i].width
             obsminy = obs_list[i].y
             obsmaxy = obs_list[i].y + obs_list[i].length
             if beginning and collision == False:
                 if (car_x >= obsminx and car_x <= obsmaxx) or (car_x + CAR_W >= obsminx and car_x + CAR_W <= obsmaxx):
                     if (car_y >= obsminy and car_y <= obsmaxy) or (car_y + CAR_L >= obsminy and car_y + CAR_L <= obsmaxy):
                         LIVES -= 1
                         collision = True
                         counter = 0
        i += 1
   
    for event in pygame.event.get():
            if event.type == pygame.QUIT: #stop the program if the player quits
                on = False
               
            #if event.type == pygame.MOUSEBUTTONDOWN:
            #    continue
            #if event.type == pygame.MOUSEBUTTONUP:
            #    screen.fill((255, 0, 0))
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    right = True
                if event.key == pygame.K_LEFT:
                    left = True
                if event.key == pygame.K_UP:
                    up = True
                if event.key == pygame.K_DOWN:
                    down = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    right = False
                if event.key == pygame.K_LEFT:
                    left = False
                if event.key == pygame.K_UP:
                    up = False
                if event.key == pygame.K_DOWN:
                    down = False
           
    if right == True:
        beginning = True
        delta = min(450-car_x, 0.5)
        car_x += delta
    if left == True:
        beginning = True
        delta = min(car_x, 0.5)
        car_x -= delta
    if up == True:
        beginning = True
        delta = min(car_y, 0.5)
        car_y -= delta
    if down == True:
        beginning = True
        delta = min(400-car_y, 0.5)
        car_y += delta

    pygame.draw.rect(screen, (0,0,0), (car_x, car_y, CAR_W, CAR_L))

    if beginning == False:
        text4 = font3.render("F1 Racing", True, (0, 0, 0), (160, 160, 160))
        textRect3 = text4.get_rect()
        textRect3.center = (250, 250)
        screen.blit(text4, textRect3)
    else:
        text1 = font1.render("Lives: " + str(LIVES), True, (0, 0, 0), (160, 160, 160))
        textRect = text1.get_rect()
        textRect.center = (400, 50)
        screen.blit(text1, textRect)
        text2 = font2.render("Score: " + str(SCORE), True, (0, 0, 0), (160, 160, 160))
        textRect1 = text2.get_rect()
        textRect1.center = (125, 50)
        screen.blit(text2, textRect1)
    pygame.display.update()
