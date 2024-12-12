import random

from basic.player import player

class gameManager():
    card_dictionary = {
        # BasicCards
        "kill": ["basic", "cause damage to a player", 1, "kill"],
        "defend": ["basic", "defend 1 damage to a player", -1, "defend"],
        "heal": ["basic", "heal 1 hp to a player", 1, "heal"],

        # Weapons
        "AK47": ["weapon", "no limitation on using kill card", 1, "AK47"],
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
    card_type = ["kill", "defend", "heal", "AK47", "fireSupport", "doubleAttack"]
    weight = [30, 24, 12, 2, 1, 1]

    def __init__(self):
        self.playerList = {}

    def get_card_bynumber(self, target, number):
        """
        Draw cards from the system according to the given number.
        """
        for i in range(number):
            card_type = random.choices(self.card_type, weights=self.weight)
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

        source_player = self.playerList.get(source)
        target_player = self.playerList.get(target)

        if card_type == "kill":
            # 距离比较：武器攻击范围
            weapon_equipped = source_player.equipment["weapon"]
            if weapon_equipped is not None:
                weapon_range = self.card_dictionary[weapon_equipped][2]
            else:
                weapon_range = 1
            # 计算双方已装备horse的距离和
            distance_mod = 0
            if source_player.equipment["horse1"] is not None:
                distance_mod += 1
            if source_player.equipment["horse-1"] is not None:
                distance_mod -= 1
            if target_player.equipment["horse1"] is not None:
                distance_mod += 1
            if target_player.equipment["horse-1"] is not None:
                distance_mod -= 1
            final_distance = original_distance + distance_mod
            distance_permission = (weapon_range >= final_distance)

            # AK47
            if source_player.kill_limitation and source_player.kill >= 1:
                print("not valid kill due to used kill before")
                return None, False

            if not distance_permission:
                 print("not valid kill due to out of attack range")
                 return None, False
            source_player.kill += 1

            # 【已实现】doubleAttack: target无手牌时，kill造成二倍伤害
            if source_player.doubleAttack and len(target_player.cards) == 0:
                self.card_dictionary["kill"][2] = 2

        elif self.card_dictionary.get(card_type)[0] == "weapon":
            if self.check_weapon(target_player):
                self.remove_weapon(target_player)
            target_player.equipment["weapon"] = card_type

        elif self.card_dictionary.get(card_type)[0] == "defend":
            target_player.equipment["defend"] = card_type

        elif self.card_dictionary.get(card_type)[0] == "horse1":
            target_player.equipment["horse1"] = card_type

        elif self.card_dictionary.get(card_type)[0] == "horse2":
            target_player.equipment["horse2"] = card_type

        elif card_type == "heal":
            if target_player.health == target_player.maximum_health:
                print("not valid heal due to full hp")
                return None, False

        source_player.cards.remove(card_type)
        number = self.card_dictionary.get(card_type)[2]
        function = self.card_dictionary.get(card_type)[3]
        
        if self.check_defend(target_player) and card_type == "kill":
            number += self.use_card(target, target, "defend")[0]
            if source_player.fireSupport:
                source_player.kill -= 1

        method = getattr(self, function)
        print("\n%s used %s towards %s\n" % (source, card_type, target))
        return method(target_player, number), True

    def check_weapon(self, target:player):
        if target.equipment.get("weapon") != None:
            return True
        else:
            return False

    def remove_weapon(self, target:player):
        target.kill_limitation = True
        target.fireSupport = False
        target.doubleAttack = False

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
        card_type = player.cards[card_order]
        return self.drop_card(target, card_type)

    def calculate_distance(self, source, target):
        right_distance = abs(int(source) - int(target))
        left_distance = 1 + len(self.playerList) - max(int(source), int(target))
        distance = min(right_distance, left_distance)
        return distance

    def get_hp(self, target):
        target = self.playerList.get(target)
        hp = target.health
        return hp

    def get_player(self, target):
        return self.playerList.get(target)
    # ----------------------------------------------------------------------------------------------------------------
    def damage(self, target:player, number):
        target.health -= number
        return number

    # Method of cards
    def kill(self, target:player, number):
        return self.damage(target, number)

    def defend(self, target:player, number):
        return -1

    def heal(self, target:player, number):
        target.health += number
        pass

    def AK47(self, target:player, number):
        target.kill_limitation = False
        pass

    def alchemy(self, target:player, number):
        pass

    def fireSupport(self, target:player, number):
        target.fireSupport = True
        pass

    def doubleAttack(self, target:player, number):
        target.doubleAttack = True
        pass
