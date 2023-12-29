import pygame as pg
import os
import src.GloDec as g

class Score:
    def __init__(self):
        self.score: int = 0
        self.font: pg.font.Font = pg.font.SysFont('arial', 22, bold=False)
        self.x: int = g.score_x
        self.y: int = g.score_y
        self.color: tuple = g.score_color
    
    # Drawing the score on the screen
    def draw(self, screen: pg.Surface) -> None:
        score_text = self.font.render(f"Score: {self.score}", True, self.color)
        screen.blit(score_text, (self.x, self.y))

    # Increasing the score
    def increase_score(self) -> None:
        self.score += 1
        # Increasing the speed of the game as the score increases
        if self.score % 200 == 0:
            self.load_sound()
            self.sound.play()
            g.speed += 1
            g.bird_speed += 1

    # Resetting the score when the game is over
    def reset_score(self) -> None:
        self.score = 0

    # Updating the high score if the current score is greater than the high score
    def update_high_score(self) -> None:
        #self.load_sound()
        if self.score > self.current_high_score:
            self.current_high_score = self.score

    # Getting the current high score
    def get_high_score(self) -> int:
        return self.current_high_score
    
    # Loading the sound of score when high score is updated
    def load_sound(self) -> pg.mixer.Sound:
        self.sound = pg.mixer.Sound(os.path.join("assets", "Audio", "high_score.wav"))
        return self.sound
