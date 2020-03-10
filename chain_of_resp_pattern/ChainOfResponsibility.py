from abc import ABCMeta, abstractmethod


class Request:

    def __init__(self, name, dayoff, reason):
        self.__name = name
        self.__dayoff = dayoff
        self.__reason = reason
        self.__leader = None

    def get_name(self):
        return self.__name

    def get_day_off(self):
        return self.__dayoff

    def get_reason(self):
        return self.__reason


class Responsible(metaclass=ABCMeta):

    def __init__(self, name, title):
        self.__name = name
        self.__title = title
        self._nextHandler = None

    def get_name(self):
        return self.__name

    def get_title(self):
        return self.__title

    def set_next_handler(self, next_handler):
        self._nextHandler = next_handler

    def handle_request(self, request):
        self._handle_request_impl(request)

        if self._nextHandler is not None:
            self._nextHandler.handle_request(request)

    @abstractmethod
    def _handle_request_impl(self, request):
        pass


class Person:

    def __init__(self, name):
        self.__name = name
        self.__leader = None

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_leader(self, leader):
        self.__leader = leader

    def get_leader(self):
        return self.__leader

    def send_request(self, request):
        print('%s 申请请假 %d 天。 请假事由：%s' % (self.__name, request.get_day_off(), request.get_reason()))
        if self.__leader is not None:
            self.__leader.handle_request(request)


class Supervisor(Responsible):

    def __init__(self, name, title):
        super().__init__(name,title)

    def _handle_request_impl(self, request):
        if request.get_day_off() <= 2:
            print('同意 %s 请假，签字人：%s(%s)' % (request.get_name(), self.get_name(), self.get_title()))


class DepartmentManager(Responsible):

    def __init__(self, name, title):
        super().__init__(name, title)

    def _handle_request_impl(self, request):
        if 2 < request.get_day_off() <= 5:
            print('同意 %s 请假，签字人：%s(%s)' % (request.get_name(), self.get_name(), self.get_title()))


class CEO(Responsible):

    def __init__(self, name, title):
        super().__init__(name, title)

    def _handle_request_impl(self, request):
        if 5 < request.get_day_off() <= 22:
            print('同意 %s 请假，签字人：%s(%s)' % (request.get_name(), self.get_name(), self.get_title()))


class Administrator(Responsible):

    def __init__(self, name, title):
        super().__init__(name, title)

    def _handle_request_impl(self, request):
        if request.get_day_off() <= 2:
            print('%s 的请假申请已审核，情况属实！已备案处理。处理人：%s(%s)\n' % (request.get_name(), self.get_name(), self.get_title()))


def test_chain_of_responsibility():
    direct_leader = Supervisor('Eren', '客户端研发部经理')
    department_leader = DepartmentManager('Eric', '技术研发中心总监')
    ceo = CEO('Hello', '创意文化公司CEO')
    administrator = Administrator('Nina','行政中心总监')
    direct_leader.set_next_handler(department_leader)
    department_leader.set_next_handler(ceo)
    ceo.set_next_handler(administrator)

    sunny = Person('Sunny')
    sunny.set_leader(direct_leader)
    sunny.send_request(Request(sunny.get_name(),1,'参加MDCC大会。'))

    tony = Person('Tony')
    tony.set_leader(direct_leader)
    tony.send_request(Request(tony.get_name(),5,'家里有紧急事件！'))

    pony = Person('Pony')
    pony.set_leader(direct_leader)
    pony.send_request(Request(pony.get_name(),15,'出国深造。'))


if __name__ == '__main__':
    test_chain_of_responsibility()

