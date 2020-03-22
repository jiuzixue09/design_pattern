from abc import ABCMeta, abstractmethod


class Flyweight(metaclass=ABCMeta):

    @abstractmethod
    def operation(self,extrinsic_state):
        pass


class FlyweightImpl(Flyweight):

    def __init__(self, color):
        self.__color = color

    def operation(self,extrinsic_state):
        print('%s 取得 %s 色颜料' % (extrinsic_state, self.__color))


class FlyweightFactory:

    def __init__(self):
        self.__flyweights = {}

    def get_flyweight(self, key):
        pigment = self.__flyweights.setdefault(key,FlyweightImpl(key))
        return pigment


def test_flyweight():
    factory = FlyweightFactory()
    pigment_red = factory.get_flyweight('红')
    pigment_red.operation('梦之队')
    pigment_yellow = factory.get_flyweight('黄')
    pigment_yellow.operation('梦之队')
    pigment_blue1 = factory.get_flyweight('蓝')
    pigment_blue1.operation('梦之队')
    pigment_blue2 = factory.get_flyweight('蓝')
    pigment_blue2.operation('和平队')


test_flyweight()


