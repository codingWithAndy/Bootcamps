import pygame

# Initialise all the main Pygame methods
pygame.init() 

gameScreen = pygame.display.set_mode((800, 600)); # Height and Width in a tuple
gameClose = False

# Snake Position
lead_x = 300
lead_y = 300
lead_x_change = 0
lead_y_change = 0

# Taking Pygame time clock
clock = pygame.time.Clock()

# Set Colours
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

pygame.display.set_caption("Old Snake"); #Set Title

while not gameClose:
    for event in pygame.event.get():
        print(event) # will get positions of mouse and buttons.
        if event.type == pygame.QUIT:
            gameClose = True
        
        # Checking for buttons being pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                lead_x_change = -10
                lead_y_change = 0
            elif event.key == pygame.K_RIGHT:
                lead_x_change = 10
                lead_y_change = 0
            
            elif event.key == pygame.K_UP:
                lead_y_change = -10
                lead_x_change = 0
            elif event.key == pygame.K_DOWN:
                lead_y_change = 10
                lead_x_change = 0

           
        lead_x += lead_x_change
        lead_y += lead_y_change

        if lead_x >= 800 or lead_x < 10 or lead_y >= 600 or lead_y < 0:
            gameClose = True


    clock.tick(30) # frame per second
    gameScreen.fill(black) # or a tuple ((255,255,255))
    pygame.draw.rect(gameScreen, white, (lead_x,lead_y,10,10)) # Where to place, fill colour, location and size in tuple or list
    # gameScreen.fill(red, rect=[200,200,50,50])  # Alternative to the above statement
    pygame.display.update()
# pygame.display.update() # Update the screen


pygame.quit()

#quit()