import pygame as pg
import os
import random
import GloDec as g

class Cloud:
    Cloud_heights: list = [150, 175, 200, 225]

    def __init__(self, x: int):
        self.x = x
        self.y = g.track_position - random.choice(self.Cloud_heights)
        self.img = self.load_image()
        self.draw(g.screen)
        self.rect = self.img.get_rect()
        self.rect.x = x
        self.rect.y = self.y

    # Drawing the cloud
    def draw(self, window: pg.Surface) -> None:
        window.blit(self.img, (self.x, self.y))
        #window.blit(self.img, (self.x + g.SCREEN_WIDTH - 1, self.y))

    # Moving the cloud
    def move(self) -> None:
        self.x -= g.speed
        self.rect.x = self.x

    # Loading the image of cloud
    def load_image(self) -> pg.Surface:
        self.img = pg.image.load(os.path.join("assets", "Cloud", "Cloud.png"))
        return self.img
