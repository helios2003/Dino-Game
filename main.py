import pygame as pg
import random
import src.GloDec as g
from src.Dinosaur import Dinosaur
from src.Cloud import Cloud
from src.Cactus import Cactus
from src.Bird import Bird
from src.Track import Track
from src.Score import Score
from src.Die import Die

# Initialize pygame
pg.init()

# Set up the game window
screen = g.screen
pg.display.set_caption("Dinosaur Game")
clock = pg.time.Clock()

# Create game objects
dinosaur = Dinosaur(30)
track = Track(0)
score_display = Score()
die = Die(False)  # Create Die object with initial collided state as False

# Initialize variables for component generation
cloud_timer = 0
cloud_frequency = random.randint(200, 400)
obstacle_timer = 0
obstacle_frequency = random.randint(200, 300)

# Lists to store clouds and obstacles (cacti and birds)
clouds = []
obstacles = []  # For cacti and birds

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # Update game objects
    keys = pg.key.get_pressed()
    dinosaur.update(keys)
    track.update()

    # Cloud generation
    if cloud_timer >= cloud_frequency:
        new_cloud = Cloud(g.SCREEN_WIDTH)
        clouds.append(new_cloud)
        cloud_timer = 0
        cloud_frequency = random.randint(200, 400)

    cloud_timer += 1

    # Obstacle generation (cacti and birds)
    if obstacle_timer >= obstacle_frequency:
        if not obstacles or obstacles[-1].x <= 250:
            # Ensure a minimum distance of 150 pixels between obstacles
            if random.randint(0, 1) == 0:
                new_obstacle = Cactus(g.SCREEN_WIDTH)
            else:
                new_obstacle = Bird(g.SCREEN_WIDTH)
            obstacles.append(new_obstacle)
            obstacle_timer = 0
            obstacle_frequency = random.randint(75, 100)

    obstacle_timer += 1

    # Check for collisions with obstacles
    for obstacle in obstacles:
        if obstacle.collide(dinosaur.rect):
            score_display.reset_score()
            die.collided = True  
            die.play_sound() 
            running = False 

    # Update positions of cacti and birds in the obstacles array
    for obstacle in obstacles:
        obstacle.move()
        if obstacle.rect.right < 0:
            obstacles.remove(obstacle)

    # Update cloud positions
    for cloud in clouds:
        cloud.move()
        if cloud.rect.right < 0:
            clouds.remove(cloud)

    # Renderings
    screen.fill(g.bg_color)
    track.draw(screen)
    for cloud in clouds:
        cloud.draw(screen)
    for obstacle in obstacles:
        obstacle.draw(screen)
    dinosaur.draw(screen)

    # Increase the score
    score_display.increase_score()

    # Draw the score on the screen
    score_display.draw(screen)

    pg.display.flip()
    clock.tick(60)

pg.quit()
