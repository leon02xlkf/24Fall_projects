"""
latest edited on Nov 7, 2024
author: Zhanchen Kang, Guanyi Wang

This is the main file of the entire project.
"""

from basic.newstage import game
from basic.AI_player_stage import AIgame

def function():
    return -1, 2

if __name__ == "__main__":
    while True:
        print("welcome to the \"War of Three kingdom\" game system!")
        print("several errors are fixed, however, there will be more")
        print("use the choices below to enter the game:")
        print("1 for self play, to play against yourself")
        print("2 for play with a basic AI")
        print("q for quit")
        commend = input("commend:")
        if commend == "1":
            print("use the index as python does to use and drop the card")
            print("you can always input \'q\' to get to the dropping card stage")
            print("you can always input \'v\' to see every parameter in the game")
            game = game()
            game.initialization(2)
            game.start()
        elif commend == "2":
            print("use the index as python does to use and drop the card")
            print("you can always input \'q\' to get to the dropping card stage")
            print("you can always input \'v\' to see every parameter in the game")
            game = AIgame()
            game.initialization()
            game.start()
        elif commend == "q":
            exit(0)
        else:
            continue