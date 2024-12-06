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
            self.gameManager.get_card_bylist(player, ['AK47', 'kill', 'kill', 'heal'])
        # return None
        return self.game()

    def game(self):
        index = 0
        while True:
            if index > len(self.playerList)-1:
                index = 0
            self.change_turn(index)

            while True:
                target = self.gameManager.get_player(self.playerList[index])
                print(self.playerList[index],"turn")
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

                self.gameManager.use_card(self.playerList[index], aim, target.cards[int(usage)])

                for player in self.playerList:
                    if self.gameManager.playerList.get(player).health == 0:
                        self.playerList.remove(player)
                if len(self.playerList) == 1:
                    print(self.playerList[0], "wins")
                    return None
            index += 1

    def discard_phase(self, current_player_id):
        player = self.gameManager.playerList.get(current_player_id)
        print("Discard Phase: You must discard cards if your hand is more than your HP.")
        while len(player.cards) > player.health:
            discard_card = input(f"{len(player.cards)-player.health} left. Please enter the card you want to discard.")
            if discard_card not in player.cards:
                print("Invalid card.")
                continue
            player.cards.remove(discard_card)

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
