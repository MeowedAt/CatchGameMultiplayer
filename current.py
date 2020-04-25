import pygame
from pygame.locals import *
import sys, math, random
from time import sleep
import time, socket, sys, pickle

soc = socket.socket()
shost = socket.gethostname()
ip = socket.gethostbyname(shost)
print(shost, '({})'.format(ip))

sendonjoin = ip
server_host = "127.0.1.1"
clientname1 = "player"
port = 8824
soc.connect((server_host, port))
soc.send(sendonjoin.encode())

class Ball():
    
    def __init__(self, startx):
        self.ballx = startx
        self.bally = 30
        ##        screen.get_height()-199
        self.ballismovingright = True
        self.hitcount = 5
        self.bottom = screen.get_height() - 200
        self.ballcdh = 100
        self.colour = blue
        self.coconut = 0
        self.deadpos = 0

    def drawball(self):
        pygame.draw.circle(screen, (self.colour), (self.ballx, self.bally), 20)
        message_display_pos_size(str(self.hitcount), screen.get_height() - 200 - self.ballx,
                                 screen.get_height() - self.bally)

    def checkonscreen(self):
        if self.bally > screen.get_height():
            ##            print("you lose")
            applemeow = "nope"
        if self.ballx > 400:
            self.ballismovingright = False
            self.bally = self.bally + 30
        if self.ballx < 0:
            self.ballismovingright = True
            self.bally = self.bally + 30

    def isAlive(self):
        return self.coconut == 0

    def moveball(self):
        if self.isAlive():
            if self.ballismovingright:
                self.ballx = self.ballx + 1
            else:
                self.ballx = self.ballx - 1
            if self.bally > self.bottom:
                self.bally = 30
                self.ballismovingright = True
                self.ballx = 30
                soc.send(pos2send.encode())
        else:
            if self.deadpos == 0:
                # This means it has NOT died yet. Don't use this use - self.isALive() to get alive / false.
                # 1 = left
                # 2 = right
                # 3 = up
                # 4 = down
                self.deadpos = 2
            if self.deadpos == 1:
                self.ballx = self.ballx - 5
                self.deadpos = 3
            if self.deadpos == 2:
                self.ballx = self.ballx + 5
                self.deadpos = 4
            if self.deadpos == 3:
                self.bally = self.bally + 5
                self.deadpos = 2
            if self.deadpos == 4:
                self.bally = self.bally - 5
                self.deadpos = 1

    def deathpro(self):
        self.colour = yellow
        self.coconut = self.coconut + 1

    ##        while self.coconut < 21:
    ##            self.coconut = self.coconut + 1
    ##            if self.coconut >19:
    ##                self.coconut = 0

    def hitshow(self):
        self.chicken = "yummy"


class Projectile:

    def whatever():
        print("hi")


# ballx = 15
# bally = 30
prox = 15
proy = 30
botmode=False
batx = 200
baty = 500
shotdistance = 0
score = 100
aaa = 0
bbb = 0
ccc = 0
hitboxon = True
debugmode = False
shot = True
projectile = False
movingdown = True
caught = False
counting = False
red = (255, 73, 73)
white = (255, 255, 255)
yellow = (69, 244, 66)
black = (0, 0, 0)
blue = (0, 0, 255)
purple = (176, 4, 127)
color = white
display_width = 400
display_height = 600
# todo: change name to projectilecolor or similar, as this is not the balls colour
ballcolour = blue
ballc = blue
realscore = score-100
countdownhit = 0
waitabit = 0
timer = 0
pos2send=[]
countingbcdh = False
pygame.init()

screen = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Catch Game")

##ball = Ball()
balls = []
balls.append(Ball(15))

def text_objects(text, font, colour):
    textSurface = font.render(text, True, colour)
    return textSurface, textSurface.get_rect()


def message_display(text):
    largeText = pygame.font.Font('fonts/font.ttf', 50)
    TextSurf, TextRect = text_objects(text, largeText, blue)
    TextRect.center = ((display_width - 50), (display_height - 50))
    screen.blit(TextSurf, TextRect)


def message_display_pos(text, x, y):
    largeText = pygame.font.Font('fonts/font.ttf', 20)
    TextSurf, TextRect = text_objects(text, largeText, blue)
    TextRect.center = ((display_width - x), (display_height - y))
    screen.blit(TextSurf, TextRect)


def message_display_pos_size(text, x, y):
    largeText = pygame.font.Font('fonts/font.ttf', 20)
    TextSurf, TextRect = text_objects(text, largeText, black)
    TextRect.center = ((display_width - x), (display_height - y))
    screen.blit(TextSurf, TextRect)


#def message_display_timer(text, x, y):
#    largeText = pygame.font.Font('font.ttf', 50)
#    TextSurf, TextRect = text_objects(text, largeText, black)
#    TextRect.center = ((display_width - 50), (display_height - 100))
#    screen.blit(TextSurf, TextRect)


def drawprojectile():
    pygame.draw.circle(screen, (ballcolour), (prox, proy), 10)


def drawbat():
    pygame.draw.line(screen, (0, 0, 255), (batx - 30, baty), (batx + 30, baty), 6)


def movebat():
    global batx
    global baty

    if pressed_keys[K_LEFT] and batx > 40:
        batx -= 5

    if pressed_keys[K_RIGHT] and batx < 360:
        batx += 5


def gameOver():
    pygame.quit()


donuts = "not yummy"


def donothing():
    donuts = "yummy"


clock = pygame.time.Clock()

# todo: move this to ball class
# do not change... i warned u.
# bally = screen.get_height()-199

# screen.fill((0,255,255))
# pressed_keys = pygame.key.get_pressed()

# while not pressed_keys[K_SPACE]:
#    pygame.display.update()
#    pass

print("passed the infinte loop")
screen.fill((0, 0, 255))
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            gameOver()
    
    pygame.display.update()
    pressed_keys = pygame.key.get_pressed()

    screen.fill((0, 0, 255))
    pygame.draw.rect(screen, (0, 0, 0), Rect((10, 10), (screen.get_width() - 20, screen.get_height() - 20)))
    if debugmode:
        pygame.draw.line(screen, (0, 255, 0), (10, screen.get_height() - 200), (390, screen.get_height() - 200), 6)
    drawbat()

    drawprojectile()
    message_display(str(score))
    message_display_pos(str(timer), display_width - 50, display_height - 100)  #########################################

    for ballitem in balls:
        ballitem.drawball()
        ballitem.hitshow()

    movebat()

    if proy > screen.get_height() - 20 or proy < 0:
        movingdown = True
        if random.randint(1, 1000) >= 999:
            # todo: add more projectiles and randomize.
            try:
                ballitem = balls[0]
                prox = ballitem.ballx
                proy = ballitem.bally + 30
            except:
                print("No balls on screen")

    if random.randint(1, 1000) >= 998:
        balls.append(Ball(15))

    # todo: add a call for checkonscreen() ball class.
    for ballitem in balls:
        ballitem.checkonscreen()

    if caught:
        ballcolour = red
    else:
        ballcolour = blue

    if pressed_keys[K_F1]:
        for ballitem in balls:
            balls.remove(ballitem)

    if pressed_keys[K_F2]:
        ###################
        balls.append(Ball(15))
    
    if pressed_keys[K_SPACE] and caught:
        proy = proy - 30
        caught = False
        movingdown = False
        ballcolour = red

    if pressed_keys[K_F3]:
        debugmode = True
    if pressed_keys[K_F4]:
        debugmode = False
    # if pressed_keys[K_C]:
    #    if debugmode:
    #        balls.append(Ball(30))

    if movingdown:
        if not caught:
            proy = proy + 3
    else:
        if not caught:
            proy = proy - 3

    if caught:
        proy = baty
        prox = batx

    for ballitem in balls:
        ballitem.moveball()
        if ballitem.hitcount < 1:
            ballitem.deathpro()
            if ballitem.coconut == 200:
                balls.remove(ballitem)

    if pygame.Rect(batx, baty, 50, 20).colliderect(prox - 10, proy - 10, 20, 20):
        #        proy = proy-30
        movingdown = False
        caught = True
    else:
        caught = False

    #bot mode

#    if pressed_keys[K_F8]:
#        botmode=True
#    if pressed_keys[K_F7]:
#        botmode=False
#    if botmode:
#        batx = prox
#    if caught:
#        proy = proy - 30
#        caught = False
#        movingdown = False
#        ballcolour = red         
 
    # IMPORTANT VARIABLES: CHANGE AT YOUR OWN RISK
    placex = 60
    placey = 20
    # set to negative number to add instead of subtract.
    subtractx = 30
    subtracty = 0
    # I couldn't come up with a better name for any variable.
    
    if debugmode:
        for ballitem in balls:
            pygame.draw.rect(screen, (0, 255, 0),
                             Rect((ballitem.ballx - subtractx, ballitem.bally - subtracty), (placex, placey)))
            message_display_pos("BHP = " + str(ballitem.ballcdh), 330, 110)  # ballhp (like cdh)
        message_display_pos("FPS = " + str(round(clock.get_fps(), 1)), 330, 50)  # Gamefps
        message_display_pos("BOX = " + str(hitboxon), 330, 70)  # Is the hitbox on?
        message_display_pos("CDH = " + str(countdownhit), 330, 90)  # CountDownHit to countdown ticks from hit
        message_display_pos(("Debug mode for nerds :)"), 270, 570)  # just a piece of text...

    for ballitem in balls:
        if pygame.Rect(ballitem.ballx - subtractx, ballitem.bally - subtracty, placex, placey).colliderect(prox - 10,
                                                                                                           proy - 10,
                                                                                                           20, 20):
            ballitem.hitcount = ballitem.hitcount - 1
            aaa = random.uniform(0, 255)
            bbb = random.uniform(0, 255)
            ccc = random.uniform(0, 255)
            ##        ballc = str("("+str(aaa)+", "+str(bbb)+", "+str(ccc)+")")
            if movingdown:
                movingdown = False
                proy = proy - 20
            else:
                movingdown = True
                proy = proy + 20
            if hitboxon:
                score = score + 1
                hitboxon = False
                counting = True
                countdownhit = 50
            # if ballc == blue:
            #    ballc = white
            # else:
            #    ballc == blue

    # countdownhit is the number of ticks before giving a score on hit. (to stop clipping on the side pf the hitbox)
    # countingbcdh
    if countdownhit < 1:
        hitboxon = True
        counting = False
    if counting:
        countdownhit = countdownhit - 1
    pygame.display.update()
    pygame.display.flip()
    clock.tick(120)
    pos2send=[batx,score,prox,proy]
    data = pickle.dumps(pos2send)
    soc.send(data)
    del pos2send[:]
    
