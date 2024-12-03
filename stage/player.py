class player:
    def __init__(self):
        self.card = list()
        self.health = int()
        self.equipment = {"weapon": None,
                          "horse1": None,
                          "horse2": None}

    def get_card(self, cards: list):
        """
        获取卡的方法，用这个方法把抽卡获得的卡放到self.card里面。
        参数cards直接用list表明获得了什么卡
        :param cards:
        :return:
        """
        pass

    def use_card(self, card, target):
        """
        使用卡的方法，跟上面一样，直接指定卡牌类型，target负责瞄准一个玩家。
        :param card:
        :param target:
        :return:
        """
        pass

    def health_change(self, number):
        """
        用这个方法来扣血或者回血
        :param number:
        :return:
        """
        pass

    def drop_card(self, cards: list):
        """
        跟获取卡牌一样，用这个方法来弃牌。
        :param cards:
        :return:
        """
        pass