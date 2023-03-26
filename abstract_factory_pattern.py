from __future__ import annotations
from abc import ABC, abstractmethod


class PizzaStore(ABC):
    def orderPizza(self, type_: str):
        pizza = self.createPizza(type_)
        print(f'Preparing {pizza.name}')
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        print()

    @abstractmethod
    def createPizza(self, type_: str) -> Pizza:
        pass


class NYPizzaStore(PizzaStore):
    def __init__(self):
        self.ingredientFactory = NYPizzaIngredientFactory()

    def createPizza(self, type_: str) -> Pizza:
        if type_ == 'cheese':
            pizza = NYStyleCheesePizza(self.ingredientFactory)
            pizza.setName('New York Style Cheese Pizza')
        elif type_ == 'clam':
            pizza = NYStyleCalmPizza(self.ingredientFactory)
            pizza.setName('New York Style Clam Pizza')

        return pizza


class Pizza(ABC):
    def __init__(self):
        self.name = None
        self.dough = None
        self.sauce = None
        self.cheese = None
        self.clam = None

    @abstractmethod
    def prepare(self):
        pass

    def bake(self):
        print('Bake for 25 minutes at 350')

    def cut(self):
        print('Cutting the pizza into diagonal slices')

    def box(self):
        print('Place pizza in official PizzaStore box')

    def setName(self, name):
        self.name = name

    def getName(self):
        print(self.name)


class NYStyleCheesePizza(Pizza):
    def __init__(self, ingredientFactory):
        super().__init__()
        self.ingredientFactory = ingredientFactory

    def prepare(self):
        self.dough = self.ingredientFactory.createDough()
        self.sauce = self.ingredientFactory.createSauce()
        self.cheese = self.ingredientFactory.createCheese()
        print(f'Tossing {self.dough.name}...')
        print(f'Adding {self.sauce.name}...')
        print(f'Adding {self.cheese.name}...')


class NYStyleCalmPizza(Pizza):
    def __init__(self, ingredientFactory):
        super().__init__()
        self.ingredientFactory = ingredientFactory

    def prepare(self):
        self.dough = self.ingredientFactory.createDough()
        self.sauce = self.ingredientFactory.createSauce()
        self.cheese = self.ingredientFactory.createCheese()
        self.clam = self.ingredientFactory.createClam()
        print(f'Tossing {self.dough.name}...')
        print(f'Adding {self.sauce.name}...')
        print(f'Adding {self.cheese.name}...')
        print(f'Adding {self.clam.name}...')


# 提供抽象介面，建立出一個產品家族
class PizzaIngredientFactory(ABC):
    # 工廠方法
    @abstractmethod
    def createDough(self) -> Dough:
        pass

    @abstractmethod
    def createSauce(self) -> Sauce:
        pass

    @abstractmethod
    def createCheese(self) -> Cheese:
        pass

    @abstractmethod
    def createClam(self) -> Clam:
        pass


class NYPizzaIngredientFactory(PizzaIngredientFactory):
    def createDough(self) -> Dough:
        return ThinCrustDough()

    def createSauce(self) -> Sauce:
        return MarinaraSauce()

    def createCheese(self) -> Cheese:
        return ReggianoCheese()

    def createClam(self) -> Clam:
        return FreshClam()


class Dough(ABC):
    pass


class ThinCrustDough(Dough):
    def __init__(self):
        self.name = 'thin crust dough'


class Sauce(ABC):
    pass


class MarinaraSauce(Sauce):
    def __init__(self):
        self.name = 'marinara sauce'


class Cheese(ABC):
    pass


class ReggianoCheese(Cheese):
    def __init__(self):
        self.name = 'reggiano cheese'


class Clam(ABC):
    pass


class FreshClam(Clam):
    def __init__(self):
        self.name = 'fresh clam'


nyStore = NYPizzaStore()
nyStore.orderPizza('cheese')
nyStore.orderPizza('clam')
