class Register:

    def register(self, name):
        print('活动中心：%s 同学报到成功！' % name)


class Payment:

    def pay(self, name, money):
        print('缴费中心：收到%s同学%s元付款，缴费成功！' % (name, money))


class DormitoryManagementCenter:

    def provide_living_goods(self, name):
        print('生活中心：%s 同学的生活用品已发放。' % name)


class Dormitory:

    def meet_roommate(self, name):
        print('宿    舍： 大家好！这是刚来的%s 同学，是你们未来需要共度四年的室友！相互认识一下...' % name)


class Volunteer:

    def __init__(self, name):
        self.__name = name
        self.__register = Register()
        self.__payment = Payment()
        self.__life_center = DormitoryManagementCenter()
        self.__dormintory = Dormitory()

    def welcome_freshmen(self, name):
        print('你好，%s 同学！我是新生报到的志愿者%s，我将带你完成整个报到流程。' % (name, self.__name))
        self.__register.register(name)
        self.__payment.pay(name, 1000)
        self.__life_center.provide_living_goods(name)
        self.__dormintory.meet_roommate(name)


def test_register():
    volunteer = Volunteer('Frank')
    volunteer.welcome_freshmen('Tony')


if __name__ == '__main__':
    test_register()
