from abc import ABCMeta, abstractmethod

import logging

import time

logging.basicConfig(level=logging.INFO)


class PooledObject:

    def __init__(self, obj):
        self.__obj = obj
        self.__busy = False

    def get_object(self):
        return self.__obj

    def set_object(self, obj):
        self.__obj = obj

    def is_busy(self):
        return self.__busy

    def set_busy(self, busy):
        self.__busy = busy


class ObjectPool(metaclass=ABCMeta):
    initial_num_of_objects = 10
    max_num_of_objects = 50

    def __init__(self):
        self.__pools = [self.create_pooled_object() for _ in range(0, ObjectPool.initial_num_of_objects)]

    @abstractmethod
    def create_pooled_object(self):
        pass

    def borrow_object(self):
        obj = self._find_free_object()
        if obj is not None:
            logging.info('%x 对象已被借用，time:%s', id(obj), time.strftime('%Y-%m-%d %H:%M:%S',
                                                                     time.localtime(time.time())))
            return obj

        if len(self.__pools) < ObjectPool.max_num_of_objects:
            pooled_obj = self.add_object()
            if pooled_obj is not None:
                pooled_obj.set_busy(True)
                logging.info('%x 对象已被借用，time:%s', id(obj), time.strftime('%Y-%m-%d %H:%M:%S',
                                                                         time.localtime(time.time())))
                return pooled_obj.get_object()

        return None

    def return_object(self, obj):

        for pooled_obj in self.__pools:
            if pooled_obj.get_object() == obj:
                pooled_obj.set_busy(False)
                logging.info('%x 对象已归还，time:%s', id(obj), time.strftime('%Y-%m-%d %H:%M:%S',
                                                                        time.localtime(time.time())))
                break

    def add_object(self):

        obj = None
        if len(self.__pools) < ObjectPool.max_num_of_objects:
            obj = self.create_pooled_object()
            self.__pools.append(obj)
            logging.info('添加新对象%x，time:%s', id(obj), time.strftime('%Y-%m-%d %H:%M:%S',
                                                                   time.localtime(time.time())))
        return obj

    def clear(self):
        self.__pools.clear()

    def _find_free_object(self):
        pooled_obj = next(p for p in self.__pools if not p.is_busy())
        pooled_obj.set_busy(True)
        return pooled_obj.get_object()


class PowerBank:

    def __init__(self, serial_num, electric_quantity):
        self.__serial_num = serial_num
        self.__electric_quantity = electric_quantity
        self.__user = ''

    def get_serial_num(self):
        return self.__serial_num

    def get_electric_quantity(self):
        return self.__electric_quantity

    def set_user(self, user):
        self.__user = user

    def get_user(self):
        return self.__user

    def show_info(self):
        print('序列号：%03d 电量：%d%% 使用者：%s' % (self.__serial_num, self.__electric_quantity, self.__user))


class PowerBankPool(ObjectPool):
    __serial_num = 0

    @classmethod
    def get_serial_num(cls):
        cls.__serial_num += 1
        return cls.__serial_num

    def create_pooled_object(self):
        power_bank = PowerBank(PowerBankPool.get_serial_num(), 100)
        return PooledObject(power_bank)


def test_object_pool():
    power_bank_pool = PowerBankPool()
    power_bank1 = power_bank_pool.borrow_object()
    if power_bank1 is not None:
        power_bank1.set_user('Tony')
        power_bank1.show_info()
    power_bank2 = power_bank_pool.borrow_object()
    if power_bank2 is not None:
        power_bank2.set_user('Sam')
        power_bank2.show_info()
    power_bank_pool.return_object(power_bank1)

    power_bank3 = power_bank_pool.borrow_object()
    if power_bank3 is not None:
        power_bank3.set_user('Aimee')
        power_bank3.show_info()

    power_bank_pool.return_object(power_bank2)
    power_bank_pool.return_object(power_bank3)
    power_bank_pool.clear()


test_object_pool()
