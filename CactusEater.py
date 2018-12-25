"""
Converted spaceman into a sprite and added enemy sprites
Keeping score of collisions
"""

import pygame
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (5, 5, 250)
PURPLE = (144, 5, 250)
YELLOW = (242, 250, 5)
ORANGE = (250, 136, 5)
BROWNISH_GREY = (110,106,105)
GREY_BUILDING = (196,189,187)
DARK_GREY1=(145,153,156)
ALIEN_GREEN=(23, 191,65)
SPACE_SUIT=(213, 219, 214)

colors=(PURPLE, WHITE, YELLOW, ORANGE)

PI = 3.141592653

pygame.init()

# Set the width and height of the screen [width, height]
size = (900, 800)
screen = pygame.display.set_mode(size)

earth_background = pygame.image.load("EarthBackground.png").convert()
y = -3450 #canvas height is 4525
screen.blit(earth_background, [0,y]) #background image

pygame.display.set_caption("Bring Spaceman Home!")

'''
def write(msg="yo"):
    myfont = pygame.font.SysFont("None", 32)
    mytext = myfont.render(msg, True, (0,0,0))
    mytext = mytext.convert_alpha()
    return mytext
'''

class Spaceman(pygame.sprite.Sprite):
    '''
    This class represents the astronaut character
    '''

    def __init__(self):
        super().__init__() # Call the parent class (Sprite) constructor
 
        self.image = pygame.image.load("spaceman.png").convert()
        self.image.set_colorkey(GREY_BUILDING)
        
        self.rect = self.image.get_rect()
        self.rect.x = 500
        self.rect.y = 470

        self.radius = 0
        
    def move(self):
        '''
        move spaceman with keys and sets boundaries for where he can move
        '''
        dist = 25 # distance moved in 1 frame
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.rect.x -= dist
                elif event.key == pygame.K_RIGHT:
                    self.rect.x += dist

        #boundaries        
        if self.rect.x > 800:
            self.rect.x = 800
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.y > 470:
            self.rect.y = 470

class Cactusman(pygame.sprite.Sprite):
    '''
    This class represents the cactus enemy character
    '''
    #cactusmen = []
    #number = 0
    def __init__(self):
        super().__init__() # Call the parent class (Sprite) constructor
 
        self.image = pygame.image.load("CactusMan.png").convert_alpha()
        self.rect = self.image.get_rect()

    def update(self):
        if y==0: #screen height
            self.rect.y +=0
        else:
            self.rect.y += 1
            if self.rect.y > 4325:
                self.rect.y = random.randrange(-500, -10)
                self.rect.x = random.randrange(0, 900)



allsprites = pygame.sprite.Group()
cactusmen = pygame.sprite.Group()
player = Spaceman()
allsprites.add(player, cactusmen)

for i in range(50):
    # This represents a block
    enemy = Cactusman()
 
    # Set a random location for the block
    enemy.rect.x = random.randrange(0,900)
    enemy.rect.y = random.randrange(0, 4525)
 
    # Add the block to the list of objects
    cactusmen.add(enemy)
    allsprites.add(enemy)

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Hide the mouse cursor
pygame.mouse.set_visible(0)
 
# Speed in pixels per frame
x_speed = 0
y_speed = 0

#thud = pygame.mixer.Sound("thud.ogg") #sound upon pressing left key

score = 0

pygame.time.wait(1000)

# -------- Main Program Loop -----------
while not done:
    # --- Game Logic
    if y<0:
        y+=1
        screen.blit(earth_background, [0, y])

    if y == -3450:
       pygame.time.wait(1000)
           
    allsprites.update()
    allsprites.draw(screen)
    player.move()
    '''
    if y<0:
        rain_list=[]
        for i in range(200):
            x = random.randrange(0, 900)
            y = random.randrange(0, 800)
            pygame.draw.line(screen, BLUE, [x, y], [x+3, y+9], 2)
        for i in range(1000):
            x=random.randrange(0,600)
            y=random.randrange(0,900)
            rain_list.append([x,y])
    '''
    
    
    # see if the player block has collided with anything.
    enemy_hitlist = pygame.sprite.spritecollide(player, cactusmen, True)
    for enemy in enemy_hitlist:
        score +=1
    print(score)
    
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
