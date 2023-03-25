from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


# 簡單工廠方法
class PizzaStore:
    def __init__(self, factory: PizzaFactory):
        self.factory = factory

    def orderPizza(self, type_: str):
        pizza = self.factory.createPizza(type_)
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        print()


class PizzaFactory(ABC):
    @abstractmethod
    def createPizza(self, type_: str):
        raise NotImplementedError


class NYPizzaFactory(PizzaFactory):
    def createPizza(self, type_: str) -> Pizza:
        if type_ == 'cheese':
            pizza = NYStyleCheesePizza()
        elif type_ == 'calm':
            pizza = NYStyleCalmPizza()

        return pizza


class Pizza(ABC):
    def __init__(self):
        self.name = None
        self.dough = None
        self.sauce = None
        self.toppings = []

    def prepare(self):
        print(f'Preparing {self.name}')
        print(f'Tossing {self.dough}...')
        print(f'Adding {self.sauce}...')
        print(f'Adding toppings:')
        for topping in self.toppings:
            print(topping)

    def bake(self):
        print('Bake for 25 minutes at 350')

    def cut(self):
        print('Cutting the pizza into diagonal slices')

    def box(self):
        print('Place pizza in official PizzaStore box')


class NYStyleCheesePizza(Pizza):
    def __init__(self):
        super().__init__()
        self.name = 'NY Style Sauce and Cheese Pizza'
        self.dough = 'Thin Crust dough'
        self.sauce = 'Marinara Sauce'
        self.toppings.append('Grated Reggiano Cheese')


class NYStyleCalmPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.name = 'NY Style Sauce and Calm Pizza'
        self.dough = 'Double Crust dough'
        self.sauce = 'Bazhe Sauce'
        self.toppings.append('Grated Reggiano Cheese')


nyFactory = NYPizzaFactory()
nyStore = PizzaStore(nyFactory)
nyStore.orderPizza('cheese')
nyStore.orderPizza('calm')
