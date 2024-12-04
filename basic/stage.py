import cards.basicCards, cards.skillCards, cards.equipmentCards
import player

class game:
    def __init__(self):
        self.players = list()  # 用于存储有哪些玩家
        self.round = 1 # 用于存储已经进行的回合数
        self.live_player_indexes = list() # 用于存储存活玩家的编号，游戏开始时按照玩家数量生成，每有人死亡时从中删除对应数字，列表长度为1时返回元素（即为游戏胜者）

    def start(self, player_number):
        """
        开始游戏的方法，在开始游戏的时候需要生成player_number个玩家、该方法应该调用player类，并生成若干个player
        :param player_number:
        :return: index of the winner:
        """
        self.generate_player(player_number)
        self.live_player_indexes = [x+1 for x in range(player_number)]
        while True:
            if len(self.live_player_indexes) == 1: # 剩余一名玩家，游戏结束
                break
            else:
                for player in self.players: # 每名玩家轮流执行player_turn进行游戏
                    self.player_turn(player)
                self.round += 1
        return self.live_player_indexes[0]

    def generate_player(self, player_number):
        """
        在这里生成若干个玩家，直接一直生成player类就行
        :param player_number:
        :return:
        """
        for i in range(player_number):
            player_generated = player.player(name=f"player_{i}")
            self.players.append(player_generated)
        pass

    def player_turn(self, player):
        """
        在这里让player到他的回合
        回合需要干4件事
        1 如有锦囊牌，进行一次判定。
        2 抽卡
        3 用卡
        4 弃牌
        :param player:
        :return:
        """
        pass

    def judge(self, player, card):
        """
        在这里进行判定，负责指定玩加和卡牌，这个里面应该随机生成一个数字，并根据card类的dictionary里面获取的effect判断是否生效，然后把效果给player
        :param player:
        :param card:
        :return:
        """
        # TODO：判定时需要提供每一张卡牌的花色/数字，这个实现起来复杂吗？（会影响牌堆生成和存储）
        #  要不要直接用掷骰子判定（1-6中random，再判断奇偶等等。。。）
        pass

    def get_card(self, player):
        """
        在这里直接指定获取几个牌，然后发给玩家，调用player类的 get_card 方法
        :param player:
        :return:
        """
        if self.round == 1:
            cards_get_num = 4 # 第一回合，每名玩家抓四张牌
        else:
            cards_get_num = 2 # 其余回合，每名玩家抓两张牌
        # TODO: 调用player中的方法抓牌


    def drop_card(self, player):
        """
        指定玩家弃牌多少张，之后调用player类里面drop_card方法，让玩家弃牌
        :param player:
        :return:
        """
        if len(player.card) > player.health:
            cards_drop_num = len(player.card) - player.health # 按照现有生命值确定应保留的牌数
        # TODO: 调用player中的方法弃牌

    def use_card(self, player, card):
        """
        这个是直接指定玩家用什么牌的
        :param player:
        :param card:
        :return:
        """
        # TODO: 出牌机制