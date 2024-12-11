"""
author: Zhanchen Kang, Guanyi Wang

This is the main file of the entire project.
"""

from basic.newstage import game
from basic.AI_player_stage import AIgame

def function():
    return -1, 2

if __name__ == "__main__":
    """
    This part will run the game based on the mode given by the user.
    """
    while True:
        print("***** Welcome to the \"War of Three Kingdoms\" game! *****")
        print("1 --- Player vs. Player")
        print("2 --- Player vs. Computer")
        print("Q --- Quit")
        command = input("Please enter your choice:")
        if command == "1":
            print("\nEnter the index of the card to use/drop it (Start from 0).")
            print("q --- move on to the discarding phase")
            print("v --- show detailed information about the game in progress")
            game = game()
            game.initialization(2)
            game.start()
        elif command == "2":
            print("\nEnter the index of the card to use/drop it (Start from 0).")
            print("q --- move on to the discarding phase")
            print("v --- show detailed information about the game in progress")
            game = AIgame()
            game.initialization()
            game.start()
        elif command == "Q":
            exit(0)
        else:
            continue