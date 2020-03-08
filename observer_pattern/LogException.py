import time
from abc import ABCMeta, abstractmethod


class Observer(metaclass=ABCMeta):

    @abstractmethod
    def update(self, observable, login_info):
        pass


class Observable:

    def __init__(self):
        self.__observers = []

    def add_observer(self, observer):
        self.__observers.append(observer)

    def remove_observer(self, observer):
        self.__observers.remove(observer)

    def notify_observers(self, login_info):
        for o in self.__observers:
            o.update(self, login_info)


class Account(Observable):

    def __init__(self):
        super().__init__()
        self.__latest_ip = {}
        self.__latest_region = {}

    def login(self, name, ip, time):
        region = self.__get_region(ip)
        if self.__is_long_distance(name, region):
            login_info = {"name": name, "ip": ip, "region": region, "time": time}
            self.notify_observers(login_info)
        self.__latest_region[name] = region
        self.__latest_ip[name] = ip

    def __get_region(self, ip):
        ip_regions = {"101.47.18.9": "浙江省杭州市", "67.218.147.69": "美国洛杉矶"}
        region = ip_regions.get(ip)
        return "" if region is None else region

    def __is_long_distance(self, name, region):
        latest_region = self.__latest_region.get(name)
        return latest_region is not None and latest_region != region


class SmsSender(Observer):

    def update(self, observable, login_info):
        print("""[短信发送] {}您好！检测到您的账户可能登录异常。最近一次登录信息：
登录地区：{} 登录 ip: {} 登录时间： {}"""
              .format(login_info["name"], login_info["region"],
                      login_info["ip"],
                      time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(login_info["time"]))))


class MailSender(Observer):

    def update(self, observable, login_info):
        print("""[邮件发送] {}您好！检测到您的账户可能登录异常。最近一次登录信息：
登录地区：{} 登录 ip: {} 登录时间： {}"""
              .format(login_info["name"], login_info["region"],
                      login_info["ip"],
                      time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(login_info["time"]))))


def test_login():
    account = Account()
    account.add_observer(SmsSender())
    account.add_observer(MailSender())
    account.login("Tony", "101.47.18.9", time.time())
    account.login("Tony", "67.218.147.69", time.time())


if __name__ == '__main__':
    test_login()
