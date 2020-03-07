import time

class Observable:

    def __init__(self):
        self.__observers = []

    def add_observer(self, observer):
        self.__observers.append(observer)

    def remove_observer(self, observer):
        self.__observers.remove(observer)

    def notify_observers(self, object=0):
        for o in self.__observers:
            o.update(self, object)


class Account(Observable):
    
    def __init__(self):
        super().__init__()
        self.__latestIp = {}
        self.__latestRegion = {}
        
        
    def login(self, name, ip, time):
        region = self.__get_region(ip)

    def __get_region(self, ip):
        pass