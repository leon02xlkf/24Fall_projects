"""
latest edited on Nov 7, 2024
author: Zhanchen Kang, Guanyi Wang

This is the main file of the entire project.
"""

from basic.stage import game

if __name__ == "__main__":
    game = game()

    game.initialization(2)
    game.start()