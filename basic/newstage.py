from basic.gameManager import gameManager
from basic.player import  player

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
        self.turn = 1
        while True:
            if index > len(self.playerList) - 1:
                index = 0
            self.change_turn(index)
            while True:
                target = self.gameManager.get_player(self.playerList[index])
                try:
                    print(self.playerList[index], "turn")
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
                    print("something wrong, check your input")
                    continue

                try:
                    self.gameManager.use_card(self.playerList[index], aim, target.cards[int(usage)])
                except Exception:
                    print("something wrong, check your input")
                    continue

                for player in self.playerList:
                    if self.gameManager.playerList.get(player).health == 0:
                        self.playerList.remove(player)
                if len(self.playerList) == 1:
                    print(self.playerList[0], "wins")
                    return None
            index += 1


    def discard_phase(self, target):
        player = self.gameManager.playerList.get(target)
        print("Discard Phase: You must discard cards if your hand is more than your HP.")
        while len(player.cards) > player.health:
            print("your cards:", player.cards)
            discard_card = input(
                f"{len(player.cards) - player.health} left. Please enter the card you want to discard.")
            self.gameManager.drop_card_byorder(target, int(discard_card))

    def try_alchemy_as_kill(self, current_player_id):
        """
        当玩家输入“a”尝试通过alchemy技能出杀时自动使用前两张手牌为kill
        条件：已装备alchemy，手中无kill牌，手中至少有两张其他牌
        :param current_player_id:
        :return:
        """
        player_obj = self.gameManager.playerList.get(current_player_id)
        if player_obj.equipment["weapon"] != "alchemy":
            return False
        if "kill" in player_obj.cards:
            return False
        if len(player_obj.cards) < 2:
            return False
        chosen_cards = player_obj.cards[:2]
        for card in chosen_cards:
            player_obj.cards.remove(card)
        return True

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

