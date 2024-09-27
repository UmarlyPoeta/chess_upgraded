# /home/patryk/projects/chess_upgraded/src/__init__.py
from game_model import Game
from colorama import init

init()

if __name__ == "__main__":
    game = Game()
    game.play()
