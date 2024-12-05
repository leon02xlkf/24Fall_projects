from gameManager import gameManager
from player import  player

class game:
    def __init__(self):
        self.gameManager = gameManager()
        self.playerList = []

    def initialization(self, player_number):
        for i in range(0, player_number):
            newplayer = player()
            self.gameManager.playerList[f"{i}"] = newplayer
            self.playerList.append(f"{i}")

    def start(self):
        for player in self.playerList:
            self.gameManager.get_card_bynumber(player, 4)
        # return None
        return self.game()

    def game(self):
        index = 0
        while True:
            if index > len(self.playerList)-1:
                index = 0
            self.change_turn(index)

            while True:
                target = self.gameManager.playerList.get(self.playerList[index])
                print(self.playerList[index],"turn")
                print(target.cards)
                print(target.equipment)
                print("aliving player",self.playerList)
                print("do what you want")
                usage = input("card order:")
                aim = input("target:")

                print(self.playerList[index], aim, usage)
                if usage == "q":
                    break
                self.gameManager.use_card(self.playerList[index], aim, target.cards[int(usage)])

            for player in self.playerList:
                if self.gameManager.playerList.get(player).health == 0:
                    self.playerList.remove(player)
            if len(self.playerList) == 1:
                print(self.playerList[0], "wins")
                break
            index += 1


    def change_turn(self, index):
        self.gameManager.get_card_bynumber(self.playerList[index], 2)

    def visualization(self):
        for player in self.playerList:
            print(player)
            i = self.gameManager.playerList.get(player)
            print(i.health)
            print(i.cards)
            print(i.equipment)

game = game()

game.initialization(2)
game.start()
