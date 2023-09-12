import pygame as pg
import os
import src.GloDec as g

class Die:
    def __init__(self, collided: bool):
        self.collided = collided
        if self.collided:
                self.load_sound().play()

    def draw(self, window: pg.Surface) -> None:
        window.blit(self.img, (g.SCREEN_WIDTH // 2, g.SCREEN_HEIGHT // 2))

    def load_image(self) -> pg.Surface:
        self.img = pg.image.load(os.path.join('assets', 'GameOver.png'))
        return self.img
        
    def load_sound(self):
        self.sound = pg.mixer.Sound(os.path.join('assets', 'Audio', 'die.wav'))
        return self.sound
    