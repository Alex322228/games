import pygame
import pers

pygame.init()
win = pygame.display.set_mode((1100,600))
pygame.display.set_caption("stepik")
bg = pygame.image.load('image/bg2.jpg')
playerStand = pygame.image.load('image/right_1.png')
trap = pygame.image.load('image/trap.png')

clock= pygame.time.Clock()

x = pers.x
y = pers.y
width = pers.width
height = pers.height
speed = pers.speed

Jump = False
JumpCount = 10

left = False
right = False
animation = 0

def drawWindow():
    global animation
    global x, y
    win.blit(bg, (0, 0))
    if animation + 1>=30:
        animation = 0
    if left:
        win.blit(pers.walkLeft[animation // 5], (x, y))
        animation += 1
    elif right:
        win.blit(pers.walkRight[animation // 5], (x, y))
        animation += 1
    else:
        win.blit(playerStand, (x, y))  
    pygame.display.update()

run  = True

while run:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 10:
        x -= speed
        left = True
        right = False
    elif keys[pygame.K_RIGHT] and x < 1100 - width - 5:
        x += speed
        left = False
        right = True
    else:
        left = False
        right = False
        animation = 0
    if not(Jump): 
        # if keys[pygame.K_UP] and y > 5: это читы
        #     y -= speed
        # if keys[pygame.K_DOWN] and y < 500 - height - 5:
        #     y += speed
        if keys[pygame.K_SPACE]:
            Jump = True
    else:
        if JumpCount >= -10:
            if JumpCount < 0:
                y += (JumpCount**2) / 2 
            else:
                y -= (JumpCount**2) / 2  
            JumpCount -=1
        else:
            Jump = False
            JumpCount = 10
    drawWindow()
pygame.quit()