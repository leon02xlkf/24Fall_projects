class equipmentCards():
    def __init__(self):
        self.description = None # 这个就是描述
        self.damage = 0 # 这个就是伤害啦 装备一般没伤害，就不管了
        self.effect = None # 用于表明卡牌有什么特殊效果，比如兵粮寸断，就要在玩家开局的时候进行一次判定， 这个里面请装进去判定条件
        self.dictionary = { # 有多少个卡就写做少个，按 description，damage， effect来分配
            "kill": ["cause damage to a player", 0, None],
            # TODO:武器功能补充
            # e.g. 无视距离/伤害加倍/...
            "Chitu": ["Horse: increase 1 distance between the equipped player and others", 0, None],
            "Dilu": ["Horse: reduce 1 distance between the equipped player and others", 0, None]
        }

    def initialization(self, card_type):
        """
        用这个来声明卡牌是啥，直接通过get dictionary里面的表述来神明卡牌
        :param card_type:
        :return:
        """
        list = self.dictionary.get(card_type)
        self.description = list[0]
        self.damage = list[1]
        self.effect = list[2]