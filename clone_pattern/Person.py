from copy import copy, deepcopy


class Clone:

    def clone(self):

        """浅拷贝的方式克隆对象"""
        return copy(self)

    def deep_clone(self):

        """深拷贝的方式克隆对象"""
        return deepcopy(self)


class Person(Clone):

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def show_my_self(self):
        print('我是%s, 年龄%d。' % (self.__name,self.__age))

    def coding(self):
        print('我是码农，我用程序改变世界，Coding......')

    def reading(self):
        print('阅读使我快乐！知识使我成长！如饥似渴地阅读是生活的一部分......')

    def fall_in_love(self):
        print('春风吹，月亮明，花前月下好相约......')


def test_clone():
    tony = Person('Tony', 27)
    tony.show_my_self()
    tony.coding()

    tony1 = tony.clone()
    tony1.show_my_self()
    tony1.reading()

    tony2 = tony.clone()
    tony2.show_my_self()
    tony2.fall_in_love()


if __name__ == '__main__':
    test_clone()


