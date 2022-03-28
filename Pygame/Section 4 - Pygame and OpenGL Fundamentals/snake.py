import pygame
import sys
import time
import random

# Initialise all the main Pygame methods
pygame.init() 

display_width = 800
display_height = 600

gameScreen = pygame.display.set_mode((display_width, display_height)); # Height and Width in a tuple

# Font Mesurements
font = pygame.font.SysFont(None, 25)
small_font = pygame.font.SysFont("comicsansms", 25)
medium_font = pygame.font.SysFont("comicsansms", 40)
large_font = pygame.font.SysFont("comicsansms", 80)


# Snake Position
lead_x = display_width / 2
lead_y = display_width / 2
lead_x_change = 0
lead_y_change = 0

steps = 10

# Taking Pygame time clock
clock = pygame.time.Clock()
fps = 15

# Set Colours
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 155, 0)
purple = (128, 0, 128)

pygame.display.set_caption("Old Snake"); #Set Title

# Create Icon
icon = pygame.image.load('/Users/Andy/Developer/Bootcamps/Pygame/Section 4: Pygame and OpenGL Fundamentals/snake_icon2.png')
pygame.display.set_icon(icon)

# Adding an image
# img = pygame.image.load('fullpath/imagename.png')


def game_intro():
    intro = True

    while intro == True:
        gameScreen.fill(white)
        message_to_screen("Welcome", purple, -100, size="large")
        message_to_screen("You should aim to eat as many apples as possible!", black, -50, size="medium")
        message_to_screen("Hope you enjoy!", black, 10, size="small")
        message_to_screen("Press Space to Start game or Q to Quit", black, 100, size="medium")

        pygame.display.update()
        clock.tick(15)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.type == pygame.QUIT:
                    intro = False
                if event.key == pygame.K_q:
                    
                    intro = False
                

                if event.key == pygame.K_SPACE:
                    intro = False
                    game_loop()
    pygame.quit()


def score(score):
    text = small_font.render("Score is: " + str(score), True, white)
    gameScreen.blit(text,[0,0])


def text_objects(text, colour, size):
    if size == "small":
        textSurface = small_font.render(text, True, colour)
    elif size == "medium":
        textSurface = medium_font.render(text, True, colour)
    elif size == "large":
        textSurface = large_font.render(text, True, colour)

    return textSurface, textSurface.get_rect()


# Message to the screen
def message_to_screen(msg, colour, y_displace = 0, size = "small"):
    textsurf, textRect = text_objects(msg,colour,size)

    textRect.center = (display_width/2), (display_height/2) + y_displace
    gameScreen.blit(textsurf, textRect)


def our_snake(size_of_block, snake_list):
    #gameScreen.blit(img,(snake_list[-1][0],snake_list[-1][1])) # Adds snake head image to the snake
    for XY in snake_list:  # to assogn values to all minus the head is: snake_list[:-1]
        pygame.draw.rect(gameScreen,green,[XY[0],XY[1],size_of_block,size_of_block])



# Main Game Loop
def game_loop():
    gameClose = False
    game_over = False
    size_of_block = 10

    lead_x = display_width / 2
    lead_y = display_width / 2
    lead_x_change = 0
    lead_y_change = 0

    snake_list = []
    snake_length = 1

    rand_apple_x = round(random.randrange(0,display_width - size_of_block)/10.0)*10.0
    rand_apple_y = round(random.randrange(0, display_height - size_of_block)/10.0)*10.0
    
    while not gameClose:
        while game_over == True:
            gameScreen.fill(white)
            message_to_screen("Game Over!",red,-50,size="large")
            message_to_screen("Press Space to play again or Q to quit!",black,50,size="medium")
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameClose = True
                        game_over = False
                    
                    if event.key == pygame.K_SPACE:
                        game_loop()
        
        for event in pygame.event.get():
            print(event) # will get positions of mouse and buttons.
            if event.type == pygame.QUIT:
                gameClose = True
            
            # Checking for buttons being pressed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_x_change = -steps
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    lead_x_change = steps
                    lead_y_change = 0
                
                elif event.key == pygame.K_UP:
                    lead_y_change = -steps
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    lead_y_change = steps
                    lead_x_change = 0

        if lead_x >= 800 or lead_x < 10 or lead_y >= 600 or lead_y < 0:
            game_over = True

        lead_x += lead_x_change
        lead_y += lead_y_change

        gameScreen.fill(black)  # or a tuple ((255,255,255))

        pygame.draw.rect(gameScreen, red, (rand_apple_x,rand_apple_y,size_of_block, size_of_block))

        #pygame.draw.rect(gameScreen, green, (lead_x,lead_y,10,10)) # Where to place, fill colour, location and size in tuple or list
        # gameScreen.fill(red, rect=[200,200,50,50])  # Alternative to the above statement
        snake_head = []
        snake_head.append(lead_x)
        snake_head.append(lead_y)

        snake_list.append(snake_head)
        
        if len(snake_list) > snake_length:
            del snake_list[0]

        for each_segment in snake_list[:-1]:
            if each_segment == snake_head:
                game_over = True
        

        our_snake(size_of_block, snake_list)
        score(snake_length-1)
        pygame.display.update()  # Update the screen
        
        if lead_x == rand_apple_x and lead_y == rand_apple_y:
            rand_apple_x = round(random.randrange(0, display_width - size_of_block)/10.0)*10.0
            rand_apple_y = round(random.randrange(0, display_height - size_of_block)/10.0)*10.0

            snake_length += 1

        clock.tick(fps)  # frame per second
    
    pygame.quit()
'''
    message_to_screen("You Lose!!!", red)
    pygame.display.update()
    time.sleep(2)
    pygame.quit()
'''

game_intro()
#game_loop()
