from collections.abc import Iterable, Iterator
from typing import List


class MenuItem:
    def __init__(self, name: str, description: str, price: float):
        self.name = name
        self.description = description
        self.price = price


# 迭代器
class DinnerMenuIterator(Iterator):
    def __init__(self, items: List[MenuItem]):
        self.position = 0
        self.items = items

    def __next__(self) -> str:
        try:
            value = self.items[self.position]
            self.position += 1
        except IndexError:
            raise StopIteration()

        return value


# 可迭代的物件
class DinnerMenu(Iterable):
    def __init__(self):
        self.items = []

    def __iter__(self) -> DinnerMenuIterator:
        return DinnerMenuIterator(self.items)  # iter(self.itmes)

    def add_item(self, name: str, description: str, price: float):
        menu_item = MenuItem(name, description, price)
        self.items.append(menu_item)


class BreakfastMenuIterator(Iterator):
    def __init__(self, items: dict):
        self.position = 0
        self.values = list(items.values())

    def __next__(self) -> str:
        try:
            value = self.values[self.position]
            self.position += 1
        except IndexError:
            raise StopIteration()

        return value


class BreakfastMenu(Iterable):
    def __init__(self):
        self.items = {}
        self.position = 0

    def __iter__(self) -> BreakfastMenuIterator:
        return BreakfastMenuIterator(self.items)

    def add_item(self, name: str, description: str, price: float):
        menu_item = MenuItem(name, description, price)
        self.items[self.position] = menu_item
        self.position += 1


class Waitress:
    def __init__(self, menus: List[Iterable]):
        self.menus = menus

    def print_menu(self):
        for menu in self.menus:
            self._print_menu(menu)

    def _print_menu(self, iterator: Iterator):
        for i in iterator:
            print(i.name)
            print(i.description)
            print(i.price)


if __name__ == '__main__':
    breakfast_menu = BreakfastMenu()
    breakfast_menu.add_item('Pancake Breakfast', 'Pancakes with scrambled eggs, and toast', 2.99)
    breakfast_menu.add_item('Regular Breakfast', 'Pancakes with fried eggs', 2.99)
    breakfast_menu.add_item('Bluberry Breakfast', 'Pancakes made with fresh blueberries', 3.49)

    dinner_menu = DinnerMenu()
    dinner_menu.add_item('BLT', 'Bacon with lettuce & tomato on whole wheat', 2.99)
    dinner_menu.add_item('Soup of the day', 'Soup of the day, with a side of potato salad', 3.29)
    dinner_menu.add_item('Hotdog', 'A hot dog, with saurkraut, relish, onions', 3.05)

    waitress = Waitress([breakfast_menu, dinner_menu])
    waitress.print_menu()
