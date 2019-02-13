
import os, pygame, sys, random, math
from pygame.locals import *


# Constant color definitions
           #R    G    B
ORANGE =   (255, 128, 0)
BLUE =     (0,   0,   255)
GREEN =    (0,   128, 0)
PURPLE =   (128, 0,   128)
RED =      (255, 0,   0)
YELLOW =   (255, 255, 0)
NAVYBLUE = (0,   0,   128)
WHITE =    (255, 255, 255)
BLACK =    (0,   0,   0)









pygame.init()


player_img = pygame.image.load('ufo.png')
space_bg = pygame.image.load('space_bg.jpg')
space = space_bg.get_rect()
meteor_img = pygame.image.load('Meteor.png')

#Exmark utilized from https://www.iconfinder.com/icons/2472270/alert_danger_error_exclamation_mark_red_icon
ex_mark_img = pygame.image.load('ex_mark.png')
ex_mark = ex_mark_img.get_rect()
clock = pygame.time.Clock()

def init_main_window(dimensions, caption):
    pygame.init()
    pygame.display.set_caption(caption)
    return pygame.display.set_mode(dimensions)

class player(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 7
        self.left = False
        self.right = False
        self.up = False
        self.down = False
        self.bubble = 200
    def show(self, DISPLAYSURF):

        if self.left and self.up:
            self.x -= self.vel
            self.y -= self.vel
            DISPLAYSURF.blit(player_img, (self.x,self.y))
        elif self.left and self.down:
            self.x -= self.vel
            self.y += self.vel
            DISPLAYSURF.blit(player_img, (self.x,self.y))
        elif self.right and self.up:
            self.x += self.vel
            self.y -= self.vel
            DISPLAYSURF.blit(player_img, (self.x,self.y))
        elif self.right and self.down:
            self.x += self.vel
            self.y += self.vel
            DISPLAYSURF.blit(player_img, (self.x,self.y))

        elif self.left:
            self.x -= self.vel
            DISPLAYSURF.blit(player_img, (self.x,self.y))
        elif self.right:
            self.x += self.vel
            DISPLAYSURF.blit(player_img, (self.x,self.y))
        elif self.up:
            self.y -= self.vel
            DISPLAYSURF.blit(player_img, (self.x,self.y))
        elif self.down:
            self.y += self.vel
            DISPLAYSURF.blit(player_img, (self.x,self.y))
        else:
            DISPLAYSURF.blit(player_img, (self.x,self.y))

        #resetting of off of edge
        if self.x < 0:
            self.x = 0
        if self.x > dispwidth:
            self.x = dispwidth
        if self.y < 0:
            self.y = 0
        if self.y > dispheight:
            self.y = dispheight

class meteor(object):

    def __init__(self, x, y, width, height):
        angle = 360*random.random() #random() generates float b/t 0.0 and 1.0
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel_mag = 7
        self.x_mag = self.vel_mag*math.sin(angle)
        self.y_mag = self.vel_mag*math.cos(angle)
        self.move = True
    def show(self, DISPLAYSURF):
        if self.move:
            self.x -= self.x_mag
            self.y += self.y_mag

            # Reset if falls off DISPLAYSURF
            if self.x < 0:
                self.x_mag = -self.x_mag
                #self.reset(DISPLAYSURF)
            if self.x > dispwidth:
                self.x_mag = -self.x_mag
                #self.reset(DISPLAYSURF)
            if self.y < 0:
                self.y_mag = -self.y_mag
                #self.reset(DISPLAYSURF)
            if self.y > dispheight:
                self.y_mag = -self.y_mag
                #self.reset(DISPLAYSURF)
            DISPLAYSURF.blit(meteor_img, (self.x,self.y))

            ''' may no longer be utilized
            def reset(self, DISPLAYSURF):
                randx = random.randint(0,dispwidth)
                randy = random.randint(0,dispheight)
                #if meteor is spawning too close to char
                if abs(randx-char.x)<char.bubble*1.2 and abs(randy-char.y)<char.bubble*1.2:
                    self.x = randx + char.bubble*1.2
                    self.y = randy + char.bubble*1.2
                else:
                    self.x = randx
                    self.y = randy
            '''
            #collision
            if abs(self.x - char.x) < 50 and abs(self.y - char.y) < 50:
                start_game = False
                end_game = True
                run = False
                print('oops, you are quite awful')
                self.x = randx+char.bubble*1.2
                self.y = randy+char.bubble*1.2
                pygame.event.post(pygame.event.Event(QUIT))
                #quit_game = pygame.event.Event(pygame.QUIT)
                #pygame.event.post(quit_game)
                #pygame.event.post(pygame.event.Event(QUIT))
                #sys.exit()
                #ideally, would define this as own function, and prompt end_game screen with score
                # (You survived __ seconds -> fun facts, ex: That's longer than: The Comm takes to run the IOCT!, Dr. Blair takes to finish a given CY300 HW problem!)


dispwidth = 800
dispheight = 800
DISPLAYSURF = init_main_window((dispwidth, dispheight), 'Meteor')

#mainloop
char = player(dispwidth/2, dispheight/2, 50, 50)

#spawning multiple meteors
mtr = meteor(random.randint(0,dispwidth), random.randint(0,dispheight), 50, 50)
meteors = []
max_mtrs = 10

for n in range(max_mtrs):
    randx = random.randint(0,dispwidth)
    randy = random.randint(0,dispheight)
    #if meteor is spawning too close to char
    if abs(randx-char.x)<char.bubble*1.2 and abs(randy-char.y)<char.bubble*1.2:
        meteors.append(meteor(randx+char.bubble*1.2, randy+char.bubble*1.2, 50, 50))
    else:
        meteors.append(meteor(randx, randy, 50, 50))
#oneMeteor = meteor(dispwidth/2,50,50,50)


time_survived = 0
font = pygame.font.SysFont(None, 20)
'''
basicfont = pygame.font.SysFont(None, 48)
text = basicfont.render('Hello World!', True, (255, 0, 0), (255, 255, 255))
textrect = text.get_rect()
textrect.centerx = DISPLAYSURF.get_rect().centerx
textrect.centery = DISPLAYSURF.get_rect().centery
'''

# Write text onto the game-board (game window)
def draw_text(text, font, surface, x, y):
    textobj = font.render(text, 1, WHITE)
    textrect = textobj.get_rect()
    textrect.topleft = (x,y)
    surface.blit(textobj, textrect)




count = 0
delay_count = 1


#from CITATION
pygame.display.set_caption('Meteor!')

size = DISPLAYSURF.get_size()
width = size[0]
height = size[1]

title = pygame.Rect(((width/16)+1, (height/8)+1, 7*width/8, height/4))
dead = pygame.Rect(((width/16)+1, (height/8)+1, 7*width/8, height/4))
menu1 = pygame.Rect(((width/4)+1, (height/2)+1, 2*width/4, height/10))
menu2 = pygame.Rect(((width/4)+1, (height/2)+1+(3*height/20), 2*width/4, height/10))


#Draws dark blue rectangles.
#pygame.draw.rect(DISPLAYSURF, (0,0,150), menu1)
#pygame.draw.rect(DISPLAYSURF, (0,0,150), menu2)

#Draws blue ovals on top of the rectangles.
#pygame.draw.ellipse(DISPLAYSURF, BLACK, title)
#pygame.draw.ellipse(DISPLAYSURF, BLACK, menu1)
#pygame.draw.ellipse(DISPLAYSURF, BLACK, menu2)

#pygame.font.Font takes in a font name and an integer for its size.
#Free Sans Bold comes with Pygame (Sweigart 2012 p. 30).
font_title = pygame.font.Font('freesansbold.ttf', 64)
font_menu = pygame.font.Font('freesansbold.ttf', 32)

#Creates and draws the text.
surface_title = font_title.render('Meteor!', True, (0, 10, 76))
rect_title = surface_title.get_rect() #get_rect() is my favorite Pygame function.
rect_title.center = (width/2,(height/4)+3)
surface_new_game = font_menu.render('NEW GAME', True, WHITE)
rect_new_game = surface_new_game.get_rect()
rect_new_game.center = (width/2,(height/2)+(height/20)+3)
surface_exit_game = font_menu.render('EXIT', True, WHITE)
rect_exit_game = surface_exit_game.get_rect()
rect_exit_game.center = (width/2, (height/2)+(4*height/20)+3)
surface_you_died = font_title.render('GAME OVER', True, (0, 10, 76))
rect_dead = surface_you_died.get_rect() #get_rect() is my favorite Pygame function.
rect_dead.center = (50*width/100,(height/4)+3)
surface_play_again = font_menu.render('ONE MORE TRY!', True, WHITE)
rect_play_again = surface_new_game.get_rect()
rect_play_again.center = (45*width/100,(height/2)+(height/20)+3)

run = True
def play_game(run):

    count = 0
    delay_count = 1

    start_game = False
    end_game = False

    time_survived = 0
    font = pygame.font.SysFont(None, 20)
    #from CITATION
    pygame.display.set_caption('Meteor!')

    size = DISPLAYSURF.get_size()
    width = size[0]
    height = size[1]

    title = pygame.Rect(((width/16)+1, (height/8)+1, 7*width/8, height/4))
    dead = pygame.Rect(((width/16)+1, (height/8)+1, 7*width/8, height/4))
    menu1 = pygame.Rect(((width/4)+1, (height/2)+1, 2*width/4, height/10))
    menu2 = pygame.Rect(((width/4)+1, (height/2)+1+(3*height/20), 2*width/4, height/10))


    #Draws dark blue rectangles.
    #pygame.draw.rect(DISPLAYSURF, (0,0,150), menu1)
    #pygame.draw.rect(DISPLAYSURF, (0,0,150), menu2)

    #Draws blue ovals on top of the rectangles.
    #pygame.draw.ellipse(DISPLAYSURF, BLACK, title)
    #pygame.draw.ellipse(DISPLAYSURF, BLACK, menu1)
    #pygame.draw.ellipse(DISPLAYSURF, BLACK, menu2)

    #pygame.font.Font takes in a font name and an integer for its size.
    #Free Sans Bold comes with Pygame (Sweigart 2012 p. 30).
    font_title = pygame.font.Font('freesansbold.ttf', 64)
    font_menu = pygame.font.Font('freesansbold.ttf', 32)

    #Creates and draws the text.
    surface_title = font_title.render('Meteor!', True, (0, 10, 76))
    rect_title = surface_title.get_rect() #get_rect() is my favorite Pygame function.
    rect_title.center = (width/2,(height/4)+3)
    surface_new_game = font_menu.render('NEW GAME', True, WHITE)
    rect_new_game = surface_new_game.get_rect()
    rect_new_game.center = (width/2,(height/2)+(height/20)+3)
    surface_exit_game = font_menu.render('EXIT', True, WHITE)
    rect_exit_game = surface_exit_game.get_rect()
    rect_exit_game.center = (width/2, (height/2)+(4*height/20)+3)
    surface_you_died = font_title.render('GAME OVER', True, (0, 10, 76))
    rect_dead = surface_you_died.get_rect() #get_rect() is my favorite Pygame function.
    rect_dead.center = (50*width/100,(height/4)+3)
    #surface_play_again = font_menu.render('PLAY AGAIN', True, WHITE)

    while run:

        DISPLAYSURF.blit(surface_title, rect_title)
        #DISPLAYSURF.blit(space_bg, space)
        DISPLAYSURF.blit(surface_new_game, rect_new_game)
        DISPLAYSURF.blit(surface_exit_game, rect_exit_game)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print('reach')
                start_game = False
                #end_game = True
                run = False
                #print('this is fully functioning')
                #sys.exit()

            if event.type == VIDEORESIZE:
                #This line creates a new display in order to clear the screen.

                DISPLAYSURF.blit(space_bg, space)
                width = event.w
                height = event.h

                #Creates the rectangle objects that will be behind the title and menu buttons.
                title = pygame.Rect(((width/16)+1, (height/8)+1, 7*width/8, height/4))
                menu1 = pygame.Rect(((width/4)+1, (height/2)+1, 2*width/4, height/10))
                menu2 = pygame.Rect(((width/4)+1, (height/2)+1+(3*height/20), 2*width/4, height/10))


                #Draws dark blue rectangles.
                #pygame.draw.rect(DISPLAYSURF, BLACK, menu1)
                #pygame.draw.rect(DISPLAYSURF, BLACK, menu2)

                #Draws blue ovals on top of the rectangles.
                pygame.draw.ellipse(DISPLAYSURF, (12, 167, 223), title)
                pygame.draw.ellipse(DISPLAYSURF, BLACK, menu1)
                pygame.draw.ellipse(DISPLAYSURF, BLACK, menu2)

                #Creates and draws the text.
                rect_title = surface_title.get_rect()
                rect_title.center = (width/2,(height/4)+3)
                rect_new_game = surface_new_game.get_rect()
                rect_new_game.center = (width/2,(height/2)+(height/20)+3)
                rect_exit_game = surface_exit_game.get_rect()
                rect_exit_game.center = (width/2,(height/2)+(4*height/20)+3)

                pygame.display.update() #Necessary to update the screen

            #When you let go of the left mouse button in the area of a button, the button does something.
            if event.type == MOUSEBUTTONUP:
                if event.button == 1:
                    if (menu1.left < event.pos[0] < menu1.right) and (menu1.top < event.pos[1] < menu1.bottom):
                        start_game = True

                        print("NEW GAME") #Placeholder #We want a difficulty setting display#
                    if (menu2.left < event.pos[0] < menu2.right) and (menu2.top < event.pos[1] < menu2.bottom):
                        sys.exit()
                        pygame.event.post(pygame.event.Event(QUIT))

            #When you mouse-over a button, the text turns green.
            if event.type == MOUSEMOTION:
                if (menu1.left < event.pos[0] < menu1.right) and (menu1.top < event.pos[1] < menu1.bottom):
                    surface_new_game = font_menu.render('NEW GAME', True, (0, 255, 0))
                else:
                    surface_new_game = font_menu.render('NEW GAME', True, (12, 167, 223))
                if (menu2.left < event.pos[0] < menu2.right) and (menu2.top < event.pos[1] < menu2.bottom):
                    surface_exit_game = font_menu.render('EXIT', True, RED)
                else:
                    surface_exit_game = font_menu.render('EXIT', True, (12, 167, 223))

        if start_game:
            if count < delay_count:
                pygame.time.delay(500)
                count +=1

            clock.tick(30)
            time_survived += round(1/30,2)

            if time_survived> 5:
                mtr.show(DISPLAYSURF)


            DISPLAYSURF.blit(space_bg, space)
            #DISPLAYSURF.blit(text, textrect)
            keys = pygame.key.get_pressed()

            #diagonal movement
            if keys[pygame.K_LEFT] and keys[pygame.K_UP]:
                char.left = True
                char.up = True
            elif keys[pygame.K_LEFT] and keys[pygame.K_DOWN]:
                char.left = True
                char.down = True
            elif keys[pygame.K_RIGHT] and keys[pygame.K_UP]:
                char.right = True
                char.up = True
            elif keys[pygame.K_RIGHT] and keys[pygame.K_DOWN]:
                char.right = True
                char.down = True
            elif keys[pygame.K_LEFT]:
                char.left = True
            elif keys[pygame.K_RIGHT]:
                char.right = True
            elif keys[pygame.K_UP]:
                char.up = True
            elif keys[pygame.K_DOWN]:
                char.down = True

            else:
                char.up, char.down, char.left, char.right = False, False, False, False

            char.show(DISPLAYSURF)

            for meteor in meteors:
                meteor.show(DISPLAYSURF)


            #oneMeteor.show(DISPLAYSURF)
            # update display
            draw_text("Time Survived: {:.2f}".format(time_survived), font, DISPLAYSURF, 10, 0)
            pygame.display.update()


        pygame.display.update()
    return time_survived
# DISPLAYSURF.fill(WHITE)
# DISPLAYSURF.blit(space_bg, space)
# DISPLAYSURF.blit(surface_you_died, rect_dead)
# DISPLAYSURF.blit(surface_play_again, rect_new_game)
# DISPLAYSURF.blit(surface_exit_game, rect_exit_game)
#game over screen
score = play_game(run)
print('Time survived: ', score, 's')
end_game = True
while end_game:

    DISPLAYSURF.blit(space_bg, space)
    # DISPLAYSURF.blit(surface_title, rect_title)
    # DISPLAYSURF.blit(surface_new_game, rect_new_game)
    # DISPLAYSURF.blit(surface_exit_game, rect_exit_game)

    #Creates the rectangle objects that will be behind the title and menu buttons.
    title = pygame.Rect(((width/16)+1, (height/8)+1, 7*width/8, height/4))
    menu1 = pygame.Rect(((width/4)+1, (height/2)+1, 2*width/4, height/10))
    menu2 = pygame.Rect(((width/4)+1, (height/2)+1+(3*height/20), 2*width/4, height/10))


    #Draws dark blue rectangles.
    # pygame.draw.rect(DISPLAYSURF, (0,0,150), menu1)
    # pygame.draw.rect(DISPLAYSURF, (0,0,150), menu2)

    #Draws blue ovals on top of the rectangles.
    pygame.draw.ellipse(DISPLAYSURF, (12, 167, 223), title)
    pygame.draw.ellipse(DISPLAYSURF, BLACK, menu1)
    pygame.draw.ellipse(DISPLAYSURF, BLACK, menu2)

    #Creates and draws the text.
    rect_title = surface_title.get_rect()
    rect_title.center = (width/2,(height/4)+3)
    rect_new_game = surface_new_game.get_rect()
    rect_new_game.center = (width/2,(height/2)+(height/20)+3)
    rect_exit_game = surface_exit_game.get_rect()
    rect_exit_game.center = (width/2,(height/2)+(4*height/20)+3)

    #DISPLAYSURF.blit(space_bg, space)
    DISPLAYSURF.blit(surface_you_died, rect_dead)
    DISPLAYSURF.blit(surface_play_again, rect_play_again)
    DISPLAYSURF.blit(surface_exit_game, rect_exit_game)

    #DISPLAY score
    font_score = pygame.font.Font('freesansbold.ttf', 20)
    surface_score = font_score.render("YOU SURVIVED: {:.2f} s".format(score), True, (0, 10, 76))
    rect_score = surface_score.get_rect() #get_rect() is my favorite Pygame function.
    rect_score.center = (width/2,(height/4)+57)
    DISPLAYSURF.blit(surface_score, rect_score)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        #When you let go of the left mouse button in the area of a button, the button does something.
        if event.type == MOUSEBUTTONUP:
            if event.button == 1:
                if (menu1.left < event.pos[0] < menu1.right) and (menu1.top < event.pos[1] < menu1.bottom):
                    start_game = True
                    end_game = False
                    DISPLAYSURF.blit(space_bg, space)

                    pygame.draw.ellipse(DISPLAYSURF, (12, 167, 223), title)
                    pygame.draw.ellipse(DISPLAYSURF, BLACK, menu1)
                    pygame.draw.ellipse(DISPLAYSURF, BLACK, menu2)

                    play_game(run)

                    #after dying twice
                    #FREE TRIAL EXPIRED screen
                    trial = True
                    while trial:
                        TRIALSURF = init_main_window((dispwidth, dispheight), 'Buy the Full Version!')
                        TRIALSURF.blit(space_bg, space)
                        pygame.font.init() # you have to call this at the start,
                        # if you want to use this module.
                        attention_font = pygame.font.SysFont('Comic Sans MS', 50)
                        expired_font = pygame.font.SysFont('Comic Sans MS', 35)
                        attention = attention_font.render('ATTENTION:', False, RED)
                        expired = expired_font.render('Your free trial has expired!', False, RED)
                        email_font = pygame.font.SysFont('Comic Sans MS', 20)
                        email = email_font.render('Please email LTC Cody at jason.cody@westpoint.edu if you are interested', False, (12, 167, 223))
                        email_pt2 = email_font.render('in purchasing the $5.99 full version of Meteor!', False, (12, 167, 223))


                        TRIALSURF.blit(attention,(.32*width, .25*height))
                        TRIALSURF.blit(expired,(.27*width, .32*height))
                        TRIALSURF.blit(email,(.1*width, .55*height))
                        TRIALSURF.blit(email_pt2,(.2*width, .58*height))
                        ex_mark.center = (17*width/100,.33*height)
                        TRIALSURF.blit(ex_mark_img,ex_mark)

                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                sys.exit()

                            if event.type == MOUSEMOTION:
                                if (menu2.left < event.pos[0] < menu2.right) and (menu2.top < event.pos[1] < menu2.bottom):
                                    surface_exit_game = font_menu.render('EXIT', True, (255,0,0))
                                else:
                                    surface_exit_game = font_menu.render('EXIT', True, (12, 167, 223))
                            pygame.display.update()
                        pygame.display.update()

                    print("PURCHASE THE FULL VERSION!") #Placeholder #We want a difficulty setting display#
                if (menu2.left < event.pos[0] < menu2.right) and (menu2.top < event.pos[1] < menu2.bottom):
                    print('test')
                    sys.exit()

        #When you mouse-over a button, the text turns green.
        if event.type == MOUSEMOTION:
            if (menu1.left < event.pos[0] < menu1.right) and (menu1.top < event.pos[1] < menu1.bottom):
                surface_play_again = font_menu.render('ONE MORE TRY!', True, (0,255,0))
            else:
                surface_play_again = font_menu.render('ONE MORE TRY!', True, (12, 167, 223))
            if (menu2.left < event.pos[0] < menu2.right) and (menu2.top < event.pos[1] < menu2.bottom):
                surface_exit_game = font_menu.render('EXIT', True, (255,0,0))
            else:
                surface_exit_game = font_menu.render('EXIT', True, (12, 167, 223))
        pygame.display.update()
    pygame.display.update()

pygame.quit()
sys.exit()
