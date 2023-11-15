"""
UNT Computer Science Club: Intro to Pygame Workshop
11/15/2023

Variable names and code structure have been simplified to be coded quickly along with a presenter.
Better variable names and designs do exist.
For instance, we could put the colors in a dictionary so we don't have to remember their indexes.
There might be too many ungrouped globals. We could make a character class to hold the variables.
Nevertheless, Secret Square lives on with this new upgrade. Will it ever reach 1 million downloads? You decide...
"""

from random import choice, randint
import pygame
pygame.init()
pygame.font.init()

# set window
screenWidth = 500
screenHeight = 500
window = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Secret Square")

# colors (red, green, blue, yellow)
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0)]

# character
squareSize = 20
xpos = 10
ypos = (screenHeight / 2) - (squareSize / 2)
vel = 5
color = colors[0]
collide = False
win = False
border = False

"""
This function fills the map with colorful obstacles!
Obstacles can be placed between 70 and 430 pixels
We are appending a list to represent a Pygame Rect and its color (random)
rect[0] = rect dimensions and rect[1] = rect color
Pygame Rect is (left, ypos, width, height)
Each obstacle will have a space of charSize + 7 between them and must be at least charSize / 2 wide
"""
rects = []
def make_obstacles(charSize):
    start = 70
    end = 430
    minWidth = charSize // 2
    prevColor = color
    currColor = None
    x = start
    while x < end:
        while currColor := choice(colors):
            if currColor != prevColor:
                break
        width = randint(minWidth, 100)
        if x + width > end:
            width = 100
        rects.append([(x, 0, width, screenHeight), currColor])
        prevColor = currColor
        x += width + charSize + 7

make_obstacles(squareSize)

# winning zone
winZone = (450, 0, 50, screenHeight)

# font
font = pygame.font.SysFont('Comic Sans MS', 60)
winningText = font.render('YOU WIN', False, (255, 255, 0))
text_rect = winningText.get_rect(center=(screenWidth / 2, screenHeight / 2))

# main pygame loop
spacePressed = False
run = True
while run:
    pygame.time.delay(25)
    keys = pygame.key.get_pressed()
    character = pygame.Rect(xpos, ypos, squareSize, squareSize)

    # check for collisions
    for rect in rects:
        if character.colliderect(rect[0]):
            if color == rect[1]:
                border = True
                collide = False
            else:
                collide = True
                border = False

    # check for win
    if character.colliderect(winZone):
        win = True
    
    # change colors
    # red
    if keys[pygame.K_r]:
        color = colors[0]
    # green
    if keys[pygame.K_g]:
        color = colors[1]
    # blue
    if keys[pygame.K_b]:
        color = colors[2]
    # yellow
    if keys[pygame.K_y]:
        color = colors[3]

    # move character
    if keys[pygame.K_UP] and ypos > 0:
        ypos -= vel

    if keys[pygame.K_DOWN] and ypos < screenHeight - squareSize:
        ypos += vel
    
    if keys[pygame.K_LEFT] and xpos > 0 and not collide:
        xpos -= vel

    if keys[pygame.K_RIGHT] and xpos < screenWidth - squareSize and not collide:
        xpos += vel

    # let the user restart if they won
    if keys[pygame.K_SPACE] and win and not spacePressed:
        spacePressed = True
        win = False
        collide = False
        squareSize = randint(5, 50)
        rects.clear()
        make_obstacles(squareSize)
        xpos = 10
        ypos = (screenHeight / 2) - (squareSize / 2)
    elif not keys[pygame.K_SPACE]:
        spacePressed = False  

    # check for quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 

    # draw to window
    window.fill((0,0,0))
    pygame.draw.rect(window, color, character, 0)
    if win:
        window.blit(winningText, text_rect)
    else:
        for rect in rects:
            pygame.draw.rect(window, rect[1], rect[0])
        if border:
            pygame.draw.rect(window, (0,0,0), character, 1)

    pygame.display.update()

pygame.quit()