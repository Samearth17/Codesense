from random import shuffle
from itertools import product

deck = list(product(['A','2','3','4','5','6','7','8','9','10','J','Q','K'],['C','D','H','S']))
shuffle(deck)

player1_score = 0
player2_score = 0

def deal_cards(player):
    card1 = deck.pop()
    card2 = deck.pop()
    player.append(card1)
    player.append(card2)
    return player

player1 = deal_cards([])
player2 = deal_cards([])

# Player 1 turn
player1_score = 0
for i in range(len(player1)):
    card_score = 0
    if (player1[i][0] == 'A'):
        card_score = 11
    elif (player1[i][0] == 'J' or player1[i][0] == 'Q' or player1[i][0] == 'K'):
        card_score = 10
    else:
        card_score = int(player1[i][0])
        
    player1_score += card_score

# Player 2 turn
player2_score = 0
for i in range(len(player2)):
    card_score = 0
    if (player2[i][0] == 'A'):
        card_score = 11
    elif (player2[i][0] == 'J' or player2[i][0] == 'Q' or player2[i][0] == 'K'):
        card_score = 10
    else:
        card_score = int(player2[i][0])
        
    player2_score += card_score

# Checking the winner
if (player1_score > player2_score):
    print("Player 1 wins!")
elif (player2_score > player1_score):
    print("Player 2 wins!")
else:
    print("It's a Tie!")