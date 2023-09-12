import pygame as pg
import os
import random
import src.GloDec as g

class Cactus:
    def __init__(self, x: int):
        self.x = x

        # Randomly choose between large and small cactus
        if random.randint(0, 1) == 0:
            self.img = random.choice(self.load_large_cactus())
            self.y = g.track_position - g.cactus_height
        else:
            self.img = random.choice(self.load_small_cactus())
            self.y = g.track_position - g.cactus_height + 20

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

    def collide(self, dinosaur: pg.Rect) -> bool:
        if dinosaur.colliderect(self.rect):
            return True
        return False

    # Loading the images of the cacti
    def load_large_cactus(self) -> list:
        LARGE_CACTI = [ pg.image.load(os.path.join('assets', 'Cactus', 'LargeCactus1.png')), 
         pg.image.load(os.path.join('assets', 'Cactus', 'LargeCactus2.png')), 
         pg.image.load(os.path.join('assets', 'Cactus', 'LargeCactus3.png'))
        ]
        return LARGE_CACTI
    
    def load_small_cactus(self) -> list:
        SMALL_CACTI = [ pg.image.load(os.path.join('assets', 'Cactus', 'SmallCactus1.png')), 
         pg.image.load(os.path.join('assets', 'Cactus', 'SmallCactus2.png')), 
         pg.image.load(os.path.join('assets', 'Cactus', 'SmallCactus3.png'))
        ]
        return SMALL_CACTI
