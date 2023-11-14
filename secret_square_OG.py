"""
UNT Computer Science Club: Intro To Pygame Workshop
4/some Wednesday/2023

The original Secret Square code. 'Classic Mode,' if you will, for the true gamers.
"""


import pygame
pygame.init()
pygame.font.init()

#screen
screenWidth = 500
screenHeight = 500
win = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Secret Square")

#character
width = 50
height = 50
xPos = 10
yPos = (screenHeight / 2) - (height / 2)
vel = 5

#colors
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]
color = colors[1]

#blocks
#blue
blueRectangle = (112, 0, 20, screenHeight)
#red
redRectangle = (225, 0, 20, screenHeight)
#green
greenRectangle = (367, 0, 20, screenHeight)
#winZone
winZone = (437, 0, 67, screenHeight)

#collisions
collide = False
winningCollision = False

#font
font = pygame.font.SysFont('Comic Sans MS', 30)
winningText = font.render('YOU WIN', False, (255, 255, 0))

#main pygame loop
run = True
while run:
    pygame.time.delay(25)

    keys = pygame.key.get_pressed()

    character = pygame.Rect(xPos, yPos, width, height)

    if character.colliderect(blueRectangle):
        if color == colors[2]:
            collide = False
        else:
            collide = True
    
    if character.colliderect(redRectangle): 
        if color == colors[0]:
            collide = False
        else:
            collide = True
    
    if character.colliderect(greenRectangle):
        if color == colors[1]:
            collide = False
        else:
            collide = True

    if character.colliderect(winZone):
        winningCollision = True
    
    #red
    if keys[pygame.K_r]:
        color = colors[0]

    #green
    if keys[pygame.K_g]:
        color = colors[1]

    #blue
    if keys[pygame.K_b]:
        color = colors[2]

    #movement
    if keys[pygame.K_UP] and yPos > 0:
        yPos -= vel

    if keys[pygame.K_DOWN] and yPos < screenHeight - height:
        yPos += vel
    
    if keys[pygame.K_LEFT] and xPos > 0 and not collide:
        xPos -= vel

    if keys[pygame.K_RIGHT] and xPos < screenWidth - width and not collide:
        xPos += vel

    
    #check for quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           run = False 

    #draw to window
    win.fill((0,0,0))
    pygame.draw.rect(win, color, character)

    if winningCollision:
        win.blit(winningText, (200, 200))
    else:
        pygame.draw.rect(win, colors[2], blueRectangle)
        pygame.draw.rect(win, colors[0], redRectangle)
        pygame.draw.rect(win, colors[1], greenRectangle)


    pygame.display.update()

pygame.quit()