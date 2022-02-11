from enum import Enum
from abc import ABC, abstractmethod
from random import shuffle

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

    def __eq__(self, other):
        return self.get_value() == other.get_value()

    def __lt__(self, other):
        return self.get_value() < other.get_value()


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


c1 = JackCard(Suit.Spades)
c2 = NumberedCard(3, Suit.Spades)

print(c1 > c2)


class Hand:
    def __init__(self, cards=None):
        if cards is None:
            self.cards = []     # We almost always want to initialise variables.
        else:
            self.cards = cards

    def add_card(self, card):
        self.cards.append(card)

    def drop_card(self, cards, index):
        cards.index = index
        for index in cards:
            self.cards.pop(index)

    def sort(self, cards):
        self.cards.sort()

    def best_poker_hand(self, cards=[]):
        pass


class StandardDeck:
    def __init__(self, cards):
        self.cards = []

    def build_deck(self, cards):
        for suit in Suit:
            self.cards.append(AceCard(suit))
            self.cards.append(KingCard(suit))
            self.cards.append(QueenCard(suit))
            self.cards.append(JackCard(suit))
            for v in range(2, 11):
                self.cards.append(NumberedCard(v, suit))


    def shuffle(self, cards):
        shuffle(cards)

    def draw(self, cards):
        self.cards.pop(0)

d = StandardDeck.cards
for c in d:
    print(c)
print(d)