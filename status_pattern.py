from __future__ import annotations
from abc import ABC, abstractmethod


class State(ABC):
    def __init__(self, gumballMachine: GumballMachine):
        self.gumballMachine = gumballMachine

    @abstractmethod
    def insertQuarter(self):
        pass

    @abstractmethod
    def ejectQuarter(self):
        pass

    @abstractmethod
    def turnCrank(self):
        pass

    @abstractmethod
    def dispense(self):
        pass


class SoldState(State):
    def insertQuarter(self):
        print('Please wait, we\'re already giving you a gumball')

    def ejectQuarter(self):
        print('Sorry, you already turned the crank')

    def turnCrank(self):
        print('Turning twice doesn\'t get you another gumball')

    def dispense(self):
        self.gumballMachine.releaseBall()
        if self.gumballMachine.count == 0:
            print('Oops, out of gumballs')
            self.gumballMachine.setState(self.gumballMachine.soldOutState)
        else:
            self.gumballMachine.setState(self.gumballMachine.noQuarterState)


class SoldOutState(State):
    def insertQuarter(self):
        print('You can\'t insert a quarter, the machine is sold out')

    def ejectQuarter(self):
        print('You can\'t eject, you haven\'t inserted a quarter yet')

    def turnCrank(self):
        print('You turned, but there are no gumballs')

    def dispense(self):
        print('No gumballl dispensed')


class NoQuarterState(State):
    def insertQuarter(self):
        print('You inserted a quarter')
        self.gumballMachine.setState(self.gumballMachine.hasQuarterState)

    def ejectQuarter(self):
        print('You haven\'t inserted a quarter')

    def turnCrank(self):
        print('You turned, but there\'s no quarters')

    def dispense(self):
        print('You need to pay first')


class HasQuarterState(State):
    def insertQuarter(self):
        print('You can\'t insert another quarter')

    def ejectQuarter(self):
        print('Quarter returned')
        self.gumballMachine.setState(self.gumballMachine.noQuarterState)

    def turnCrank(self):
        print('You turned...')
        self.gumballMachine.setState(self.gumballMachine.soldState)

    def dispense(self):
        print('No gumball dispensed')


class GumballMachine:

    def __init__(self, numberGumballs: int):
        self.soldState = SoldState(self)
        self.soldOutState = SoldOutState(self)
        self.noQuarterState = NoQuarterState(self)
        self.hasQuarterState = HasQuarterState(self)

        self.count = numberGumballs
        if numberGumballs > 0:
            self.__state = self.noQuarterState
        else:
            self.__state = self.soldOutState

    def insertQuarter(self):
        self.__state.insertQuarter()

    def ejectQuarter(self):
        self.__state.ejectQuarter()

    def turnCrank(self):
        self.__state.turnCrank()
        self.__state.dispense()

    def setState(self, state: State):
        self.__state = state

    def releaseBall(self):
        print('A gumball comes rolling out the slot...')

        if self.count != 0:
            self.count -= 1


if __name__ == '__main__':
    gumballMachine = GumballMachine(2)
    gumballMachine.insertQuarter()
    gumballMachine.turnCrank()
    gumballMachine.turnCrank()
