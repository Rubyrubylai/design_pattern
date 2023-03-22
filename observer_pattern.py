from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Optional, List


# 主題介面
class Subject(ABC):
    @abstractmethod
    def registerObserver(self, observer: Observer):
        raise NotImplementedError

    @abstractmethod
    def removeObserver(self, observer: Observer):
        raise NotImplementedError

    @abstractmethod
    def notifyObservers(self):
        raise NotImplementedError


class WeatherData(Subject):
    __observers: List[Observer] = []
    __temperature: Optional[float] = None
    __humidity: Optional[float] = None
    __pressure: Optional[float] = None
    __weather: Optional[str] = None

    def registerObserver(self, observer: Observer):
        self.__observers.append(observer)

    def removeObserver(self, observer: Observer):
        self.__observers.remove(observer)

    def notifyObservers(self):
        for observer in self.__observers:
            observer.update(self)

    def measurementsChanged(self):
        self.notifyObservers()

    def setMeasurement(self, temperature: float, humidity: float, pressure: float, weather: str):
        self.__temperature = temperature
        self.__humidity = humidity
        self.__pressure = pressure
        self.__weather = weather
        self.measurementsChanged()

    def getTemperature(self) -> float:
        return self.__temperature

    def getHumidity(self) -> float:
        return self.__humidity

    def getPressure(self) -> float:
        return self.__pressure

    def getWeather(self) -> float:
        return self.__weather


# 觀察者介面
class Observer(ABC):
    @abstractmethod
    def update(self):
        raise NotImplementedError


class DisplayElement(ABC):
    @abstractmethod
    def display(self):
        raise NotImplementedError


class CurrentConditionDisplay(Observer, DisplayElement):
    __temperature: Optional[float] = None
    __humidity: Optional[float] = None
    __pressure: Optional[float] = None

    def __init__(self, subject: Subject):
        self.subject = subject
        subject.registerObserver(self)

    def update(self, subject: Subject):
        self.__temperature = subject.getTemperature()
        self.__humidity = subject.getHumidity()
        self.__pressure = subject.getPressure()
        self.display()

    def display(self):
        print(f'Current conditions: {self.__temperature} F degrees, {self.__humidity} % humidity, {self.__pressure} pressure')


class ForecastDisplay(Observer, DisplayElement):
    __weather: Optional[str] = None

    def __init__(self, subject: Subject):
        self.subject = subject
        subject.registerObserver(self)

    def update(self, subject: Subject):
        self.__weather = subject.getWeather()
        self.display()

    def display(self):
        print(f'Today\'s weather: {self.__weather}')


weatherData = WeatherData()
currentConditionDisplay = CurrentConditionDisplay(weatherData)
forecastDisplay = ForecastDisplay(weatherData)
weatherData.setMeasurement(20, 10, 30, 'sunny')
weatherData.removeObserver(forecastDisplay)
weatherData.setMeasurement(30, 10.2, 30, 'windy')
