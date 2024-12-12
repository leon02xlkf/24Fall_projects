# 2024 Fall Final Projects

# An original version of the card game "The War of the Three Kingdom (三国杀)"

## Author: Guanyi Wang(guanyiw2), Zhanchen Kang(zk11)

## Hope you enjoy the game.

### Introduction

This is an adapted version of the card game "The War of the Three Kingdom". The game is played by 2. 
Each player has HP with the amount of 3, has cards in hand to use or discard, and can have equipment to put on.

The type of cards are listed below:
1. Basic cards:
kill: damage the target player and cause 1 HP loss (can only be used once in a single round whatever the number of kill the player has)
defend: immediately prevent the 1 HP damage from card "kill"
heal: recover for 1 HP
2. Equipment cards: This type of cards can be equipped to a player, and each has special skills to use cards, cause damage, etc.
We created the new functions of the weapons below from the original version.
AK47: ignore the limitation of "kill" only used once in a round
fireSupport: when a player used a "defend" to avoid damage, you can use another "kill" at once
doubleAttack: if the target player has no cards, you can cause double damage when using "kill"
3. Skill cards: this type of cards has special skills. (These new types can be added based on our version later)

At the beginning of the game, both player draw 4 cards, then take turns to make actions.
Each player should go through 3 phases in order when it comes to his turn.
1. Card Drawing: the player draw 2 cards.
2. Card Using: the player can use card.
3. Card Discarding: the number remove card from hand until the number of cards hold is no more than the HP.
   (e.g. if a player has 4 cards, and he only gets 2 HP, then 2 cards should be thrown away.)

Both players keep exchanging turns until one player's HP comes to zero, then the other player wins!

### Structure & Complexity Analysis
Generally, the main performance constraints come from player interactions and AI logic.
The code’s memory consumption scales linearly with the number of players, cards, and equipment.
1. Card Management via card_dictionary
The card_dictionary centralizes card definitions, including types, effects, and attributes like damage or healing values. 
Each card's behavior (e.g., "kill," "heal") is encoded in a single dictionary for easy reference.
This design simplifies card management and makes it easy to add or modify cards without changing other parts of the program.
   (We intend to make some potential future improvements: extend this to include dynamic effects by associating cards with lambda functions)
2. Unified Card Usage Logic in use_card
The use_card method serves as a centralized handler for using cards. 
It determines the card type, applies its effects, and manages card-specific rules like distance checks, weapon effects, and player equipment.
This ensures consistent behavior across different parts of the game.
   (If we break down the logic into smaller functions, we and instead get better readability and maintainability)
3. Complexity of gameManager:
Managing turns involves iterating over players needs O(n), where n is the number of players.
O(n+c) space is needed where c is the total number of cards in hand.
   (The time complexity may increase to O(n^2) when we make improvements later, e.g. skill cards with multi-target effects, distance of causing damage)


Thanks to CodeWithMe module in PyCharm, we can simultaneously edit the code, which saved a lot of time and improved our working efficiency.
Thanks everyone who gave really helpful advice on this program and hope you will all enjoy it. 

Dec 2024
