import pygame as pg
import os
import GloDec as g

class Cactus:
    def __init__(self, x):
        self.x = x
        self.y = g.track_position - g.cactus_height + 20
        self.img = self.load_image()
        self.draw(g.screen)

    # Drawing the cactus
    def draw(self, window):
        window.blit(self.img, (self.x, self.y))
    
    # Moving the cactus
    def move(self):
        self.x -= g.speed

    # Loading the image of the cactus
    def load_image(self):
        self.img = pg.image.load(os.path.join("assets", "Cactus", "LargeCactus1.png"))
        self.img = pg.transform.scale(self.img, (g.cactus_width, g.cactus_height))
        return self.img