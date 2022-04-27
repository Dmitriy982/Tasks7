from abc import ABC, abstractmethod


class Clothes(ABC):
    res = 0

    def __init__(self, p):
        self.p = p

    @property
    @abstractmethod
    def method(self):
        pass

    def __add__(self, other):
        return  self.method + other.method

    def __str__(self):
        return self.method


class Suit(Clothes):
    @property
    def method(self):
        return self.p * 2 + 0.3


class Coat(Clothes):
    @property
    def method(self):
        return self.p / 6.5 + 0.5


suit = Suit(30)
coat = Coat(60)
print(round(coat + suit, 3))
