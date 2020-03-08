from abc import ABCMeta


class Water:

    def __init__(self, state):
        self.__temperature = 25
        self.__state = state

    def __set_state__(self, state):
        self.__state = state

    def change_state(self, state):
        if self.__state:
            print("由{}变为{}".format(self.__state.get_name(), state.get_name()))
        else:
            print("初始化为{}".format(state.get_name()))
        self.__state = state

    def get_temperature(self):
        return self.__temperature

    def set_temperature(self, temperature):
        self.__temperature = temperature

        if self.__temperature <= 0:
            self.change_state(SolidState("固态"))
        elif self.__temperature <= 100:
            self.change_state(LiquidState("液态"))
        else:
            self.change_state(GaseousState("气态"))

    def rise_temperature(self, step):
        self.set_temperature(self.__temperature + step)

    def reduce_temperature(self, step):
        self.set_temperature(self.__temperature - step)

    def behavior(self):
        self.__state.behavior(self)


class State(metaclass=ABCMeta):

    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def behavior(self,water):
        pass


class SolidState(State):

    def __init__(self, name):
        super().__init__(name)

    def behavior(self, water):
        print("我性格高冷，当前体温{} ˚C, 我坚如钢铁，仿如一冷血动物，请用我砸人，嘿嘿......".format(water.get_temperature()))


class LiquidState(State):

    def __init__(self, name):
        super().__init__(name)

    def behavior(self, water):
        print("我性格温和，当前体温{} ˚C, 我可滋润万物，饮用我可以让你活力倍增......".format(water.get_temperature()))


class GaseousState(State):

    def __init__(self, name):
        super().__init__(name)

    def behavior(self, water):
        print("我性格热烈，当前体温{} ˚C, 飞向天空是我毕生的梦想，在这你将看到我的存在，我将达到无我的境界......".format(water.get_temperature()))


def test_state():
    water = Water(LiquidState("液态"))
    water.behavior()
    water.set_temperature(-4)
    water.behavior()
    water.rise_temperature(18)
    water.behavior()
    water.rise_temperature(110)
    water.behavior()


if __name__ == '__main__':
    test_state()
