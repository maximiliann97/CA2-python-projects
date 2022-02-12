from enum import Enum
from abc import ABC, abstractmethod
from random import shuffle
from collections import Counter

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

    def __str__(self):
        return f" Card value: {self.get_value()}"


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


class StandardDeck:
    def __init__(self):
        self.cards = []

        for suit in Suit:
            self.cards.append(AceCard(suit))
            self.cards.append(KingCard(suit))
            self.cards.append(QueenCard(suit))
            self.cards.append(JackCard(suit))
            for value in range(2, 11):
                self.cards.append(NumberedCard(value, suit))

    def __iter__(self):
        return iter(self.cards)

    def shuffle(self):
        shuffle(self.cards)

    def draw(self):
        return self.cards.pop(0)


#d = StandardDeck()
#for c in d:
#    print(c)


class Hand:
    def __init__(self, cards=None):
        if cards is None:
            self.cards = []  # We almost always want to initialise variables.
        else:
            self.cards = cards
        #self.sort() fråga Michael!!!
        #self.drop_cards()

    def add_card(self, card):
        self.cards.append(card)

    def drop_cards(self, indices):
        for index in sorted(indices, reverse=True):
            del self.cards[index]

    def sort(self):
        return self.cards.sort()

    def best_poker_hand(self, cards=[]):
        value_counter = Counter(self.cards)


class StandardDeck:
    def __init__(self):
        self.cards = []
        self.build_deck()

    def build_deck(self):
        for suit in Suit:
            self.cards.append(AceCard(suit))
            self.cards.append(KingCard(suit))
            self.cards.append(QueenCard(suit))
            self.cards.append(JackCard(suit))
            for value in range(2, 11):
                self.cards.append(NumberedCard(value, suit))

    def shuffle(self):
        shuffle(self.cards)

    def draw(self):
        return self.cards.pop(0)

#d = StandardDeck()
#print(d)
#for c in d.cards:
#    print(c)

class PokerHand:
    def __init__(self, cards):
        self.cards = cards

    def __lt__(self, other):
        pass