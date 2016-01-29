import random

class Card:
    RANKS = (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)
    SUITS = ('Spades', 'Hearts', 'Cloves', 'Diamonds')
    
def _init_ (self, rank, suit):
    self._rank = rank
    self._suit = suit
    
deg getRank (self):
    return self._rank