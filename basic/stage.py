import cards.basicCards, cards.skillCards, cards.equipmentCards

class game:
    def __init__(self):
        self.player = list()  # 用于存储有哪些玩家

    def start(self, player_number):
        """
        开始游戏的方法，在开始游戏的时候需要生成player_number个玩家、该方法应该调用player类，并生成若干个player
        :param player_number:
        :return:
        """
        while True:
            """
            在这里进行游戏
            """
            pass

    def generate_player(self, player_number):
        """
        在这里生成若干个晚间，直接一直生成player类就行
        :param player_number:
        :return:
        """
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
        pass

    def get_card(self, player, card_number):
        """
        在这里直接指定获取几个牌，然后发给玩家，调用player类的 get_card 方法
        :param player:
        :param card_number:
        :return:
        """
        pass

    def drop_card(self, player, card_number):
        """
        指定玩家弃牌多少张，之后调用player类里面drop_card方法，让玩家弃牌
        :param player:
        :param card_number:
        :return:
        """
        pass

    def use_card(self, player, card):
        """
        这个是直接指定玩家用什么牌的
        :param player:
        :param card:
        :return:
        """