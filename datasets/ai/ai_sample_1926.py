import random

class CardGame:

    deck = None
    scores = None

    def __init__(self):
        self.deck = self.generateDeck()
        self.scores = {'player1': 0, 'player2': 0}     

    def generateDeck(self):
        suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
        ranks = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
        deck = []
        for suit in suits:
            for rank in ranks:
                deck.append([suit, rank])
        random.shuffle(deck)
        return deck

    # Returns total points of a player's cards
    def getScore(self, player):
        score = 0
        for card in self.deck:
            if card[1] in ['J', 'Q', 'K']:
                score += 10
            elif card[1] == 'A':
                score += 11
            else:
                score += int(card[1])
        self.scores[player] = score
        return score

    # Check if a player won or there is a tie
    def isWinner(self, player1, player2):
        score1 = self.getScore(player1)
        score2 = self.getScore(player2)

        if score1 > score2:
            print(f'{player1} Wins')
        elif score2 > score1:
            print(f'{player2} Wins')
        else:
            print('It is a tie')