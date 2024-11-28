class basicCards():
    def __init__(self):
        self.description = None
        self.damage = 0
        self.effect = None
        self.dictionary = {
            "kill": ["cause damage to a player", 1, None],
            "heal": ["recover 1 health to a player", 0, None],
            "defend": ["reduce 1 damage to player self", 0, None]
        }

    def initialization(self, card_type):
        list = self.dictionary.get(card_type)
        self.description = list[0]
        self.damage = list[1]
        self.effect = list[2]