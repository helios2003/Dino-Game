import pygame as pg

# Constants for the entire game
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 300
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
bg_color = (255, 255, 255)
speed = 2

# Track constants
track_position = 200
track_height = 50

# Cactus constants
cactus_width = 30
cactus_height = 70

# Cloud constants
cloud_width = 50
cloud_height = 30

# Display the screen
screen = pg.display.set_mode(SCREEN_SIZE)