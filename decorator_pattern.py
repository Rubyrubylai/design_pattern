from abc import ABC, abstractmethod


# 裝飾者和被裝飾者有相同的超型態
class Beverage(ABC):
    description = 'Unknow Beverage'

    @abstractmethod
    def cost(self):
        raise NotImplementedError

    def getDescription(self):
        return self.description


class CondimentDecorator(Beverage):
    def __init__(self, beverage: Beverage):
        self.beverage = beverage

    @abstractmethod
    def getDescription(self):
        raise NotImplementedError


class Espresso(Beverage):
    description = 'Espresso'

    def cost(self) -> float:
        return 1.99


class HouseBlend(Beverage):
    description = 'HouseBlend'

    def cost(self) -> float:
        return 0.89


class Mocha(CondimentDecorator):

    def getDescription(self) -> str:
        return f'{self.beverage.getDescription()}, Mocha'

    def cost(self) -> float:
        return self.beverage.cost() + 0.2


class Soy(CondimentDecorator):

    def getDescription(self) -> str:
        return f'{self.beverage.getDescription()}, Soy'

    def cost(self) -> float:
        return self.beverage.cost() + 0.3


class Whip(CondimentDecorator):

    def getDescription(self) -> str:
        return f'{self.beverage.getDescription()}, Whip'

    def cost(self) -> float:
        return self.beverage.cost() + 0.5


beverage1 = Espresso()
print(f'{beverage1.getDescription()}: {beverage1.cost()}')
beverage2 = Mocha(beverage1)
print(f'{beverage2.getDescription()}: {beverage2.cost()}')
beverage3 = Whip(Soy(beverage2))
print(f'{beverage3.getDescription()}: {beverage3.cost()}')
