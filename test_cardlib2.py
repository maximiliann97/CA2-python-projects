import pytest
from enum import Enum
from cardlib import *


# This test assumes you call your suit class "Suit" and the colours "Hearts and "Spades"
def test_cards():
    h5 = NumberedCard(4, Suit.Hearts)
    assert isinstance(h5.suit, Enum)

    sk = KingCard(Suit.Spades)
    assert sk.get_value() == 13

    assert h5 < sk
    assert h5 == h5

# Our own tests
    c7 = NumberedCard(7, Suit.Clubs)
    sa = AceCard(Suit.Spades)
    assert isinstance(sa.suit, Enum)
    assert sa > c7
    assert sa.get_value() == 14

    da = AceCard(Suit.Diamonds)
    assert sa == da


# This test assumes you call your shuffle method "shuffle" and the method to draw a card "draw"
def test_deck():
    d = StandardDeck()
    c1 = d.draw()
    c2 = d.draw()
    assert not c1 == c2

    d2 = StandardDeck()
    d2.shuffle()
    c3 = d2.draw()
    c4 = d2.draw()
    assert not ((c3, c4) == (c1, c2))

#Our own tests
    d3 = StandardDeck()
    d3.shuffle()
    c5 = d3.draw()

    assert len(d3.deck) == 51

    # Collect remaining 51 cards in a list
    # Check that the drawn card has been removed (pop)
    rest_of_deck = []
    for i in range(len(d3.deck)):
        rest_of_deck.append(d3.draw())

    assert len(rest_of_deck) == 51
    assert c5 not in d3.deck

    # Know that the first card is 2 of Clubs, check that pop takes the first card.
    d4 = StandardDeck()
    c8 = d4.draw()
    assert c8 == NumberedCard(2, Suit.Clubs)


# This test builds on the assumptions above and assumes you store the cards in the hand in the list "cards",
# and that your sorting method is called "sort" and sorts in increasing order
def test_hand():
    h = Hand()
    assert len(h.cards) == 0
    d = StandardDeck()
    d.shuffle()
    h.add_card(d.draw())
    h.add_card(d.draw())
    h.add_card(d.draw())
    h.add_card(d.draw())
    h.add_card(d.draw())
    assert len(h.cards) == 5

    h.sort()
    for i in range(3):
        assert h.cards[i] < h.cards[i+1] or h.cards[i] == h.cards[i+1]

    cards = h.cards.copy()
    h.drop_cards([3, 0, 1])
    assert len(h.cards) == 2
    assert h.cards[0] == cards[2]
    assert h.cards[1] == cards[4]

# Our own tests
    h2 = Hand()
    h2.add_card(NumberedCard(7, Suit.Clubs))
    h2.add_card(KingCard(Suit.Hearts))
    assert len(h2.cards) == 2
    h2.drop_cards([1])
    assert len(h2.cards) == 1
    assert h2.cards[0] == NumberedCard(7, Suit.Clubs)


def test_pokerhands():
    h1 = Hand()
    h1.add_card(QueenCard(Suit.Diamonds))
    h1.add_card(KingCard(Suit.Hearts))

    h2 = Hand()
    h2.add_card(QueenCard(Suit.Hearts))
    h2.add_card(AceCard(Suit.Hearts))

    cl = [NumberedCard(10, Suit.Diamonds), NumberedCard(9, Suit.Diamonds),
          NumberedCard(8, Suit.Clubs), NumberedCard(6, Suit.Spades)]

    ph1 = h1.best_poker_hand(cl)
    assert isinstance(ph1, PokerHand)
    ph2 = h2.best_poker_hand(cl)
    assert ph1 == PokerHand(HandType.high_card, 13, 12)
    assert ph2 == PokerHand(HandType.high_card, 14, 12)

    assert ph1 < ph2

    cl.pop(0)
    cl.append(QueenCard(Suit.Spades))
    ph3 = h1.best_poker_hand(cl)
    ph4 = h2.best_poker_hand(cl)
    assert ph3 < ph4
    assert ph1 < ph2

    assert ph3 == PokerHand(HandType.one_pair, 12, 13)
    assert ph4 == PokerHand(HandType.one_pair, 12, 14)

    cl = [QueenCard(Suit.Clubs), QueenCard(Suit.Spades), KingCard(Suit.Clubs), KingCard(Suit.Spades)]
    ph5 = h1.best_poker_hand(cl)
    assert ph5 == PokerHand(HandType.full_house, (13, 12), 13)


# Own tests
    hand1 = Hand()
    hand1.add_card(NumberedCard(2, Suit.Spades))
    hand1.add_card(KingCard(Suit.Spades))

    hand2 = Hand()
    hand2.add_card(NumberedCard(4, Suit.Spades))
    hand2.add_card(KingCard(Suit.Hearts))

    cardlist = [NumberedCard(2, Suit.Clubs), NumberedCard(2, Suit.Diamonds), NumberedCard(2, Suit.Hearts),
                KingCard(Suit.Diamonds), KingCard(Suit.Clubs)]


    poker_hand1 = hand1.best_poker_hand(cardlist)
    poker_hand2 = hand2.best_poker_hand(cardlist)

    assert poker_hand1 == PokerHand(HandType.four_of_a_kind, 2, 13)
    assert poker_hand2 == PokerHand(HandType.full_house, (13, 2), 13)

    assert poker_hand2 < poker_hand1

    cardlist.pop(2)
    poker_hand3 = hand1.best_poker_hand(cardlist)
    poker_hand4 = hand2.best_poker_hand(cardlist)

    assert poker_hand3 == PokerHand(HandType.full_house, (13, 2), 13)
    assert poker_hand4 == PokerHand(HandType.full_house, (13, 2), 13)

    assert poker_hand3 == poker_hand4

    hand3 = Hand()
    hand3.add_card(NumberedCard(7, Suit.Spades))
    hand3.add_card(KingCard(Suit.Hearts))

    cardlist.pop(0)         # pop first card from cardlist, cardlist is now [2, king, king]
    poker_hand5 = hand3.best_poker_hand(cardlist)
    poker_hand6 = hand2.best_poker_hand(cardlist)

    assert poker_hand5 == PokerHand(HandType.three_of_a_kind, 13, 7)
    assert poker_hand6 == PokerHand(HandType.three_of_a_kind, 13, 4)

    assert poker_hand6 < poker_hand5       # test for comparing two equal three_of_a_kind with different high card


