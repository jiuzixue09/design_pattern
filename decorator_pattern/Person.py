from abc import ABCMeta, abstractmethod


class Person(metaclass=ABCMeta):

    def __init__(self, name):
        self._name = name

    @abstractmethod
    def wear(self):
        print('着装')


class Engineer(Person):

    def __init__(self, name, skill):
        super().__init__(name)
        self.__skill = skill

    def get_skill(self):
        return self.__skill

    def wear(self):
        print("我是 {}工程师 {}".format(self.get_skill(),self._name), end=', ')
        super().wear()


class Teacher(Person):

    def __init__(self, name, title):
        super().__init__(name)
        self.__title = title

    def get_title(self):
        return self.__title

    def wear(self):
        print("我是 {}{}".format(self._name, self.get_title()), end=', ')
        super().wear()


class ClothingDecorator(Person):

    def __init__(self, person):
        self._decorated = person

    def wear(self):
        self._decorated.wear()
        self.decorate()

    @abstractmethod
    def decorate(self):
        pass


class CasualPantDecorator(ClothingDecorator):

    def __init__(self, person):
        super().__init__(person)

    def decorate(self):
        print('一条卡期色休闲裤')


class BeltDecorator(ClothingDecorator):

    def __init__(self, person):
        super().__init__(person)

    def decorate(self):
        print('一条银色针头的黑色腰带')


class LeatherShoesDecorator(ClothingDecorator):

    def __init__(self, person):
        super().__init__(person)

    def decorate(self):
        print('一双深色休闲皮鞋')


class KnittedSweaterDecorator(ClothingDecorator):

    def __init__(self, person):
        super().__init__(person)

    def decorate(self):
        print('一件紫红色针织毛衣')


class WhiteShirtDecorator(ClothingDecorator):

    def __init__(self, person):
        super().__init__(person)

    def decorate(self):
        print('一件白色衬衫')


class GlassesDecorator(ClothingDecorator):

    def __init__(self, person):
        super().__init__(person)

    def decorate(self):
        print('一副方形黑框眼镜')


def test_decorator():
    tony = Engineer('Tony', '客户端')
    pant = CasualPantDecorator(tony)
    belt = BeltDecorator(pant)
    shoes = LeatherShoesDecorator(belt)
    shirt = WhiteShirtDecorator(shoes)
    sweater = KnittedSweaterDecorator(shirt)
    glasses = GlassesDecorator(sweater)
    glasses.wear()

    print()
    decorate_teacher = GlassesDecorator(WhiteShirtDecorator(LeatherShoesDecorator(Teacher('wells','教授'))))
    decorate_teacher.wear()


if __name__ == '__main__':
    test_decorator()
