import pygame as pg
from src.Game import Game
import asyncio

async def main():
    pg.init()
    game = Game()
    await asyncio.sleep(0)
    await game.run()  

if __name__ == "__main__":
    asyncio.run(main())  
