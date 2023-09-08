import pygame as pg

# Constants for the entire game
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 400
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
bg_color = (255, 255, 255)
speed = 2

# Dinosaur constants
dino_width = 70
dino_height = 75
dino_duck_height = 50
dino_duck_width = 75
jump_velocity = 8
gravity = 0.5

# Track constants
track_position = 300
track_height = 25

# Score constants
score_color = (0, 0, 0)
score_x = 1025
score_y = 20

# Bird constants
bird_width = 70
bird_height = 50
bird_speed = 5

# Cactus constants
cactus_width = 30
cactus_height = 70

# Cloud constants
cloud_width = 50
cloud_height = 30

# Display the screen
screen = pg.display.set_mode(SCREEN_SIZE)