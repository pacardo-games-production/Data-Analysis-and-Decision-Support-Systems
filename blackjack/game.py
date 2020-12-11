from random import randint
from enum import Enum

class Player:
    sum = 0
    usable_ace = False

    def __init__(self):
        while self.sum < 12:
            self.hit()

    def hit(self):
        """Takes one card
        Returns:
            int -- sum after taking card
        """
        c = Card().value
        if c == 11 and self.sum >= 11:
            self.sum += 1
        else:
            if c == 11 and self.sum < 11:
                self.usable_ace = True
            self.sum += c
            if self.sum > 21 and self.usable_ace:
                self.usable_ace = False
                self.sum -= 10
        return self.sum

class Card:
    """Generate one card and store its number in value field
    """
    value = 0

    def __init__(self):
        number = randint(1, 13)
        if number == 1:
            self.value = 11
        elif number > 10:
            self.value = 10
        else:
            self.value = number


class Action(Enum):
    HIT = 0
    STAND = 1

    def __int__(self):
        return self.value

class Dealer:
    sum = 0
    usable_ace = False

    def __init__(self):
        self.take_card()

    def take_card(self):
        """Take one card
        Returns:
            int -- value of card taken
        """
        c = Card().value
        if c == 11:
            self.usable_ace = True
        self.sum += c
        return c

    def play_to_end(self):
        """Play while sum < 17
        Returns:
            int -- sum of cards after playing
        """
        while (self.sum < 17):
            self.take_card()
            if self.sum > 21 and self.usable_ace:
                self.usable_ace = False
                self.sum -= 10
        return self.sum