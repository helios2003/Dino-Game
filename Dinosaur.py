import pygame as pg
import os
import GloDec as g

class Dinosaur:
    def __init__(self, x: int):
        # Load the assets of the dinosaur
        self.duck_img = self.load_ducking_image()
        self.run_img = self.load_running_images()
        self.jump_img = self.load_jump_image()
        self.sound = self.load_sound()

        # By default we want the dinosaur to be only running
        self.is_running: bool = True
        self.is_jumping: bool = False
        self.is_ducking: bool = False

        # step_index is used to cycle through the images of the dinosaur
        self.step_index: int = 0
        self.img: pg.Surface = self.run_img[0] # default image
        self.jump_velocity: int = g.jump_velocity

        # The rect attribute is used to detect collisions
        self.x = x
        self.y = g.track_position - g.dino_height + 15
        self.rect: pg.Rect = self.img.get_rect()
        self.rect.x: int = g.dino_width
        self.rect.y: int = g.dino_height

    # The duck method is used to make the dinosaur duck in presence of a bird
    def duck(self) -> None:
        self.img = self.duck_img[self.step_index // 5]
        self.rect = self.img.get_rect()
        self.x = g.dino_duck_width
        self.y = g.track_position - g.dino_duck_height + 15
        self.rect.x = g.dino_duck_width
        self.rect.y = g.dino_duck_height
        self.step_index += 1

    # The run method is used to make the dinosaur run by default
    def run(self) -> None:
        self.img = self.run_img[self.step_index // 5]
        self.rect = self.img.get_rect()
        self.rect.x = g.dino_width
        self.rect.y = g.dino_height
        self.step_index += 1

    # The jump method is used to make the dinosaur jump if a cactus is present
    def jump(self) -> None:
        self.img = self.jump_img
        if self.is_jumping:
            self.y -= self.jump_velocity  # Decreasing the y-coordinate
            self.rect.y = self.y
            self.jump_velocity -= g.gravity  # Decreasing the velocity while moving up

        # If we have reached the ground
        if self.jump_velocity < -g.jump_velocity: 
            self.is_jumping = False
            self.jump_velocity = g.jump_velocity

    # The update method is used to update the dinosaur's state based on the helper methods
    def update(self, Key: dict) -> None:
        if self.is_ducking:
            self.duck()
        elif self.is_running:
            self.run()
        elif self.is_jumping:
            self.sound.play()
            self.jump()

        if self.step_index >= 10:
            self.step_index = 0

        if Key[pg.K_UP] and self.is_jumping is False:
            self.is_jumping = True
            self.is_ducking = False
            self.is_running = False

        elif Key[pg.K_DOWN] and self.is_ducking is False:
            self.is_jumping = False
            self.is_ducking = True
            self.is_running = False

        elif not ((self.is_jumping is True or Key[pg.K_DOWN]) or (self.is_ducking is True or Key[pg.K_UP])):
            self.is_jumping = False
            self.is_ducking = False
            self.is_running = True

    # Drawing the dinosaur on the screen
    def draw(self, window: pg.Surface) -> None:
        window.blit(self.img, (self.x, self.y))

    # Loading the images of the dinosaur
    def load_jump_image(self) -> pg.Surface:
        JUMPING = pg.transform.scale(pg.image.load(os.path.join("assets", "Dino", "DinoJump.png")), (g.dino_width, g.dino_height))
        return JUMPING

    def load_ducking_image(self) -> list:
        DUCKING = [
            pg.transform.scale(pg.image.load(os.path.join("assets", "Dino", "DinoDuck1.png")), (g.dino_duck_width, g.dino_duck_height)),
            pg.transform.scale(pg.image.load(os.path.join("assets", "Dino", "DinoDuck2.png")), (g.dino_duck_width, g.dino_duck_height))
        ]
        return DUCKING

    def load_running_images(self) -> list:
        RUNNING = [
            pg.transform.scale(pg.image.load(os.path.join("assets", "Dino", "DinoRun1.png")), (g.dino_width, g.dino_height)),
            pg.transform.scale(pg.image.load(os.path.join("assets", "Dino", "DinoRun2.png")), (g.dino_width, g.dino_height))
        ]
        return RUNNING

    # Loading the sound of the dinosaur jumping
    def load_sound(self) -> pg.mixer.Sound:
        self.sound = pg.mixer.Sound(os.path.join("assets", "Audio", "jump.wav"))
        return self.sound
