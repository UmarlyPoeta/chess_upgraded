# /home/patryk/projects/chess_upgraded/src/__init__.py
from colorama import init
from game_model import Game

init(autoreset=True)

if __name__ == "__main__":
    game = Game()
    game.play()
