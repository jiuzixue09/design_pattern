from abc import ABCMeta


class SocketEntity:

    def __init__(self, num_of_pin, type_of_pin):
        self.__num_of_pin = num_of_pin
        self.__type_of_pin = type_of_pin

    def get_num_of_pin(self):
        return self.__num_of_pin

    def set_num_of_pin(self, num_of_pin):
        self.__num_of_pin = num_of_pin

    def get_type_of_pin(self):
        return self.__type_of_pin

    def set_type_of_pin(self, type_of_pin):
        self.__type_of_pin = type_of_pin


class ISocket(metaclass=ABCMeta):

    def get_name(self):
        pass

    def get_socket(self):
        pass


class ChineseSocket(ISocket):

    def get_name(self):
        return '国际插座'

    def get_socket(self):
        return SocketEntity(3, '八字扁型')


class BritishSocket:

    def name(self):
        return '英标插座'

    def socket_interface(self):
        return SocketEntity(3,'T字方型')


class AdapterSocket(ISocket):

    def __init__(self, british_socket):
        self.__british_socket = british_socket

    def get_name(self):
        return self.__british_socket.name() + '转换器'

    def get_socket(self):
        socket = self.__british_socket.socket_interface()
        socket.set_type_of_pin('八字扁型')
        return socket


def can_charge_for_digtal_device(name, socket:SocketEntity):
    if socket.get_num_of_pin() == 3 and socket.get_type_of_pin() == '八字扁型':
        is_standard = '符合'
        can_charge = '可以'
    else:
        is_standard = '不符合'
        can_charge = '不能'

    print('[%s]：\n针脚数量：%d，针脚类型：%s; %s中国标准，%s给中国内地的电子设备充电！' %
          (name, socket.get_num_of_pin(), socket.get_type_of_pin(), is_standard, can_charge))


def test_socket():
    chinese_socket = ChineseSocket()
    can_charge_for_digtal_device(chinese_socket.get_name(), chinese_socket.get_socket())

    british_socket = BritishSocket()
    can_charge_for_digtal_device(british_socket.name(), british_socket.socket_interface())

    adapter_socket = AdapterSocket(british_socket)
    can_charge_for_digtal_device(adapter_socket.get_name(), adapter_socket.get_socket())


if __name__ == '__main__':
    test_socket()

