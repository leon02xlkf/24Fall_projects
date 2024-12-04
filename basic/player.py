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
            需要建立一个牌堆，并设置出卡的机制（random）
            第一回合双方各摸四张手牌，随后每回合各摸两张
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
        if card.description == "cause damage to a player": # 使用kill
            if self.kill_used_this_turn:
                if distance_condition: #TODO: 使用杀时，考虑双方之间距离（weapon距离大于horse距离）
                    if "defend" not in target.card: #受到伤害的玩家手牌中没有defend
                        target.health_change(-1)
                    else: #受到伤害的玩家手牌中有defend，则不扣除生命，移除一张defend
                        target.card.remove("defend")
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

    def drop_card(self, cards: list):
        """
        跟获取卡牌一样，用这个方法来弃牌。
        :param cards:
        :return:
        """
        if len(self.card) > self.health:
            cards_to_drop = len(self.card) - self.health #按照现有生命值确定弃牌数
        # TODO: 弃牌机制
        pass