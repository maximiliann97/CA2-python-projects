from enum import Enum
import abc
import random
from collections import Counter


class PlayingCard(metaclass=abc.ABCMeta):
    """
    Abstract base class. Blueprint for creating cards with a value and a suit. Two abstract methods to ensure
    that the subclasses have these methods.
    """
    @abc.abstractmethod
    def __init__(self, value: int, suit):
        """
        Constructs card value and suit
        :param value:
        :param suit:
        """
        self.value = value
        self.suit = suit

    @abc.abstractmethod
    def get_value(self):
        """
        Method for accessing card values
        :return: value
        """
        return self.value

    def __eq__(self, other):
        """
        compares if the values are equal
        :param other:
        :return: True/False
        """
        return self.value == other.value

    def __lt__(self, other):
        """
        compares if self.values is less than other.values
        :param other:
        :return: True/False
        """
        return self.value < other.value


class Suit(Enum):
    """
    Class of Enum type, to be able to sort with __lt__ operator
    """
    Clubs = 0
    Diamonds = 1
    Hearts = 2
    Spades = 3


class NumberedCard(PlayingCard):
    """
    Subclass inheriting from PlayingCard.
    """
    def __init__(self, value: int, suit: Suit):
        """
        Inherit card parameter constructor from PlayingCard
        :param value:
        :param suit:
        """
        super().__init__(value, suit)

    def get_value(self):
        """
        Method for accessing card values
        :return: value
        """
        return self.value

    def __repr__(self):
        """
        overload __repr__ to print nicely
        :return:
        """
        return f"{str(self.value)} of {str(self.suit.name)}"


class JackCard(PlayingCard):
    """
    Subclass inheriting from PlayingCard. Value 11
    """
    def __init__(self, suit: Suit):
        """
        Inherit card parameter constructor from PlayingCard
        :param suit:
        """
        super().__init__(11, suit)

    def get_value(self):
        """
        Method for accessing card values
        :return: value
        """
        return self.value

    def __repr__(self):
        """
        overload __repr__ to print nicely
        :return:
        """
        return f"Jack of {str(self.suit.name)}"


class QueenCard(PlayingCard):
    """
    Subclass inheriting from PlayingCard. Value 12
    """
    def __init__(self, suit: Suit):
        super().__init__(12, suit)
        """
        Inherit card parameter constructor from PlayingCard 
        :param suit: 
        """

    def get_value(self):
        """
        Method for accessing card values
        :return: value
        """
        return self.value

    def __repr__(self):
        """
        overload __repr__ to print nicely
        :return:
        """
        return f"Queen of {str(self.suit.name)}"


class KingCard(PlayingCard):
    """
    Subclass inheriting from PlayingCard. Value 12
    """
    def __init__(self, suit: Suit):
        super().__init__(13, suit)
        """
        Inherit card parameter constructor from PlayingCard 
        :param suit: 
        """

    def get_value(self):
        """
        Method for accessing card values
        :return: value
        """
        return self.value

    def __repr__(self):
        """
        overload __repr__ to print nicely
        :return:
        """
        return f"King of {str(self.suit.name)}"


class AceCard(PlayingCard):
    """
    Subclass inheriting from PlayingCard. Ace ranked highest.
    """
    def __init__(self, suit: Suit):
        super().__init__(14, suit)
        """
        Inherit card parameter constructor from PlayingCard 
        :param suit: 
        """

    def get_value(self):
        """
        Method for accessing card values
        :return: value
        """
        return self.value

    def __repr__(self):
        """
        overload __repr__ to print nicely
        :return:
        """
        return f"Ace of {str(self.suit.name)}"


class HandType(Enum):
    """
    Class om type Enum, hand type ranking.
    """
    straight_flush = 9
    four_of_a_kind = 8
    full_house = 7
    flush = 6
    straight = 5
    three_of_a_kind = 4
    two_pair = 3
    one_pair = 2
    high_card = 1


class PokerHand:
    """
    Class receiving hand type and value for comparison between hands,
    """
    def __init__(self, handtype: HandType, handtypeval, highval):
        """
        Construct poker hand parameters
        :param handtype:
        :param val:
        """
        self.handtype = handtype
        self.handtypeval = handtypeval
        self.highval = highval

    def __eq__(self, other):
        """
        Returns equal if hand type, values of the hand type and highest cards is equal
        :param other:
        :return:
        """
        return (self.handtype.value, self.handtypeval, self.highval) ==\
               (other.handtype.value, other.handtypeval, other.highval)

    def __lt__(self, other):
        """
         First comparing hand types, if equal, the values of the hand types are compared, if equal,
         the highest values on the hand are compared
        :param other:
        :return:
        """
        return (self.handtype.value, self.handtypeval, self.highval) < \
               (other.handtype.value, other.handtypeval, other.highval)

    def __repr__(self):
        """
        Overloading __repr__ to print nicely
        :return:
        """
        return f"Hand type: {str(self.handtype.name)}, hand type value:" \
               f" {str(self.handtypeval)}, high card: {str(self.highval)}"


class Hand:
    """
    Class representing a players hand, includes methods for managing cards, static methods for checking all hand types and
    a best_poker_hand method for deciding the best available hand.
    """
    def __init__(self):
        """
        Construct a empty list representing the hand
        """
        self.cards = []

    def add_card(self, card):
        """
        Add specific card to the hand
        :param card:
        """
        self.cards.append(card)

    def drop_cards(self, index_list):
        """
        Drop cards from indexes
        :param index_list:
        """
        for index in sorted(index_list, reverse=True):      # Sort index list in reversed order to prevent
            del self.cards[index]                           # changes in indices when removing several cards.

    def sort(self):
        """
        Sort the cards in increasing orders by value
        :return:
        """
        return self.cards.sort()

    def __repr__(self):
        """
        Overloading __repr to print nicely
        :return:
        """
        return f"{str(self.cards)}"

    def best_poker_hand(self, common):
        """
        Adds the card from the input list with the cards on the hand and decides the best hand type, the value
        of the hand type and the highest card.
        :param common:
        :return: PokerHand object containing hand type and value of the hand type
        """

        cards = self.cards + common

        if self.check_for_straight_flush(cards):
            value = self.check_for_straight(cards)
            return PokerHand(HandType.straight_flush, value, value)     # Highest value is equal to highest value in the handtype

        elif self.check_for_four_of_a_kind(cards):
            value, high_card = self.check_for_four_of_a_kind(cards)
            return PokerHand(HandType.four_of_a_kind, value, high_card)

        elif self.check_for_full_house(cards):
            value = self.check_for_full_house(cards)
            return PokerHand(HandType.full_house, value, max(value))    # Highest value is equal to the highest value of
                                                                        # the full house
        elif self.check_for_flush(cards):
            value = self.check_for_flush(cards)
            return PokerHand(HandType.flush, value, value)      # Highest value is equal to highest value in the handtype

        elif self.check_for_straight(cards):
            value = self.check_for_straight(cards)
            return PokerHand(HandType.straight, value, value)       # Highest value is equal to highest value in the handtype

        elif self.check_for_three_of_a_kind(cards):
            value, high_card = self.check_for_three_of_a_kind(cards)
            return PokerHand(HandType.three_of_a_kind, value, high_card)

        elif self.check_for_two_pair(cards):
            value = self.check_for_two_pair(cards)
            return PokerHand(HandType.two_pair, value[0:2], value[2])

        elif self.check_for_one_pair(cards):
            value, high_card = self.check_for_one_pair(cards)
            return PokerHand(HandType.one_pair, value, high_card)

        elif self.check_for_high_card(cards):
            high_card, second_high = self.check_for_high_card(cards)
            return PokerHand(HandType.high_card, high_card, second_high)

    @staticmethod
    def check_for_straight_flush(cards):
        vals = [(c.get_value(), c.suit) for c in cards] +\
               [(1, c.suit) for c in cards if c.get_value() == 14]  #Add low aces
        for c in sorted(cards, reverse=True):  #Starting point (high card)
            # Check if we have the value - k in the set of cards:
            found_straight = True
            for k in range(1, 5):
                if (c.get_value() - k, c.suit) not in vals:
                    found_straight = False
                    break
            if found_straight:
                return c.get_value()        # return the highest value of the straight_flush

    @staticmethod
    def check_for_four_of_a_kind(cards):
        vals = [card.get_value() for card in cards]
        value_count = Counter()     # Keep track of how many times equivalent values appear
        for c in cards:
            value_count[c.get_value()] += 1     # Adds the cards value to the value_count
            # Find the card ranks that have four of a kind
            fours = [v[0] for v in value_count.items() if v[1] == 4]
            if fours:
                fours_value = c.get_value()
                rest_of_cards = [card for card in vals if card != fours_value]
                return c.get_value(), max(rest_of_cards)   # if four equal values are found, that value is returned
                                                        # the highest value outside the hand type is also returned
    @staticmethod
    def check_for_full_house(cards):
        value_count = Counter()
        for c in cards:
            value_count[c.get_value()] += 1
        # Find the card ranks that have at least three of a kind
        threes = [v[0] for v in value_count.items() if v[1] >= 3]
        threes.sort()       # Use the highest ranking tripple if 2 tripples are found
        # Find the card ranks that have at least a pair
        twos = [v[0] for v in value_count.items() if v[1] >= 2]
        twos.sort()
        # Threes are dominant in full house, lets check that value first:
        for three in reversed(threes):
            for two in reversed(twos):
                if two != three:
                    return three, two

    @staticmethod
    def check_for_flush(cards):
        suits = [c.suit for c in cards]
        vals = [(c.get_value(), c.suit) for c in cards]
        # Find suit if suit is found at least 5 times
        flush = ([item for item, count in Counter(suits).items() if count >= 5])

        if flush:
            flush_suit = flush[0]       # Fist value of flush is suit, second is count
            flush_cards = [i for i in vals if flush_suit == i[1]]   # list comprehension to find the values in the flush
            highest_card = max(flush_cards)[0]
            return highest_card

    @staticmethod
    def check_for_straight(cards):
        vals = [c.get_value() for c in cards] + \
               [(1, c.suit) for c in cards if c.get_value() == 14]      # Add low aces
        for c in sorted(cards, reverse=True):       # Starting point (high card)
            # Check if we have the value - k in the set of cards:
            straight = True
            for k in range(1, 5):
                if c.get_value() - k not in vals:
                    straight = False
                    break
            if straight:
                return c.get_value()    # Return the highest value of the straight


    @staticmethod
    def check_for_three_of_a_kind(cards):
        vals = [card.get_value() for card in cards]
        value_count = Counter()     # Keep track of how many times equivalent values appear
        for c in cards:
            value_count[c.get_value()] += 1     # Adds the cards value to the value_count
            # Find the card ranks that have three of a kind
            threes = [v[0] for v in value_count.items() if v[1] == 3]
            if threes:
                threes_value = c.get_value()
                rest_of_cards = [card for card in vals if card != threes_value]
                return c.get_value(), max(rest_of_cards)


    @staticmethod
    def check_for_two_pair(cards):
        vals = [card.get_value() for card in cards]
        value_count = Counter()
        for c in cards:
            value_count[c.get_value()] += 1
            # Find the card if there is 2 of the same and put in a list
            pairs = [v[0] for v in value_count.items() if v[1] == 2]
            if len(pairs) == 2:
                rest_of_cards = [card for card in vals if card not in pairs]
                return max(pairs), min(pairs), max(rest_of_cards)      # returns the best pair first, then the other pair
                                                                    # and the highest card outside the hand type

    @staticmethod
    def check_for_one_pair(cards):
        vals = [card.get_value() for card in cards]     # List with the values
        value_count = Counter()
        for c in cards:
            value_count[c.get_value()] += 1
            # Find the card if there is 2 of the same
            pair = [v[0] for v in value_count.items() if v[1] == 2]
            if pair:
                pair_value = c.get_value()
                rest_of_cards = [card for card in vals if card != pair_value]       # List with all the cards not in the pair
                return pair_value, max(rest_of_cards)      # Returns the value of the pair and the highest card outside the hand type

    @staticmethod
    def check_for_high_card(cards):
        vals = [c.get_value() for c in cards]
        high_card = sorted(vals, reverse=True)
        return high_card[0], high_card[1]


class StandardDeck:
    """
    Class creating the deck of 52 cards. Including methods for managing the deck: shuffle, draw the top card.
    """
    def __init__(self):
        """
        Constructs empty list representing the deck and fills it with card in the right order
        """
        self.deck = []
        for suit in Suit:
            for number in range(2, 11):
                self.deck.append(NumberedCard(number, suit))
            self.deck.append(JackCard(suit))
            self.deck.append(QueenCard(suit))
            self.deck.append(KingCard(suit))
            self.deck.append(AceCard(suit))

    def shuffle(self):
        """
        Shuffles the deck
        :return:
        """
        return random.shuffle(self.deck)

    def draw(self):
        """
        Draw the first card of the deck
        :return:
        """
        return self.deck.pop(0)

    def __repr__(self):
        """
        Overloading __repr__ to print nicely
        :return: 
        """
        return str(self.deck)






