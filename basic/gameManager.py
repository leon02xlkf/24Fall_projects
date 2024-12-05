import random

from pyqtgraph.exceptionHandling import original_excepthook

from player import player
"""
我在这里加了一点小小的dictionary为了调整和规范卡牌的使用，避免后续出现超级大的bug
所有的卡牌现在可以直接在card_dictionary这个里面写进去，然后调用对应的卡牌方法了，避免了每次有新的卡都需要声明一次卡牌的尴尬问题

所有的卡牌使用都需要通过use_card()这个方法，所以请务必保证除了这个方法之外其他的方法死都不会使用卡牌。
"""
class gameManager():
    # 原游戏中锦囊牌
    # 乐不思蜀：对任意玩家使用。目标角色在其下一回合开始阶段进行判定，若不是红桃花色则跳过出牌阶段
    # 闪电：对自己使用。在下个判定阶段时开始结算，目标角色进行一次判定，若为黑桃2~9则造成三点伤害，否则移入下家判定区
    # 决斗：对除自己外玩家使用。由目标角色先开始，自己和对方打出一张杀。决斗对首先不出杀的一方造成1点伤害
    # 借刀杀人：对除自己以外装备区里有武器牌的角色使用。该角色需对其攻击范围内，由自己指定的另一名角色使用一张杀，否则自己获得该角色装备区里的武器牌。
    # 过河拆桥：对除自己以外的任意一名有牌的角色使用。选择并弃置该角色的一张牌（装备/手牌）
    # 顺手牵羊：对除自己以外的距离1以内且有牌的一名角色使用。选择并获得该角色的一张牌（装备/手牌）
    # 无中生有：对自己使用。摸两张牌
    # 桃园结义：对所有玩家使用。各加一点体力
    # 无懈可击：在目标锦囊生效前，抵消其对一名角色产生的效果
    # 兵粮寸断：对除自己以外的距离1以内的一名角色使用。兵粮寸断于该角色判定阶段开始结算，若不为梅花，则跳过该角色摸牌阶段
    # 火攻：对任意一名有手牌的角色使用。目标角色展示一张手牌，若自己能弃掉一张与所展示牌相同花色的手牌，则火攻对该角色造成1点火焰伤害
    card_dictionary = {
        # BasicCards
        "kill": ["basic", "cause damage to a player", 1, "kill"],
        "defend": ["basic", "defend 1 damage to a player", 1, "defend"],
        "heal": ["basic", "heal 1 hp to a player", 1, "heal"],

        # Weapons
        "AK47": ["weapon", "no limitation on using kill card", 1, "AK47"],
        "APAmmunition": ["weapon", "cause the damage with ignoring the defend equipment", 2, "APAmmunition"],
        "alchemy": ["weapon", "using two cards as a kill", 3, "alchemy"],
        "extraAmmunition": ["weapon",
                            "when a player used a defend to avoid damage, you can drop 2 cards to make the damage cause",
                            3, "extraAmmunition"],
        "fireSupport": ["weapon", "when a player used a defend to avoid damage, you can use another kill", 3,
                        "fireSupport"],
        "surgeryAttack": ["weapon",
                          "you cause damage to a player, you can destroy a horse for the player",
                          3, "surgeryAttack"],
        "doubleAttack": ["weapon",
                         "if a player has no cards, cause double damage on the player",
                         3, "doubleAttack"],

        # Horses (defend是+1马, attack是-1马)
        "defendHorse": ["horse1", "increase the distance between players by 1", 1, "defendHorse"],
        "attackHorse": ["horse-1", "reduce the distance between players by 1", -1, "attackHorse"]

    }
    card_type = ["kill", "defend", "heal", "AK47", "APAmmunition", "alchemy", "extraAmmunition", "fireSupport",
                 "surgeryAttack", "doubleAttack"]
    weight = [30, 24, 12, 2, 1, 1, 1, 1, 1, 1]

    def __init__(self):
        self.playerList = {}

    def get_card_bynumber(self, target, number):
        """
        giving a player several random generated cards
        通过指定数字来随机生成若干个卡牌，之后给某一个玩家的方法。
        :param target:
        :param number:
        :return:
        """
        for i in range(0, number):
            card_type = random.choices(list(self.card_dictionary.keys()), weights=self.weight)
            self.get_card(target, card_type[0])

    def get_card_bylist(self,target, card_list):
        """
        giving a player one list of specific cards
        通过指定卡牌，类型和数量，直接吧card_list里面的卡全给某一个玩家的方法
        :param target:
        :param card_list:
        :return:
        """
        for card in card_list:
            self.get_card(target, card)

    def get_card(self, target, card_type):
        """
        giving a player 1 specific card, everything to do with get a card must be done with this function
        通过指定卡牌类型，把固定1张卡牌给指定玩家的方法
        所有关于获取卡牌的方法请务必通过该方法给指定玩家卡牌，请死都不要用其他的方法给
        :param target: target player， 目标玩家
        :param card_type: card_type, 卡牌类型
        :return:
        """
        target = self.playerList.get(target)
        target.cards.append(card_type)

    def use_card(self, source, target, card_type):
        """
        基础的使用卡牌的方法，所有对于用卡的修改都应该在这里
        只有这个方法可以用卡牌，其他的方法请死都不要动卡牌，不然要出问题了
        The basic function for using a card
        please modify only in this function when there is something to do with use a card
        :param source: who is using the card, 用卡的人
        :param target: who is the card's target, 被用卡的人
        :param card_type: card_type, 卡片类型
        :return: the number if there is something to do with damage
        """
        # 双方基础环形距离，调用calculate_distance计算
        original_distance = self.calculate_distance(source, target)

        source = self.playerList.get(source)
        target = self.playerList.get(target)

        if card_type == "kill":
            # 补充：距离比较
            # 武器攻击范围
            weapon_equipped = source.equipment["weapon"]
            if weapon_equipped is not None:
                weapon_range = self.card_dictionary[weapon_equipped][2]
            else:
                weapon_range = 1
            # 计算双方已装备horse的距离和
            distance_mod = 0
            if source.equipment["horse1"] is not None:
                distance_mod += 1
            if source.equipment["horse-1"] is not None:
                distance_mod -= 1
            if target.equipment["horse1"] is not None:
                distance_mod += 1
            if target.equipment["horse-1"] is not None:
                distance_mod -= 1
            final_distance = original_distance + distance_mod
            distance_permission = (weapon_range <= final_distance)

            # AK47
            if source.kill_limitation and source.kill == 1:
                print("not valid kill")
                return None

            if not distance_permission:
                 print("not valid kill")
                 return None
            source.kill += 1

            # 【已实现】doubleAttack: target无手牌时，kill造成二倍伤害
            if source.doubleAttack and len(target.cards) == 0:
                self.card_dictionary["kill"][2] = 2



        elif self.card_dictionary.get(card_type)[0] == "weapon":
            self.playerList.get(target).equipment["weapon"] = card_type
        elif self.card_dictionary.get(card_type)[0] == "defend":
            self.playerList.get(target).equipment["defend"] = card_type
        elif self.card_dictionary.get(card_type)[0] == "horse1":
            self.playerList.get(target).equipment["horse1"] = card_type
        elif self.card_dictionary.get(card_type)[0] == "horse2":
            self.playerList.get(target).equipment["horse2"] = card_type
        source.cards.remove(card_type)
        number = self.card_dictionary.get(card_type)[2]
        function = self.card_dictionary.get(card_type)[3]
        
        if self.check_defend(target) and card_type == "kill":
            number += self.use_card(target, target, "defend")
            # 【未实现】fireSupport: 若对方打出一张闪，则下次可以继续出杀
            #  source方连续打出两张kill，如何控制在同一回合？）
            if source.fireSupport:
                source.kill -= 1

        method = getattr(self, function)
        return method(target, number)

    def check_defend(self, target):
        cards = target.cards
        defend = 0
        for card in cards:
            if card == "defend":
                defend += 1

        return defend != 0

    def drop_card(self, target, card_type):
        target = self.playerList.get(target)
        target.cards.remove(card_type)
        return -1

    def drop_card_byorder(self, target, card_order):
        player = self.playerList.get(target)
        card_type = player.cards[card_order-1]
        return self.drop_card(target, card_type)

    def calculate_distance(self, source, target):
        right_distance = abs(int(source) - int(target))
        left_distance = 1 + len(self.playerList) - max(int(source), int(target))
        distance = min(right_distance, left_distance)
        return distance

    # ----------------------------------------------------------------------------------------------------------------
    def damage(self, target:player, number):
        target.health -= number
        return number

    # Method of cards
    def kill(self, target:player, number):
        return self.damage(target, number)

    def defend(self, target:player, number):
        """
        好像没什么用的方法
        :param target:
        :param number:
        :return:
        """
        return -1

    def heal(self, target:player, number):
        target.health += number
        pass

    def AK47(self, target:player):
        target.kill_limitation = False
        pass

    def APAmmunition(self, target:player, number):
        pass

    def alchemy(self, target:player, number):
        pass

    def extraAmmunition(self, target:player, number):
        pass

    def fireSupport(self, target:player, number):
        target.fireSupport = True
        pass

    def surgeryAttack(self, target:player, number):
        pass

    def doubleAttack(self, target:player):
        target.doubleAttack = True
        pass


if __name__ == "__main__":
    gm = gameManager()
    gm.get_card_bylist("1", ['kill', 'heal', 'kill', 'APAmmunition', "AK47"])
    gm.get_card_bylist("2", ['kill', 'defend', "defend", 'AK47'])

    gm.use_card("1", "1", "AK47")
    print(gm.playerList.get("1").equipment)
    print(gm.playerList.get("1").health, gm.playerList.get("1").cards)
    print(gm.playerList.get("2").health, gm.playerList.get("2").cards)

    gm.use_card("1", "2", "kill")
    gm.use_card("1", "2", "kill")
    print(gm.playerList.get("1").health, gm.playerList.get("1").cards)
    print(gm.playerList.get("2").health, gm.playerList.get("2").cards)