import pygame
import random
import array 
pygame.init()

width = 400
height = 400
 
window = pygame.display.set_mode((width,height))
 
pygame.display.set_caption("Ssssnake")
 
black = (0,0,0)
white = (255,255,255)
red = (255,25,25)
orange = (255,132,0)
yellow = (255,255,0)
green = (25,255,25)
blue = (25,25,255)
purple = (255,25,255)
magenta =(175,0,255)
mx, my = 100, 100
snakeX = []
snakeY = []
food = 0
length = 0
'cell must be a whole number whereas width % dividend = 0'
cell = width/20
gameSpeed = 10
cell
velocityX = 0
velocityY = cell
clock = pygame.time.Clock()
 
def detectCollisions(x1,y1,x2,y2):
 
    if (x1 == x2 and y1 == y2):

        print("Yum!")
        
        return True
    
    else:

        return False

def printTail():
   
    for x in range(0, length):
        if(FOOD.x == snakeX[x] and FOOD.y == snakeY[x]):
            FOOD.drawRandom()

        c = 5*x
        
      

        
        if (x % 7 == 0):
            pygame.draw.rect(window,red,(snakeX[x],snakeY[x],cell,cell))
        elif (x % 7 == 1):
            pygame.draw.rect(window,orange,(snakeX[x],snakeY[x],cell,cell))
        elif (x % 7 == 2):
            pygame.draw.rect(window,yellow,(snakeX[x],snakeY[x],cell,cell))
        elif (x % 7 == 3):
            pygame.draw.rect(window,green,(snakeX[x],snakeY[x],cell,cell))
        elif (x % 7 == 4):
            pygame.draw.rect(window,blue,(snakeX[x],snakeY[x],cell,cell))
        elif (x % 7 == 5):
            pygame.draw.rect(window,purple,(snakeX[x],snakeY[x],cell,cell))
        elif (x % 7 == 6):
            pygame.draw.rect(window,magenta,(snakeX[x],snakeY[x],cell,cell))
        else:
            pygame.draw.rect(window,black,(snakeX[x],snakeY[x],cell,cell))
      
        

def storeTail():
    
    snakeX.insert(0, Sprite1.x)
    snakeY.insert(0, Sprite1.y)

    
    return True

 

class Sprite:
 
    def __init__(self,x,y,width,height):
 
        self.x=x
 
        self.y=y
 
        self.width=width
 
        self.height=height
 
    def draw(self):
 
            pygame.draw.rect(window,black,(self.x,self.y,self.width,self.height))

    def drawRandom(self):
            
        self.x = (random.randint(1,(width/cell-1)) * cell)
        self.y = (random.randint(1,(height/cell-1)) * cell)
        
            
        pygame.draw.rect(window,black,(self.x,self.y,self.width,self.height))
 
Sprite1=Sprite(cell,cell,cell,cell)
FOOD=Sprite(cell,cell,cell,cell) 
moveX,moveY=0,0
 
gameLoop=True
while gameLoop:
 
    for event in pygame.event.get():
 
        if (event.type==pygame.QUIT):
 
            gameLoop=False
 
        if (event.type==pygame.KEYDOWN):
         
            if (event.key==pygame.K_LEFT):
                if not (velocityX == cell): 
                    velocityX = (cell * -1)
                    velocityY = 0
 
            if (event.key==pygame.K_RIGHT):
                 if not (velocityX == (-1 * cell)):
                    velocityX = cell
                    velocityY = 0
 
            if (event.key==pygame.K_UP):
                 if not (velocityY == cell):
                    velocityY = (cell * -1)
                    velocityX = 0
 
            if (event.key==pygame.K_DOWN):
                 if not (velocityY == (-1 * cell)):
                    velocityY = cell
                    velocityX = 0
            
    window.fill(white)

    

    if((Sprite1.x < cell) and (velocityX < 0)):
        Sprite1.x = (width - cell)
    elif(((Sprite1.x + Sprite1.width)  > width - cell) and (velocityX > 0)):
        Sprite1.x = 0
    elif((Sprite1.y < cell) and (velocityY < 0)):
         Sprite1.y = (height - cell)
    elif(((Sprite1.y + Sprite1.height) > height - cell) and (velocityY > 0)):
         Sprite1.y = 0
    else:
         Sprite1.y += velocityY
         Sprite1.x += velocityX
         
    if (detectCollisions(Sprite1.x,Sprite1.y,FOOD.x,FOOD.y) == True):

        length+=1
        food = 0
            

    if(food == 0):

        gameSpeed += 0.25
        
        food = 1

        FOOD.drawRandom()

    

    storeTail()

    FOOD.draw()
    
    Sprite1.draw()

    printTail()
 
    pygame.display.flip()
 
    clock.tick(gameSpeed)
 
pygame.quit()
