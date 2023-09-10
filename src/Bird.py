import os
import random
import pygame as pg
import src.GloDec as g

class Bird:

    Bird_heights: list = [125, 150, 160, 180]

    def __init__(self, x: int):
        self.x = x
        self.y = g.track_position - random.choice(self.Bird_heights)
        self.images = self.load_images()
        self.img = self.images[0]
        self.draw(g.screen)
        self.rect = self.img.get_rect()

        self.step_index: int = 0
        self.rect.x = x
        self.rect.y = self.y

    def draw(self, window: pg.Surface) -> None:
        window.blit(self.img, (self.x, self.y))

    def move(self) -> None:
        self.x -= g.bird_speed

        if self.step_index >= 40:
            self.step_index = 0

        self.img = self.images[self.step_index // 20]
        self.rect = self.img.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.step_index += 1

    def load_images(self) -> list:
        FLYING = [
            pg.transform.scale(pg.image.load(os.path.join("assets", "Bird", "Bird1.png")), (g.bird_width, g.bird_height)),
            pg.transform.scale(pg.image.load(os.path.join("assets", "Bird", "Bird2.png")), (g.bird_width, g.bird_height)),
        ]
        return FLYING

