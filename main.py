import pygame as pg
from src.Game import Game

def main():
    pg.init()
    game = Game()
    game.run()

if __name__ == "__main__":
    main()