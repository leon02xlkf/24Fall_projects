class player:
    def __init__(self):
        self.card = list()
        self.health = int()
        self.equipment = {"weapon": None,
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
        pass

    def use_card(self, card, target):
        """
        使用卡的方法，跟上面一样，直接指定卡牌类型，target负责瞄准一个玩家。
        :param card:
        :param target:
        :return:
        """
        if card.description == "cause damage to a player": # 使用“杀”
            if self.kill_used_this_turn:
                if distance <= 1: #TODO: 考虑双方之间距离（horse问题，此处distance如何计算）
                    if not self.equipment.get("weapon"):
                        #TODO: 使用“杀”时装备武器的情况
                    else: #未装备武器的情况
                        if "defend" not in target.card: #受到伤害的玩家手牌中没有defend
                            target.health_change(-1)
                        else: #受到伤害的玩家手牌中有defend，则不扣除生命，移除这张defend
                            target.card.remove("defend")
        elif card.description == "recover 1 health to a player": # 使用“桃”
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

    def drop_card(self, cards: list):
        """
        跟获取卡牌一样，用这个方法来弃牌。
        :param cards:
        :return:
        """
        if len(self.card) > self.health:
            cards_to_drop = len(self.card) - self.health #按照现有生命值确定弃牌数
        # TODO: 按照数目如何选择弃哪几张牌
        pass