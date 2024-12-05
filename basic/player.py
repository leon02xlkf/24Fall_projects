import random
class pp():
    def __init__(self):
        self.maximum_health = 3
        self.health = 3
        self.cards = []
        self.equipment = {"weapon": None,
                          "defend": None,
                          "horse1": None,
                          "horse2": None}



class player:
    def __init__(self, name):
        self.name = name
        self.card = list()
        self.health = int()
        self.equipment = {"weapon": None,
                          "defend": None,
                          "horse1": None,
                          "horse2": None}
        self.kill_used_this_turn = False #玩家本回合是否已经使用过了“杀”

    def get_card(self, cards: list):
        """
        获取卡的方法，用这个方法把抽卡获得的卡放到self.card里面。
        参数cards直接用list表明获得了什么卡
        :param cards:
        :return:
        """
        self.card.extend(cards)

    def use_card(self, card, target):
        """
        使用卡的方法，跟上面一样，直接指定卡牌类型，target负责瞄准一个玩家。
        :param card:
        :param target:
        :return:
        """
        if card.description == "cause damage to a player": # 使用kill
            if self.kill_used_this_turn:
                if distance_condition: #TODO: 距离条件（weapon距离大于horse距离）
                    if "defend" not in target.card: #受到伤害的玩家手牌中没有defend
                        target.health_change(-1)
                    else: #受到伤害的玩家手牌中有defend，则不扣除生命，移除一张defend
                        target.card.remove("defend")
            self.kill_used_this_turn = True
        elif card.description == "recover 1 health to a player": # 使用heal
            target.health_change(1)
        else:
            # TODO: 使用锦囊牌（skillcards）
            pass

    def health_change(self, number):
        """
        用这个方法来扣血或者回血
        :param number:
        :return:
        """
        self.health += number
        return number

    def drop_card_byNumber(self, cards_drop_num):
        """
        跟获取卡牌一样，用这个方法来弃牌。
        :param cards:
        :return:
        """
        for i in range(0, cards_drop_num):
            self.card.remove(random.choice(self.card))

    def drop_card_byCard(self, card_list:list):
        for card in card_list:
            self.card.remove(card)
