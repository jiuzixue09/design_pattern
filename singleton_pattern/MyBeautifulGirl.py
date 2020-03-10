
class MyBeautifulGirl(object):

    __instance = None
    __is_first_int = False

    def __new__(cls, name):
        if not cls.__instance:
            MyBeautifulGirl.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, name):
        if not self.__is_first_int:
            self.__name = name
            print('遇见%s, 我一见钟情！' % name)
            MyBeautifulGirl.__is_first_int = True
        else:
            print('遇见%s, 我置若罔闻' % name)

    def show_my_heart(self):
        print('%s就是我心中的唯一！' % self.__name)


def test_love():
    jenny = MyBeautifulGirl('Jenny')
    jenny.show_my_heart()
    kimi = MyBeautifulGirl('Kimi')
    kimi.show_my_heart()

    print('id(jenny):%s id(kimi):%s' % (id(jenny), id(kimi)))


if __name__ == '__main__':
    test_love()
