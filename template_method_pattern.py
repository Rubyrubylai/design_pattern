'''
定義演算法的架構，讓次類別重新定義演算法的某些步驟
'''
from abc import ABC, abstractmethod


class CaffeineBeverage(ABC):
    def prepareRecipe(self):
        self.boilWater()
        self.brew()
        self.pourInCup()
        if self.customerWantsCondiments():
            self.addCondiments()

    @abstractmethod
    def brew(self):
        pass

    @abstractmethod
    def addCondiments(self):
        pass

    def boilWater(self):
        print('Boiling water')

    def pourInCup(self):
        print('Pouring into cup')

    # hook
    def customerWantsCondiments(self) -> bool:
        return True


class Tea(CaffeineBeverage):
    def brew(self):
        print('Steeping the tea')

    def addCondiments(self):
        print('Adding lemon')


class Coffee(CaffeineBeverage):
    def brew(self):
        print('Dripping Coffee through filter')

    def addCondiments(self):
        print('Adding sugar and milk')

    def customerWantsCondiments(self):
        userInput = input('Would you like milk and sugar with your coffee (y/n)?')

        if userInput == 'y':
            return True

        return False


if __name__ == '__main__':
    print('Making tea...')
    tea = Tea()
    tea.prepareRecipe()

    print('Making coffee...')
    coffee = Coffee()
    coffee.prepareRecipe()
