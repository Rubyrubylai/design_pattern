from __future__ import annotations
from abc import ABC, abstractmethod


class PizzaStore(ABC):
    def orderPizza(self, type_: str):
        pizza = self.createPizza(type_)
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        print()

    @abstractmethod
    def createPizza(self, type_: str):
        raise NotImplementedError


class NYPizzaStore(PizzaStore):
    def createPizza(self, type_: str):
        if type_ == 'cheese':
            pizza = NYStyleCheesePizza()
        elif type_ == 'calm':
            pizza = NYStyleCalmPizza()

        return pizza


class ChicagoPizzaStore(PizzaStore):
    def createPizza(self, type_: str):
        if type_ == 'cheese':
            pizza = ChicagoStyleCheesePizza()
        elif type_ == 'calm':
            pizza = ChicagoStyleCalmPizza()

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


class ChicagoStyleCheesePizza(Pizza):
    def __init__(self):
        super().__init__()
        self.name = 'Chicago Style Sauce and Cheese Pizza'
        self.dough = 'Extra Thich Crust dough'
        self.sauce = 'Marie Rose Sauce'
        self.toppings.append('Shredded Mozzarella Cheese')

    def cut(self):
        print('Cutting the pizza into square slices')


class ChicagoStyleCalmPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.name = 'Chicago Style Sauce and Calm Pizza'
        self.dough = 'Extra Thich Crust dough'
        self.sauce = 'Plum Tomato Sauce'
        self.toppings.append('Shredded Mozzarella Cheese')

    def cut(self):
        print('Cutting the pizza into square slices')


nyStore = NYPizzaStore()
nyStore.orderPizza('cheese')
nyStore.orderPizza('calm')
chicagoStore = ChicagoPizzaStore()
chicagoStore.orderPizza('cheese')
chicagoStore.orderPizza('calm')
