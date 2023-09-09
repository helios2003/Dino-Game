import pygame as pg
import random
import GloDec as g
from Dinosaur import Dinosaur
from Cloud import Cloud
from Cactus import Cactus
from Track import Track
from Bird import Bird
from Score import Score

# Initialize pygame
pg.init()

# Set up the game window
screen = g.screen
pg.display.set_caption("Dinosaur Game")
clock = pg.time.Clock()

# Create game objects
dinosaur = Dinosaur(20)
track = Track(0)
score_display = Score(0)
clouds = [Cloud(random.randint(800, 1600)) for _ in range(3)]  # Randomize the initial cloud positions
cacti = [Cactus(random.randint(800, 1200)) for _ in range(3)]  # Randomize the initial cactus positions
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

    # Check for collisions with cacti
    for cactus in cacti:
        if dinosaur.rect.colliderect(cactus.rect):
            # Handle collision here, e.g., end the game or reset the score
            score_display.reset_score()
            running = False  # Stop the game when a collision occurs

    # Update cloud positions
    for cloud in clouds:
        cloud.move()
        if cloud.rect.right < 0:
            cloud.rect.x = g.SCREEN_WIDTH + random.randint(800, 1600)
            cloud.rect.y = g.track_position - random.choice(Cloud.Cloud_heights)

    # Update cactus positions
    for cactus in cacti:
        cactus.move()
        if cactus.rect.right < 0:
            cactus.rect.x = g.SCREEN_WIDTH + random.randint(800, 1200)
            cactus.rect.y = g.track_position - g.cactus_height + 10

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
