import os, sys, pygame, random, array

from pygame.locals import *

# Base variables
traffic_count = 45
center_w = -1
center_h = -1

# Main Function
def main():
    clock = pygame.time.Clock()
    running = True
    font = pygame.font.Font(None, 24)

    # Create sprites

    map_s = pygame.sprite.Group()
    player_s = pygame.sprite.Group()
    traffic_s = pygame.sprite.Group()
    tracks_s = pygame.sprite.Group()
    target_s = pygame.sprite.Group()
    pointer_s = pygame.sprite.Group()

    # Initialisation