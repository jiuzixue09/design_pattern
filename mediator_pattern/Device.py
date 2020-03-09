from abc import ABCMeta, abstractmethod
from enum import Enum


class DeviceType(Enum):
    type_speaker = 1
    type_microphone = 2
    type_camera = 3


class DeviceItem:

    def __init__(self, id, name, type, is_default=False):
        self.__id = id
        self.__name = name
        self.__type = type
        self.__is_default = is_default

    def __str__(self) -> str:
        temp = vars(self)
        return str(temp)

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_type(self):
        return self.__type

    def is_default(self):
        return self.__is_default


class DeviceList:

    def __init__(self):
        self.__devices = []

    def add(self, device_item):
        self.__devices.append(device_item)

    def get_count(self):
        return len(self.__devices)

    def get_by_idx(self, idx)-> DeviceItem:
        return None if self.get_count() <= idx < 0 else self.__devices[idx]

    def get_by_id(self, id) -> DeviceItem:
        devices = list(filter(lambda d: d.get_id() == id, self.__devices))
        return devices[0] if len(devices) > 0 else None


class DeviceMgr(metaclass=ABCMeta):

    @abstractmethod
    def enumerate(self):
        pass

    @abstractmethod
    def active(self, device_id):
        pass

    @abstractmethod
    def get_cur_device_id(self):
        pass


class SpeakerMgr(DeviceMgr):

    def active(self, device_id):
        self.__cur_device_id = device_id

    def get_cur_device_id(self):
        return self.__cur_device_id

    def __init__(self):
        super().__init__()
        self.__cur_device_id = None

    def enumerate(self):
        devices = DeviceList()
        devices.add(DeviceItem("369dd760-893b-4fe0-89b1-671eca0f0224", "Definition Audio", DeviceType.type_speaker))
        devices.add(
            DeviceItem("369dd733-583b-4f40-5921-3788bad50231", "Definition Audio", DeviceType.type_speaker, True))

        return devices


class DeviceUtil:

    def __init__(self):
        self.__mgrs = {DeviceType.type_speaker: SpeakerMgr()}
        # the MicrophoneMgr and CameraMgr implement are ignored

    def __get_device_mgr(self, type):
        return self.__mgrs[type]

    def get_device_list(self,type):
        return self.__get_device_mgr(type).enumerate()

    def active(self, type, device_id):
        self.__get_device_mgr(type).active(device_id)

    def get_cur_device_id(self,type):
        return self.__get_device_mgr(type).get_cur_device_id()


def test_devices():
    device_util = DeviceUtil()
    device_list = device_util.get_device_list(DeviceType.type_speaker)

    print("microphone list")
    if device_list.get_count() > 0:
        device_util.active(DeviceType.type_speaker, device_list.get_by_idx(0).get_id())

    for idx in range(0, device_list.get_count()):
        device = device_list.get_by_idx(idx)
        print(device)
    print("current used device is: {}".format(device_list.get_by_id(device_util.get_cur_device_id(DeviceType.type_speaker)).get_name()))


if __name__ == '__main__':
    test_devices()
