from enum import Enum


class Suit(Enum):
    HEARTS = 4
    SPADES = 3
    CLUBS = 2
    DIAMONDS = 1
#        self.suits = [HEARTS, SPADES, CLUBS, DIAMONDS]
#        self.suit = self.suits[suit]

for suit in Suit:
    print(suit)


class PlayingCard:
    def __init__(self, value: int, suit: Suit):
        pass


class NumberedCard(PlayingCard):
    def __init__(self, value, suit):
        self.values = range(2, 11)
        self.value = self.values[value]


class JackCard(PlayingCard):
    def __init__(self, suit):
        pass

    def get_value(self):
        return 11








#class PlayingCard:
 #   def __init__(self, value, suit):
  #      self.values = ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King"]
   #     self.value = self.values[value]
    #    self.suits = {"Hearts", "Spades", "Clubs", "Diamonds"}
     #   self.suit = self.suits[suit]
