# 2024 Fall Final Projects

# An original version of the card game "The War of the Three Kingdom (三国杀)"

## author: Guanyi Wang(guanyiw2), Zhanchen Kang(zk11)

Several improvements have been made and the project is 95% completed. 

However, due to the limitation of our capacity, there are still some functions and designs not implemented. 
Maybe we will try to fix it a few days later.

Also, thanks to the CodeWithMe program, we saved a lot of time and git a lot less, which do improve the working efficiency.
Again, thanks to everyone who contributed in this program and hope you guys will enjoy it. 

## Hope you enjoy the game.

### The game introduction is listed below

This will be an original version of the card game "The War of the Three Kingdom". 
In this game, each player has 3 different stages that should be taken by order in each turn.

The stages are below:

1. a player will get 2 card when it is his turn.
2. The player will decide which card will he use. The card kill(do damage to other players) will only be allowed to used once a turn without some special equipment. There are no limitation for other cards.
3. If the number of the card for this player is greater than his health, then he must drop n cards(n = current containing card - health). 
For example, if a player has 4 cards and he only gets 2 health, then 2 cards should be dropped.

The type of cards are below:
1. basic cards:
kill, defend, heal
2. equipment cards: this type of cards can change the number of damage and health of the player
3. skill cards: this type of cards has special skills.

How does a game play?

1. At the very beginning, each player will get 4 cards.
2. Start with a player's stage, and repeat this step when each player get his own turn.
3. If one side of the players have won the game, the game ends.
