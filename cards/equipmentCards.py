class equipmentCards():
    def __init__(self):
        self.description = None # 这个就是描述
        self.damage = 0 # 这个就是伤害啦 装备一般没伤害，就不管了
        self.effect = None # 用于表明卡牌有什么特殊效果，比如兵粮寸断，就要在玩家开局的时候进行一次判定， 这个里面请装进去判定条件
        self.dictionary = { # 有多少个卡就写做少个，按 description，damage， effect来分配
            "kill": ["cause damage to a player", 0, None],
            "Chitu": ["Horse: increase 1 distance between the equipped player and others", 0, None],
            "Dilu": ["Horse: reduce 1 distance between the equipped player and others", 0, None]
        }

    # TODO：找了原游戏中装备牌，可以看一下用哪几个
    # 诸葛连弩（1）：出牌阶段可以使用任意张杀
    # 青釭剑（2）：使用杀时无视对方防具
    # 丈八蛇矛（3）：需要打出杀时，可以使用两张手牌当做一张杀打出
    # 贯石斧（3）：目标角色使用闪抵消你使用杀的效果时，你可以弃两张牌，则杀依然造成伤害。
    # 青龙偃月刀（3）：当你使用的【杀】被抵消时，你可以立即对相同的目标再使用一张【杀】。
    # 麒麟弓（5）：你使用【杀】对目标角色造成伤害时，你可以将其装备区里的一匹马弃置。
    # 寒冰剑（2）：当你使用【杀】造成伤害时，你可以防止此伤害，改为弃置该目标角色的两张牌。
    # 古锭刀（2）：锁定技，当你使用的【杀】造成伤害时，若指定目标没有手牌，则该伤害+1。

    # 八卦阵：每当你需要打出一张【闪】时，你可以进行一次判定：若结果为红色，则视为你打出了一张【闪】；若为黑色，则你仍可从手牌里打出。
    # 仁王盾：锁定技，黑色的【杀】对你无效

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