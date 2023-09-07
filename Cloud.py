import pygame as pg
import os
import GloDec as g

class Cloud:
    def __init__(self, x):
        self.x = x
        self.y = g.track_position - 150
        self.img = self.load_image()
        self.draw(g.screen)

    def draw(self, window):
        window.blit(self.img, (self.x, self.y))

    def move(self):
        self.x -= g.speed

    def load_image(self):
        self.img = pg.image.load(os.path.join("assets", "Cloud", "Cloud.png"))
        return self.img