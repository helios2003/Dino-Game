import pygame as pg
import os
import src.GloDec as g

class Track:
    def __init__(self, x: int):
        self.x = x
        self.y = g.track_position
        self.speed = g.speed
        self.img = self.load_image()
        self.draw(g.screen)

    def load_image(self) -> pg.Surface:
        self.img = pg.image.load(os.path.join("assets", "Track.png"))
        self.img = pg.transform.scale(self.img, (g.SCREEN_WIDTH, g.track_height))
        return self.img

    def update(self) -> None:
        self.x -= g.speed
        if self.x <= -g.SCREEN_WIDTH:
            self.x = 0

    # To create the illusion of a never-ending track, we need to draw two images
    def draw(self, window: pg.Surface) -> None:
        window.blit(self.img, (self.x, self.y))
        window.blit(self.img, (self.x + g.SCREEN_WIDTH - 1, self.y))
