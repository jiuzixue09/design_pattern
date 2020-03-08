from abc import ABCMeta, abstractmethod


class Context(metaclass=ABCMeta):

    def __init__(self):
        self.__states = set()
        self.__cur_state = None
        self.__state_info = 0

    def add_state(self, state):
        self.__states.add(state)

    def change_state(self, state):
        if state is None:
            return False
        if self.__cur_state is None:
            print("初始化为{}".format(state.get_name()))
        else:
            print("由{}变为{}".format(self.__cur_state.get_name(), state.get_name()))

        self.__cur_state = state
        self.add_state(state)
        return True

    def get_state(self):
        return self.__cur_state

    def _set_state_info(self, state_info):
        self.__state_info = state_info
        [self.change_state(state) for state in self.__states if state.is_match(state_info)]

    def _get_state_info(self):
        return self.__state_info


class State:

    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def is_match(self, state_info):
        return False

    @abstractmethod
    def behavior(self, context):
        pass


class Water(Context):

    def __init__(self):
        super().__init__()
        self.add_state(SolidState('固态'))
        self.add_state(LiquidState('液态'))
        self.add_state(GaseousState('气态'))
        self.set_temperature(25)

    def get_temperature(self):
        return self._get_state_info()

    def set_temperature(self, temperature):
        self._set_state_info(temperature)

    def rise_temperature(self, step):
        self.set_temperature(self.get_temperature() + step)

    def reduce_temperature(self, step):
        self.set_temperature(self.get_temperature() - step)

    def behavior(self):
        state = self.get_state()
        if isinstance(state, State):
            state.behavior(self)


def singleton(cls, *args, **kwargs):

    instance = {}

    def __singleton(*args, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]

    return __singleton


@singleton
class SolidState(State):

    def __init__(self, name):
        super().__init__(name)

    def is_match(self, state_info):
        return state_info < 0

    def behavior(self, water):
        print("我性格高冷，当前体温{} ˚C, 我坚如钢铁，仿如一冷血动物，请用我砸人，嘿嘿......".format(water.get_temperature()))


@singleton
class LiquidState(State):

    def __init__(self, name):
        super().__init__(name)

    def is_match(self, state_info):
        return 0 <= state_info < 100

    def behavior(self, water):
        print("我性格温和，当前体温{} ˚C, 我可滋润万物，饮用我可以让你活力倍增......".format(water.get_temperature()))


@singleton
class GaseousState(State):

    def __init__(self, name):
        super().__init__(name)

    def is_match(self, state_info):
        return state_info >= 100

    def behavior(self, water):
        print("我性格热烈，当前体温{} ˚C, 飞向天空是我毕生的梦想，在这你将看到我的存在，我将达到无我的境界......".format(water.get_temperature()))


def test_state():
    water = Water()
    water.behavior()
    water.set_temperature(-4)
    water.behavior()
    water.rise_temperature(18)
    water.behavior()
    water.rise_temperature(110)
    water.behavior()


if __name__ == '__main__':
    test_state()
