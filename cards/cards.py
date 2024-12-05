class cards:
    card_dictionary = {
        "kill": ["basic", "cause damage to a player", 1, "damage"],
        "defend": ["basic", "defend 1 damage to a player", 1, "defend"],
        "heal": ["basic", "heal 1 hp to a player", 1, "heal"],

        "AK47": ["equipment", "no limitation on using kill card", 1, "AK47"],
        "APAmmunition": ["equipment", "cause the damage with ignoring the defend equipment", 2, "APAmmunition"],
        "alchemy": ["equipment", "using two cards as a kill", 3, "alchemy"],
        "extraAmmunition": ["equipment",
                           "when a player used a defend to avoid damage, you can drop 2 cards to make the damage cause", 3, "extraAmmunition"],
        "fireSupport": ["equipment", "when a player used a defend to avoid damage, you can use another kill", 3, "fireSupport"],
        "surgeryAttack": ["equipment",
                            "you cause damage to a player, you can destrey a horse for the player",
                            3, "surgeryAttack"],
        "doubleAttack": ["equipment",
                            "if a player has no cards, cause double damange on the player",
                            3, "doubleAttack"]
    }

    def use_card(self, target, card_type):
        number = self.card_dictionary.get(card_type)[2]
        function = self.card_dictionary.get(card_type)[3]

        method = getattr(self, function)
        method(target, number)

    def damage(self, target, number):
        pass

    def defend(self, target, number):
        pass

    def heal(self, target, number):
        pass

    def AK47(self, target, number):
        pass

    def APAmmunition(self, target, number):
        pass

    def alchemy(self, target, number):
        pass

    def extraAmmunition(self, target, number):
        pass

    def fireSupport(self, target, number):
        pass

    def surgeryAttack(self, target, number):
        pass

    def doubleAttack(self, target, number):
        pass


dic = {1:1, 2:2, 3:3}
print(list(dic.keys()))