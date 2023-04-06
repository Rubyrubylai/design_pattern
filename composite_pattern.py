from __future__ import annotations
from abc import ABC
from collections.abc import Iterator


class MenuComponenet(ABC):
    def add(self, menu_component: MenuComponenet):
        raise NotImplementedError

    def remove(self, menu_component: MenuComponenet):
        raise NotImplementedError

    def get_child(self, i: int) -> MenuComponenet:
        raise NotImplementedError

    def get_name(self) -> str:
        raise NotImplementedError

    def get_description(self) -> str:
        raise NotImplementedError

    def get_price(self) -> float:
        raise NotImplementedError

    def is_vegetarian(self) -> bool:
        raise NotImplementedError


class MenuItem(MenuComponenet):
    def __init__(self, name: str, description: str, vegetarian: bool, price: float):
        self._name = name
        self._description = description
        self._vegetarian = vegetarian
        self._price = price

    def get_name(self) -> str:
        return self._name

    def get_description(self) -> str:
        return self._description

    def get_price(self) -> float:
        return self._price

    def is_vegetarian(self) -> bool:
        return self._vegetarian

    def __str__(self) -> str:
        return f'''{self.get_name()}, {self.get_price()}
        --- {self.get_description()}
        '''

    def __iter__(self) -> Iterator:
        return NullIterator()


class Menu(MenuComponenet):
    def __init__(self, name: str, description: str):
        self.menu_components = []
        self._name = name
        self._description = description

    def add(self, menu_component: MenuComponenet):
        self.menu_components.append(menu_component)

    def remove(self, menu_component: MenuComponenet):
        self.menu_components.remove(menu_component)

    def get_child(self, i: int) -> MenuComponenet:
        return self.menu_components[i]

    def get_name(self) -> str:
        return self._name

    def get_description(self) -> str:
        return self._description

    def __str__(self) -> str:
        str_representation = f'''{self.get_name()}, {self.get_description()}
        ---------------------------------------
        '''

        for menu_component in iter(self.menu_components):
            str_representation += str(menu_component)

        return str_representation

    def __iter__(self) -> Iterator:
        return CompositeIterator(iter(self.menu_components))


# 建立一個沒有作用的反覆器，在 iterate 的時候，不用再去判斷此物件是否為 iterable
class NullIterator(Iterator):
    def __next__(self):
        raise StopIteration()


class CompositeIterator(Iterator):
    def __init__(self, iterator: Iterator):
        self.stack = [iterator]  # stack 存放 iterator (一父節點下的所有子節點為一個 iterator)

    def __next__(self):
        if len(self.stack) == 0:
            raise StopIteration()

        iterator = self.stack[-1]

        try:
            menu_component = next(iterator)
            self.stack.append(iter(menu_component))
        except StopIteration:
            self.stack.pop()
            return next(self)

        return menu_component


class Waitress:
    def __init__(self, all_menus: MenuComponenet):
        self.all_menus = all_menus

    def print_menu(self):
        print(self.all_menus)

    def print_vegetarian_menu(self):
        print('Vegeratiran Menu')
        for menu_component in self.all_menus:
            try:
                if menu_component.is_vegetarian():
                    print(menu_component)
            except NotImplementedError:
                pass


if __name__ == '__main__':
    breakfast_menu = Menu('Pancake House Menu', 'Breakfast')
    dinner_menu = Menu('Dinner Menu', 'Lunch')
    cafe_menu = Menu('Cafe Menu', 'Dinner')
    dessert_menu = Menu('Dessert Menu', 'Dessert Of course')

    all_menus = Menu('All Menus', 'All menus combined')

    all_menus.add(breakfast_menu)
    all_menus.add(dinner_menu)
    all_menus.add(cafe_menu)

    dinner_menu.add(
        MenuItem('BLT', 'Bacon with lettuce & tomato on whole wheat', True, 2.99))
    dinner_menu.add(dessert_menu)

    dessert_menu.add(MenuItem(
        'Apple Pie', 'Apple Pie with a flakey crust, topped with vanilla ice cream', True, 1.59))

    waitress = Waitress(all_menus)
    waitress.print_menu()
    waitress.print_vegetarian_menu()
