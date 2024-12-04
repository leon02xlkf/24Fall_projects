class skillCards():
    def __init__(self):
        self.description = None  # 这个就是描述
        self.damage = 0  # 这个就是伤害啦
        self.effect = None  # 用于表明卡牌有什么特殊效果，比如兵粮寸断，就要在玩家开局的时候进行一次判定， 这个里面请装进去判定条件
        self.dictionary = {  # 有多少个卡就写多少个，按 description，damage，effect来分配
            "kill": ["cause damage to a player", 1, None],
            "heal": ["recover 1 health to a player", 0, None],
            "defend": ["reduce 1 damage to player self", 0, None]
        }

        # TODO：找了原游戏中锦囊牌，可以看一下用哪几个。。。
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

    def initialization(self, card_type):
        """
        用这个来声明卡牌是啥，直接通过get dictionary里面的表述来声明卡牌
        :param card_type:
        :return:
        """
        list = self.dictionary.get(card_type)
        self.description = list[0]
        self.damage = list[1]
        self.effect = list[2]