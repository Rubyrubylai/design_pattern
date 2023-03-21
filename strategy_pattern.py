from abc import ABC, abstractmethod


class FlyBehavior(ABC):
    @classmethod
    @abstractmethod
    def fly(cls):
        raise NotImplementedError


class FlyWithWings(FlyBehavior):
    @classmethod
    def fly(cls):
        print('I can fly')


class FlyNoWay(FlyBehavior):
    @classmethod
    def fly(cls):
        print('I cannot fly')


class Duck:
    def __init__(self, fb=None):
        self.flyBehavior = fb

    def swim(self):
        print('All ducks float')

    def performFly(self):
        self.flyBehavior.fly()

    def setFlyBehavior(self, fb):
        self.flyBehavior = fb


class MallardDuck(Duck):
    def __init__(self):
        super().__init__(FlyWithWings)


class ToyDuck(Duck):
    def __init__(self):
        super().__init__()


mallardDuck = MallardDuck()
mallardDuck.performFly()
mallardDuck.swim()
mallardDuck.setFlyBehavior(FlyNoWay)
mallardDuck.performFly()
toyDuck = ToyDuck()
toyDuck.swim()
