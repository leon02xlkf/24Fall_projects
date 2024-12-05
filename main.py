"""
latest edited on Nov 7, 2024
author: Zhanchen Kang, Guanyi Wang

This is the main file of the entire project.
"""

import stage

if __name__ == "__main__":
    player_number = int(input("Please enter the number of players: "))
    game = stage.Game()
    winner = game.start(player_number)
    print("The winner is: Player", winner)