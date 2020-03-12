from abc import ABCMeta, abstractmethod


class Subject(metaclass=ABCMeta):

    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    @abstractmethod
    def request(self, content=''):
        pass


class TonyReception(Subject):

    def __init__(self, name, phone_num):
        super().__init__(name)
        self.__phone_num = phone_num

    def get_phone_num(self):
        return self.__phone_num

    def request(self, content=''):
        print('name:%s, phone num:%s' % (self.get_name(), self.get_phone_num()))
        print('receive a package, parcel content:%s' % content)


class ProxySubject(Subject):

    def __init__(self, name, subject):
        super().__init__(name)
        self._real_subject = subject

    def request(self, content=''):
        self.pre_request()
        if self._real_subject is not None:
            self._real_subject.request(content)
        self.after_request()

    def pre_request(self):
        print('pre_request')

    def after_request(self):
        print('after_request')


class WendyReception(ProxySubject):

    def __init__(self, name, receiver):
        super().__init__(name, receiver)

    def pre_request(self):
        print('我是%s 的朋友，我来帮他代收快递！' % (self._real_subject.get_name()))

    def after_rquest(self):
        print('代收人: %s' % self.get_name())


def test_receive_parcel():
    tony = TonyReception('Tony','1383838438')
    print('Tony 接收:')
    tony.request('雪地鞋')
    print()

    print('Wendy 代收：')
    wendy = WendyReception('Wendy', tony)
    wendy.request('雪地鞋')


if __name__ == '__main__':
    test_receive_parcel()

