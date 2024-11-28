class skillCards():
    def __init__(self):
        self.description = None
        self.damage = 0
        self.effect = None
        self.dictionary = {

        }


    def initialization(self, card_type):
        list = self.dictionary.get(card_type)
        self.description = list[0]
        self.damage = list[1]
        self.effect = list[2]