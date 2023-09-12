import pygame as pg
import os
import src.GloDec as g

class Die:
    def __init__(self, collided: bool):
        self.collided = collided
        if self.collided:
                self.draw(g.screen)

    def draw(self, window: pg.Surface) -> None:
        window.blit(self.img, (g.SCREEN_WIDTH // 2, g.SCREEN_HEIGHT // 2))

    def load_image(self) -> pg.Surface:
        self.img = pg.image.load(os.path.join('Assets', 'GameOver.png'))
        return self.img
        
    def play_sound(self):
        sound = pg.mixer.Sound(os.path.join('Assets', 'Audio', 'die.wav'))
        sound.play()
    
