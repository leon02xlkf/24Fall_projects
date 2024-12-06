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
            self.gameManager.get_card_bylist(player, ['surgeryAttack', 'kill', 'kill'])
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
                self.show_hp()
                print("do what you want")
                usage = input("card order:")
                aim = input("target:")

                if usage == "q":
                    break
                elif usage == "v":
                    self.visualization()
                    continue
                # print(self.playerList[index], aim, target.cards[int(usage)])
                # print(self.gameManager.playerList.get(self.playerList[index]))
                self.gameManager.use_card(self.playerList[index], aim, target.cards[int(usage)])

            for player in self.playerList:
                if self.gameManager.playerList.get(player).health == 0:
                    self.playerList.remove(player)
            if len(self.playerList) == 1:
                print(self.playerList[0], "wins")
                break
            index += 1

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

game = game()

game.initialization(2)
game.start()
