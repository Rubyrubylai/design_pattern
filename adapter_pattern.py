'''
改變介面符合客戶期望
'''
from abc import ABC, abstractmethod


class Duck(ABC):
    @abstractmethod
    def quack(self):
        pass

    @abstractmethod
    def fly(self):
        pass


class MallardDuck(Duck):
    def quack(self):
        print('Quack')

    def fly(self):
        print('I\'m flying')


class Turkey(ABC):
    @abstractmethod
    def gobble(self):
        pass

    @abstractmethod
    def fly(self):
        pass


class WildTurkey(Turkey):
    def gobble(self):
        print('Gobble gobble')

    def fly(self):
        print('I\'m flying in a short distance')


# 物件轉接器
class TurkeyAdapter:
    def __init__(self, turkey: Turkey):
        self.turkey = turkey

    def quack(self):
        self.turkey.gobble()

    def fly(self):
        for _ in range(5):
            self.turkey.fly()


# 類別轉接器: 利用多重繼承
class TurkeyClassAdapter(WildTurkey, MallardDuck):
    def quack(self):
        self.gobble()

    def fly(self):
        for _ in range(5):
            super().fly()


def test_duck(duck: Duck):
    duck.quack()
    duck.fly()


if __name__ == '__main__':
    mallardDuck = MallardDuck()
    wildTurkey = WildTurkey()
    turkeyAdapter = TurkeyAdapter(wildTurkey)

    print('The Duck says...')
    test_duck(mallardDuck)

    print('The TurkeyAdapter says...')
    test_duck(turkeyAdapter)

    turkeyClassAdapter = TurkeyClassAdapter()

    print('The TurkeyClassAdapter says...')
    test_duck(turkeyClassAdapter)
