from basic.gameManager import gameManager
from basic.player import  player
from basic.ai_player import AI_player
import time

class AIgame:
    def __init__(self):
        self.gameManager = gameManager()
        self.playerList = []
        self.AI_player = None
        self.turn = 0

    def initialization(self):
        i = 1
        newplayer = player()
        self.gameManager.playerList[f"{i}"] = newplayer
        self.playerList.append(f"{i}")

        self.AI_player = AI_player()
        self.gameManager.playerList["2"] = self.AI_player
        self.playerList.append("2")

    def start(self):
        for player in self.playerList:
            self.gameManager.get_card_bynumber(player, 4)
        # return None
        return self.game()

    def game(self):
        index = 0
        self.turn = 1
        checker = None
        while True:
            if index > len(self.playerList)-1:
                index = 0
            self.change_turn(index)
            status = 1
            while True:
                target = self.gameManager.get_player(self.playerList[index])
                if self.turn == 1:
                    try:
                        print("\n", self.playerList[index], "turn")
                        print(target.cards)
                        print(target.equipment)
                        self.show_hp()
                        print("do what you want")
                        usage = input("card order:")

                        if usage == "q":
                            self.discard_phase(self.playerList[index])
                            break
                        elif usage == "v":
                            self.visualization()
                            continue
                        elif target.cards[int(usage)] == 'kill' or target.cards[int(usage)] == 'heal':
                            aim = input("target:")
                        else:
                            aim = self.playerList[index]
                    except IndexError:
                        print("incorrect index, check input")
                        continue
                else:
                    print("\nAI's turn")
                    print("calculating solutions")
                    time.sleep(10)
                    card = self.AI_player.analyze(checker, self.gameManager.get_player(self.playerList[0]).health, status)
                    if card != "q":
                        usage = self.AI_player.cards.index(card)
                    else:
                        self.discard_phase(self.playerList[index])
                        break
                    if card != "kill":
                        aim = self.playerList[index]
                    else:
                        aim = self.playerList[0]
                    print("AI used %s, towards %s"% (target.cards[int(usage)], aim))
                try:
                    checker = self.gameManager.use_card(self.playerList[index], aim, target.cards[int(usage)])[1]
                except Exception:
                    print("something wrong, check your input")
                    continue
                status = 1

                for player in self.playerList:
                    if self.gameManager.playerList.get(player).health == 0:
                        self.playerList.remove(player)
                if len(self.playerList) == 1:
                    print(self.playerList[0], "wins")
                    return None
            index += 1
            self.turn *= -1

    def discard_phase(self, target):
        if self.turn == 1:
            player = self.gameManager.playerList.get(target)
            print("Discard Phase: You must discard cards if your hand is more than your HP.")
            while len(player.cards) > player.health:
                print("your cards:", player.cards)
                discard_card = input(f"{len(player.cards)-player.health} left. Please enter the card you want to discard.")
                self.gameManager.drop_card_byorder(target, int(discard_card))
        else:
            player = self.gameManager.playerList.get(target)
            list = self.AI_player.analyze(True, self.gameManager.get_player(self.playerList[0]).health, 2)
            print("AI drops:", list)
            for card in list:
                player.cards.remove(card)


    def show_hp(self):
        for player in self.playerList:
            print("player%s: %d hp" % (player, self.gameManager.get_hp(player)))


    def change_turn(self, index):
        self.gameManager.get_card_bynumber(self.playerList[index], 2)

    def visualization(self):
        print("\n")
        for player in self.playerList:
            print("player no.",player)
            i = self.gameManager.playerList.get(player)
            print("hp:", i.health)
            print("cards:", i.cards)
            print("equipments:", i.equipment)
        print("\n")