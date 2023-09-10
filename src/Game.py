import pygame as pg
import random
import os
import src.GloDec as g
from src.Track import Track
from src.Dinosaur import Dinosaur
from src.Cloud import Cloud
from src.Cactus import Cactus
from src.Bird import Bird
from src.Score import Score

class Game:
    def __init__(self, high_score=0):
        self.track = Track(0)
        self.dinosaur = Dinosaur(20)
        self.running = False
        self.high_score = high_score
        #self.load_image()
        self.load_sound()
        self.clouds = [Cloud(random.randint(800, 1600)) for _ in range(3)]  # Randomize the initial cloud positions
        self.cacti = [Cactus(random.randint(800, 1200)) for _ in range(3)]  # Randomize the initial cactus positions
        self.bird = Bird(1200)

    def load_image(self):
        # Load game over and reset images
        self.game_over_img = pg.image.load(os.path.join("assets", "Utils", "GameOver.png"))
        self.reset_img = pg.image.load(os.path.join("assets", "Utils", "Reset.png"))

    # Load game over sound
    def load_sound(self):
        self.game_over_sound = pg.mixer.Sound(os.path.join("assets", "Audio", "die.wav"))

    def start_game(self):
        self.running = True

    def end_game(self):
        self.running = False
        self.play_game_over_sound()

    def play_game_over_sound(self):
        self.game_over_sound.play()

    def check_collisions(self):
        obstacles = self.clouds + self.cacti + [self.bird]
        for obstacle in obstacles:
            if self.dinosaur.rect.colliderect(obstacle.rect):
                self.end_game()

    def generate(self):
        # Generate new clouds when needed
        for cloud in self.clouds:
            if cloud.rect.right < 0:
                cloud.rect.x = g.SCREEN_WIDTH + random.randint(800, 1600)
                cloud.rect.y = g.track_position - random.choice(Cloud.Cloud_heights)

        # Generate new cacti when needed
        for cactus in self.cacti:
            if cactus.rect.right < 0:
                cactus.rect.x = g.SCREEN_WIDTH + random.randint(800, 1200)
                cactus.rect.y = g.track_position - g.cactus_height + 10

        # Generate a new bird when needed
        if self.bird.rect.right < 0:
            self.bird.rect.x = g.SCREEN_WIDTH
            self.bird.rect.y = random.randint(100, 150)

    def update(self, keys):
        if self.running:
            self.dinosaur.update(keys)
            self.track.update()
            self.generate()  # Call the generate method to create new objects
            self.check_collisions()  # Check for collisions with obstacles

    def reset(self):
        self.dinosaur.reset()
        self.track.reset()
        self.running = False
