from abc import ABCMeta, abstractmethod


# 监听模式
# 在对象间定义一种一对多的依赖关系，当这个对象状态发生改变时，所有依赖它的对象都会被通知并自动更新
class WaterHeater:

    def __init__(self):
        self.__observers = []
        self.__temperature = 25

    def get_temperature(self):
        return self.__temperature

    def set_temperature(self, temperature):
        self.__temperature = temperature
        print("current temperature is:" + str(self.__temperature) + "C")
        self.notifies()

    def add_observer(self, observer):
        self.__observers.append(observer)

    def notifies(self):
        for o in self.__observers:
            o.update(self)


class Observer(metaclass=ABCMeta):

    @abstractmethod
    def update(self, water_heater):
        pass


class WashingMode(Observer):

    def update(self, water_heater):
        if 50 <= water_heater.get_temperature() < 70:
            print("you can wash now.")


class DrinkingMode(Observer):

    def update(self, water_heater):
        if water_heater.get_temperature() >= 100:
            print("you can drink now.")


def test_water_heater():
    heater = WaterHeater()
    washing_obser = WashingMode()
    drinking_obser = DrinkingMode()
    heater.add_observer(washing_obser)
    heater.add_observer(drinking_obser)
    heater.set_temperature(40)
    heater.set_temperature(60)
    heater.set_temperature(100)


if __name__ == '__main__':
    test_water_heater()
