from abc import ABCMeta, abstractmethod


class IVehicle(metaclass=ABCMeta):

    @abstractmethod
    def running(self):
        pass


class SharedBycyle(IVehicle):

    def running(self):
        print('骑共享单车（轻快便捷）', end='')


class ExpressBus(IVehicle):

    def running(self):
        print('坐快速公交（经济绿色）', end='')


class Express(IVehicle):

    def running(self):
        print('打快车（快速方便）', end='')


class Subway(IVehicle):

    def running(self):
        print('坐地铁（高效安全）', end='')


class Classmate:

    def __init__(self, name, vehicle):
        self.__name = name
        self.__vehicle:IVehicle = vehicle

    def attend_the_dinner(self):
        print(self.__name + ' ', end='')
        self.__vehicle.running()
        print(' 来聚餐！')


def test_the_dinner():
    shared_bicycle = SharedBycyle()
    joe = Classmate('Joe', shared_bicycle)
    joe.attend_the_dinner()

    helen = Classmate('Helen', Subway())
    helen.attend_the_dinner()

    henry = Classmate('Henry', ExpressBus())
    henry.attend_the_dinner()

    ruby = Classmate('Ruby', Express())
    ruby.attend_the_dinner()


if __name__ == '__main__':
    test_the_dinner()
