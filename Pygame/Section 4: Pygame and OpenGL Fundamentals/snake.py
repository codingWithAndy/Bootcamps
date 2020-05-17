import pygame
import time
import random

# Initialise all the main Pygame methods
pygame.init() 

display_width = 800
display_height = 600

gameScreen = pygame.display.set_mode((display_width, display_height)); # Height and Width in a tuple


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
green = (0,155,0)

pygame.display.set_caption("Old Snake"); #Set Title

# Message to the screen
def message_to_screen(msg,type):
    font = pygame.font.SysFont(None,25)
    screen_text = font.render(msg,True,type)
    gameScreen.blit(screen_text,[display_width/2,display_height/2])

def our_snake(size_of_block,snake_list):
    for XY in snake_list:
        pygame.draw.rect(gameScreen,green,[XY[0],XY[1],size_of_block,size_of_block])
    
    


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
            message_to_screen("Game Over! Press Space to play again or Q to quit!",red)
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
game_loop()
#quit()
