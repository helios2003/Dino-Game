import pygame as pg
import random
import asyncio
import src.GloDec as g
from src.Dinosaur import Dinosaur
from src.Cloud import Cloud
from src.Cactus import Cactus
from src.Bird import Bird
from src.Track import Track
from src.Score import Score
from src.Die import Die

class Game:
    def __init__(self):
        # Set up the game window and caption
        self.screen: pg.Surface = g.screen
        pg.display.set_caption("Dinosaur Game")
        self.clock: pg.time.Clock = pg.time.Clock()

        # Create game objects
        self.dinosaur: Dinosaur = Dinosaur(30)
        self.track: Track = Track(0)
        self.score: Score = Score()
        self.die: Die = Die(False)

        self.cloud_timer: int = 0
        self.cloud_frequency: int = random.randint(50, 200)
        self.obstacle_timer: int = 0
        self.obstacle_frequency: int = random.randint(75, 100)

        # Lists to store clouds and obstacles (cacti and birds)
        self.clouds: list[Cloud] = []
        self.obstacles: list = []
        self.running: bool = True
        self.paused: bool = False

    # Main game loop
    async def run(self) -> None:
        while self.running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        self.toggle_pause()

            if not self.paused:
                # Update game objects
                keys = pg.key.get_pressed()
                self.dinosaur.update(keys)
                self.track.update()

                # Cloud generation
                if self.cloud_timer >= self.cloud_frequency:
                    new_cloud = Cloud(g.SCREEN_WIDTH)
                    self.clouds.append(new_cloud)
                    self.cloud_timer = 0
                    self.cloud_frequency = random.randint(100, 250)

                self.cloud_timer += 1

                # Obstacle generation (cacti and birds)
                if self.obstacle_timer >= self.obstacle_frequency:
                    if not self.obstacles or self.obstacles[-1].x <= 250:
                        # Ensure a minimum distance of 150 pixels between obstacles
                        if random.randint(0, 1) == 0:
                            new_obstacle = Cactus(g.SCREEN_WIDTH)
                        else:
                            new_obstacle = Bird(g.SCREEN_WIDTH)
                        self.obstacles.append(new_obstacle)
                        self.obstacle_timer = 0
                        self.obstacle_frequency = random.randint(75, 100)

                self.obstacle_timer += 1

                # Check for collision with obstacles
                for obstacle in self.obstacles:
                    if pg.Rect.colliderect(self.dinosaur.rect, obstacle.rect):
                        self.handle_collision()

                # Update obstacle positions and remove them if they are off the screen
                for obstacle in self.obstacles:
                    obstacle.move()
                    if obstacle.rect.right < 0:
                        self.obstacles.remove(obstacle)

                # Update cloud positions
                for cloud in self.clouds:
                    cloud.move()
                    if cloud.rect.right < 0:
                        self.clouds.remove(cloud)

                # Renderings
                self.screen.fill(g.bg_color)
                self.track.draw(self.screen)
                for cloud in self.clouds:
                    cloud.draw(self.screen)
                for obstacle in self.obstacles:
                    obstacle.draw(self.screen)
                self.dinosaur.draw(self.screen)

                # Increase the score
                self.score.increase_score()
                self.score.draw(self.screen)

                pg.display.flip()
                self.clock.tick(60)
            await asyncio.sleep(0)

        pg.quit()

    # Toggle the pause state of the game
    def toggle_pause(self) -> None:
        self.paused = not self.paused

    # Handle collision with obstacles
    def handle_collision(self) -> None:
        self.score.reset_score()
        self.die.collided = True
        self.running = False
