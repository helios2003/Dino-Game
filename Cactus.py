import pygame as pg
import os
import GloDec as g

class Cactus:
    def __init__(self, x: int):
        self.x = x
        self.y = g.track_position - g.cactus_height + 20
        self.img = self.load_image()
        self.draw(g.screen)
        self.rect = self.img.get_rect()
        self.rect.x = x
        self.rect.y = self.y

    # Drawing the cactus
    def draw(self, window: pg.Surface) -> None:
        window.blit(self.img, (self.x, self.y))
    
    # Moving the cactus
    def move(self) -> None:
        self.x -= g.speed
        self.rect.x = self.x

    # Loading the image of the cactus
    def load_image(self) -> pg.Surface:
        self.img = pg.image.load(os.path.join("assets", "Cactus", "LargeCactus1.png"))
        self.img = pg.transform.scale(self.img, (g.cactus_width, g.cactus_height))
        return self.img
