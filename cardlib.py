from enum import IntEnum
from enum import Enum
from abc import ABC, abstractmethod
from random import shuffle
from collections import Counter


class Suit(IntEnum):
    Hearts = 3
    Spades = 2
    Clubs = 1
    Diamonds = 0

    def __str__(self):
        return self.name


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

    def __repr__(self):
        return f"{self.suit} of {self.get_value()}"


class NumberedCard(PlayingCard):
    def __init__(self, value, suit):
        self.value = value
        super().__init__(suit)

    def get_value(self):
        return self.value


class JackCard(PlayingCard):

    def get_value(self):
        return 11


class QueenCard(PlayingCard):

    def get_value(self):
        return 12


class KingCard(PlayingCard):

    def get_value(self):
        return 13


class AceCard(PlayingCard):

    def get_value(self):
        return 14


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


class Hand:
    def __init__(self, cards=None):
        if cards is None:
            self.cards = []  # We almost always want to initialise variables.
        else:
            self.cards = cards

    def add_card(self, card):
        self.cards.append(card)  # ska man inte ha en if sats, tänker man kan väl inte ha två av samma kort

    def drop_cards(self, indices):
        for index in sorted(indices, reverse=True):
            del self.cards[index]

    def sort(self):
        return self.cards.sort()

    def best_poker_hand(self, cards):
        return PokerHand(self.cards + cards)


class HandType(IntEnum):

    STRAIGHT_FLUSH = 9
    FOUR_OF_A_KIND = 8
    FULL_HOUSE = 7
    FLUSH = 6
    STRAIGHT = 5
    THREE_OF_A_KIND = 4
    TWO_PAIRS = 3
    PAIR = 2
    HIGH_CARD = 1


class PokerHand:
    def __init__(self, cards: list):
        self.cards = cards
        checkers = [self.check_straight_flush(cards), self.check_four_of_a_kind(cards), self.check_full_house(cards),
                    self.check_flush(cards), self.check_straight(cards), self.check_diff_pairs(cards)]

        for checker in checkers:
            v = checker
            if v is not None:
                self.type = v
                break

    def __lt__(self, other):
        return self.type < other.type

    @staticmethod
    def check_straight_flush(cards):
        vals = [(c.get_value(), c.suit) for c in cards] \
               + [(1, c.suit) for c in cards if c.get_value() == 14]  # Add the aces!
        for c in reversed(cards):  # Starting point (high card)
            # Check if we have the value - k in the set of cards:
            found_straight = True
            for k in range(1, 5):
                if (c.get_value() - k, c.suit) not in vals:
                    found_straight = False
                    break
            if found_straight:
                return HandType.STRAIGHT_FLUSH, c.get_value()

    @staticmethod
    def check_four_of_a_kind(cards):
        value_count = Counter()
        for c in cards:
            value_count[c.get_value()] += 1
        # Find the card ranks that have at least four of a kind
        fours = [v[0] for v in value_count.items() if v[1] >= 4]
        fours.sort()
        if fours:
            return HandType.FOUR_OF_A_KIND, max(fours)

    @staticmethod
    def check_full_house(cards):
        value_count = Counter()
        for c in cards:
            value_count[c.get_value()] += 1
        # Find the card ranks that have at least three of a kind
        threes = [v[0] for v in value_count.items() if v[1] >= 3]
        threes.sort()
        # Find the card ranks that have at least a pair
        twos = [v[0] for v in value_count.items() if v[1] >= 2]
        twos.sort()
        # Threes are dominant in full house, lets check that value first:
        for three in reversed(threes):
            for two in reversed(twos):
                if two != three:
                    return HandType.FULL_HOUSE, (three, two)

    @staticmethod
    def check_flush(cards):
        for c in reversed(cards):
            if c.suit != cards[0].suit:
                break
            else:
                return HandType.FLUSH, c.get_value()

    @staticmethod
    def check_straight(cards):
        vals = [c.get_value() for c in cards] \
               + [1 for c in cards if c.get_value() == 14]  # Add the aces!
        for c in reversed(cards):  # Starting point (high card)
            # Check if we have the value - k in the set of cards:
            found_straight = True
            for k in range(1, 5):
                if (c.get_value() - k, c.suit) not in vals:
                    found_straight = False
                    break
            if found_straight:
                return HandType.STRAIGHT, c.get_value()

    @staticmethod
    def check_diff_pairs(cards):
        value_count = Counter()
        for c in cards:
            value_count[c.get_value()] += 1
        # Find the card ranks that have at least three of a kind
        threes = [v[0] for v in value_count.items() if v[1] >= 3]
        threes.sort()
        # Find the card ranks that have at least a pair
        twos = [v[0] for v in value_count.items() if v[1] >= 2]
        twos.sort()

        if threes:
            return HandType.THREE_OF_A_KIND, max(threes)
        if twos:
            if len(twos) == 2:
                return HandType.TWO_PAIRS, max(twos)
            elif len(twos) == 1:
                return HandType.PAIR, max(twos)
        return HandType.HIGH_CARD, max(cards)

    def __repr__(self):
        return f'{self.type}'


l = NumberedCard(3, Suit.Hearts)
j = NumberedCard(4, Suit.Hearts)
q = NumberedCard(5, Suit.Hearts)
y = NumberedCard(5, Suit.Hearts)
r = NumberedCard(10, Suit.Hearts)

cards = [l, j, r, q, y]

n = PokerHand

h = Hand()
d = StandardDeck()
d.shuffle()
h.add_card(d.draw())
h.add_card(d.draw())
h.sort()

print(cards)
print(h.cards)
best_hand = h.best_poker_hand(cards)
print(best_hand)

#print(HandType.THREE_OF_A_KIND > HandType.PAIR)

a = HandType.PAIR, 12

print(a)

b = HandType.PAIR, 12

print(a > b)

h1 = Hand()
h1.add_card(QueenCard(Suit.Diamonds))
h1.add_card(KingCard(Suit.Hearts))

h2 = Hand()
h2.add_card(QueenCard(Suit.Hearts))
h2.add_card(KingCard(Suit.Hearts))

cl = [NumberedCard(10, Suit.Diamonds), NumberedCard(9, Suit.Diamonds),
      NumberedCard(8, Suit.Clubs), NumberedCard(6, Suit.Spades)]

ph1 = h1.best_poker_hand(cl)
print(ph1)
print(isinstance(ph1, PokerHand))
ph2 = h2.best_poker_hand(cl)
print(ph2)

print(ph1 < ph2)

cl.pop(0)
cl.append(QueenCard(Suit.Spades))
ph3 = h1.best_poker_hand(cl)
ph4 = h2.best_poker_hand(cl)
print(ph3)
print(ph4)

print(ph3 == ph4)
print(ph3 > ph4)
print(ph3 < ph4)

