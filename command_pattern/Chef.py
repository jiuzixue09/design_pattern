
from abc import ABCMeta, abstractmethod


class Chef:

    def steam_food(self, original_material):
        print('%s 清蒸中...' % original_material)
        return '清蒸' + original_material

    def stir_fried_food(self, original_material):
        print('%s 爆炒中...' % original_material)
        return '爆炒' + original_material


class Order(metaclass=ABCMeta):

    def __init__(self, name, original_material):
        self._chef = Chef()
        self._name = name
        self._original_material = original_material

    def get_display_name(self):
        return self._name + self._original_material

    @abstractmethod
    def processing_order(self):
        pass


class SteamOrder(Order):

    def __init__(self,original_material):
        super().__init__('清蒸', original_material)

    def processing_order(self):
        if self._chef is not None:
            return self._chef.steam_food(self._original_material)
        return ''


class SpicyOrder(Order):

    def __init__(self, original_material):
        super().__init__('香辣炒', original_material)

    def processing_order(self):
        if self._chef is not None:
            return self._chef.stir_fried_food(self._original_material)
        return ''


class Waiter:

    def __init__(self, name):
        self.__name = name
        self.__order:Order = None

    def receive_order(self, order):
        self.__order = order
        print('服务员%s：您的 %s 订单已收到，请耐心等待' % (self.__name, order.get_display_name()))

    def place_order(self):
        food = self.__order.processing_order()
        print('服务员%s：您的餐 %s 已准备好，请您慢用！' % (self.__name, food))


def test_order():
    waiter = Waiter('Anna')
    steam_order = SteamOrder('大闸蟹')
    print('客户 David：我要一份 %s' % steam_order.get_display_name())
    waiter.receive_order(steam_order)
    waiter.place_order()
    print()

    spicy_order = SpicyOrder('大闸蟹')
    print('客户 Tony：我要一份 %s' % spicy_order.get_display_name())
    waiter.receive_order(spicy_order)
    waiter.place_order()
    print()


if __name__ == '__main__':
    test_order()


