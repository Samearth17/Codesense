import random

# A standard deck of cards with 52 cards
deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 
        'J', 'Q', 'K', 'A', 
        2, 3, 4, 5, 6, 7, 8, 9, 10, 
        'J', 'Q', 'K', 'A',
        2, 3, 4, 5, 6, 7, 8, 9, 10, 
        'J', 'Q', 'K', 'A',
        2, 3, 4, 5, 6, 7, 8, 9, 10, 
        'J', 'Q', 'K', 'A']

# Shuffle the deck
random.shuffle(deck)
print(deck)