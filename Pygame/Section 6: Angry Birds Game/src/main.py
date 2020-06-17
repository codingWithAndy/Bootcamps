import os
import sys

import math
import pygame

import time

import pymunk as pm 

pygame.init()

screen = pygame.display.set_mode((1200,650))

red_bird = pygame.image.load('Section 6: Angry Birds Game/resources/images/red-bird3.png').convert_alpha() # convert_alpha removes background  /Users/Andy/Developer/Bootcamps/Pygame/Section 6: Angry Birds Game
background = pygame.image.load('Section 6: Angry Birds Game/resources/images/background3.png').convert_alpha()
sling_image = pygame.image.load('Section 6: Angry Birds Game/resources/images/sling-3.png').convert_alpha()

full_sprite = pygame.image.load('Section 6: Angry Birds Game/resources/images/full-sprite.png').convert_alpha()
