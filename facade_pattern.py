'''
提供次系統一個簡化的介面
'''


class PopcornPopper:
    def on(self):
        print('Popcorn Popper on')

    def pop(self):
        print('Popcorn Popper popping popcorn!')


class TheaterLight:
    def dim(self, num: int):
        print(f'Therater Ceiling Lights dimming to {num}%')


class Screen:
    def down(self):
        print('Theater Screen going down')


class HomeTheaterFacade:
    def __init__(self, light: TheaterLight, screen: Screen, popper: PopcornPopper):
        self.light = light
        self.screen = screen
        self.popper = popper

    def watchMovie(self):
        self.popper.on()
        self.popper.pop()
        self.light.dim(10)
        self.screen.down()


if __name__ == '__main__':
    light = TheaterLight()
    screen = Screen()
    popper = PopcornPopper()
    homeTheater = HomeTheaterFacade(light, screen, popper)
    homeTheater.watchMovie()
