from enum import Enum
from abc import ABC, abstractmethod

class Suit(Enum):
    Hearts = 3
    Spades = 2
    Clubs = 1
    Diamonds = 0

    def __str__(self):
        return self.name[0]


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

    def __eq__(self, other):
        return self.value == other.value, self.suit.value == other.suit.value

    def __lt__(self, other): # We only check the magnitude:
        return self.value < other.value, self.suit.value < other.suit.value


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


c1 = NumberedCard(3, Suit.Spades)
c2 = NumberedCard(3, Suit.Hearts)

