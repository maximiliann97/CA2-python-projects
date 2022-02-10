from enum import Enum
from abc import ABC, abstractmethod

class Suit(Enum):
    Hearts = 4
    Spades = 3
    Clubs = 2
    Diamonds = 1

    def __str__(self):
        return self.name[0]

s = Suit.Hearts
s.value
c1 = NumberedCard(3, Suit.Spades)
c2 = NumberedCard(3, Suit.Hearts)
#c1 == c2
#c1 > c2
#c1.get_value() > c2.get_value()


for suit in Suit:
    print(suit.name)


class PlayingCard(ABC):
    def __init__(self, suit: Suit):
        self.suit = suit

    @abstractmethod
    def get_value(self):
        pass

    def __repr__(self):
        return "PlayingCard('{}', '{}')".format(self.value, self.suit)



class NumberedCard(PlayingCard):
    def __init__(self, value, suit):
        self.value = value
        super().__init__(suit)

    def get_value(self):
        return self.value


class JackCard(PlayingCard):
    def __init__(self, suit):
        super().__init__(suit)
    def get_value(self):
        return 11

class QueenCard(PlayingCard):
    def __init__(self, suit):
        super().__init__(suit)
    def get_value(self):
        return 12

class KingCard(PlayingCard):
    def __init__(self, suit):
        super().__init__(suit)
    def get_value(self):
        return 13

class AceCard(PlayingCard):
    def __init__(self, suit):
        super().__init__(suit)
    def get_value(self):
        return 14


