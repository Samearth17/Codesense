class Card():
    # suits is a set of all possible suits
    suits = {"spades", "hearts", "diamonds", "clubs"}

    # ranks is a set of all possible ranks
    ranks = {"Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King"}

    # Create a new card
    def __init__(self, suit, rank):
        # Check if the suit is valid
        if suit not in self.suits:
            raise ValueError(f"{suit} is not a valid suit")

        # Check if the rank is valid
        if rank not in self.ranks:
            raise ValueError(f"{rank} is not a valid rank")

        # Set the attributes of the card
        self.suit = suit
        self.rank = rank

    # Print the card as a string
    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck():
    # Create a deck of 52 cards
    def __init__(self):
        self.cards = []
        for suit in Card.suits:
            for rank in Card.ranks:
                self.cards.append(Card(suit, rank))

    # Generate a random card from the deck
    def get_random_card(self):
        return self.cards.pop()