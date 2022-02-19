from enum import Enum
import pytest

from cardlib import *


def test_cards():
    h1 = NumberedCard(9, Suit.Hearts)
    h2 = JackCard(Suit.Clubs)
    h3 = QueenCard(Suit.Spades)
    h4 = KingCard(Suit.Diamonds)

