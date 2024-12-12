class AI_player():
    def __init__(self):
        self.maximum_health = 3
        self.health = 3
        self.cards = []
        self.equipment = {"weapon": None,
                          "defend": None,
                          "horse1": None,
                          "horse-1": None}

        self.kill_limitation = True
        self.kill = 0

        self.fireSupport = False
        self.doubleAttack = False

        # Assign weights to different cards so that AI will use/drop them according to these weight.
        # The 1st digit stands for the weight in using the card, whereas the 2nd digit represents the discarding phase
        self.weights = {
            "kill": [5,5],
            "defend": [2,1],
            "heal": [3,3],
            "AK47": [1,1],
            "fireSupport": [1,1],
            "doubleAttack": [1,1]
        }

        self.index = 0

    def use_card(self):
        """
        Use the card with index 0 in the sorted list of current cards.
        Jump to the discard phase if the card is heal or defend when HP is full.
        """
        self.cards = self.sort_use_card()
        if self.health == 3 and (self.cards[self.index] == 'heal' or self.cards[self.index] == 'defend'):
            return "q"
        use_card = self.cards[self.index]
        self.index = 0
        return use_card

    def sort_use_card(self):
        """
        Sort the list of current cards by their weights.
        """
        cards = sorted(self.cards, key=lambda card: self.weights[card][0], reverse=True)
        return cards

    def drop_card(self):
        drop_list = []
        self.cards = self.sort_drop_card()
        for i in range(0, len(self.cards)-self.health):
            drop_list.append(self.cards[i])
        return drop_list

    def sort_drop_card(self):
        cards = sorted(self.cards, key=lambda card: self.weights[card][1], reverse=True)
        return cards

    def update_weight(self, card, number, useOrDrop):
        self.weights[card][useOrDrop] = self.weights.get(card)[0] + number
        return None

    def analyze(self, is_last_move_valid, target_hp, stage_of_move):
        # print("AI gets", len(self.cards), "cards, which are:")
        # print(self.cards)
        # print("hp:", self.health)
        # print(self.equipment)
        if self.equipment.get("weapon") == None:
            self.weights["AK47"] = [100,1]
            self.weights["doubleAttack"] = [100,1]
            self.weights["fireSupport"] = [100,1]

        if self.equipment.get("weapon") != None:
            self.weights["AK47"] = [1,100]
            self.weights["doubleAttack"] = [1,100]
            self.weights["fireSupport"] = [1,100]

        if stage_of_move == 0:
            self.sort_use_card()
            return self.use_card()

        if self.index >= len(self.cards):
            return "q"

        if is_last_move_valid == False:
            self.index += 1
            return self.use_card()

        if self.health == 3:
            self.weights["heal"] = [3, 3]

        if self.health <2:
            self.update_weight("heal", 10, 0)

        if target_hp <2:
            self.update_weight("kill", 10, 0)

        if stage_of_move == 2:
            return self.drop_card()

        return self.use_card()