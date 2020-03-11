from abc import ABCMeta, abstractmethod


class ReceiveParcel(metaclass=ABCMeta):

    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    @abstractmethod
    def receive(self, parce_content):
        pass


class TonyReception(ReceiveParcel):

    def __init__(self, name, phone_num):
        super().__init__(name)
        self.__phone_num = phone_num

    def get_phone_num(self):
        return self.__phone_num

    def receive(self, parcel_content):
        print('name:%s, phone num:%s' % (self.get_name(), self.get_phone_num()))
        print('receive a package, parcel content:%s' % parcel_content)


class WendyReception(ReceiveParcel):

    def __init__(self, name, receiver):
        super().__init__(name)
        self.__receiver = receiver

    def receive(self, parcel_content):
        print('我是%s 的朋友，我来帮他代收快递！' % (self.__receiver.get_name()))
        if self.__receiver is not None:
            self.__receiver.receive(parcel_content)
        print('代收人: %s' % self.get_name())


def test_receive_parcel():
    tony = TonyReception('Tony','18512345678')
    print('Tony 接收:')
    tony.receive('雪地鞋')
    print()

    print('Wendy 代收：')
    wendy = WendyReception('Wendy', tony)
    wendy.receive('雪地鞋')


if __name__ == '__main__':
    test_receive_parcel()

