import pygame as pg
import random
import src.GloDec as g
from src.Dinosaur import Dinosaur
from src.Cloud import Cloud
from src.Cactus import Cactus
from src.Track import Track
from src.Bird import Bird
from src.Score import Score

# Initialize pygame
pg.init()

# Set up the game window
screen = g.screen
pg.display.set_caption("Dinosaur Game")
clock = pg.time.Clock()

# Create game objects
dinosaur = Dinosaur(30)
track = Track(0)
score_display = Score(0)

# Initialize variables for component generation
cloud_timer = 0
cloud_frequency = random.randint(200, 400)
cactus_timer = 0
cactus_frequency = random.randint(200, 300)

# Lists to store components
clouds = []
cacti = []

# Bird
bird = Bird(1200)

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

    # Cactus generation
    if cactus_timer >= cactus_frequency:
        new_cactus = Cactus(g.SCREEN_WIDTH)
        cacti.append(new_cactus)
        cactus_timer = 0
        cactus_frequency = random.randint(200, 300)

    cactus_timer += 1

    # Update cloud positions
    for cloud in clouds:
        cloud.move()
        if cloud.rect.right < 0:
            clouds.remove(cloud)

    # Update cactus positions
    for cactus in cacti:
        cactus.move()
        if cactus.rect.right < 0:
            cacti.remove(cactus)

    # Update bird position
    bird.move()
    if bird.rect.right < 0:
        bird.rect.x = g.SCREEN_WIDTH
        bird.rect.y = random.randint(100, 150)

    # Renderings
    screen.fill(g.bg_color)
    track.draw(screen)
    bird.draw(screen)
    for cloud in clouds:
        cloud.draw(screen)
    for cactus in cacti:
        cactus.draw(screen)
    dinosaur.draw(screen)

    # Increase the score
    score_display.increase_score()

    # Draw the score on the screen
    score_display.draw(screen)

    pg.display.flip()
    clock.tick(60)

pg.quit()
