
class HouseInfo:

    def __init__(self, area, price, has_window, has_bathroom, has_kitchen, address, owner):
        self.__area = area
        self.__price = price
        self.__has_window = has_window
        self.__has_bathroom = has_bathroom
        self.__has_kitchen = has_kitchen
        self.__address = address
        self.__owner = owner

    def get_address(self):
        return self.__address

    def get_owner_name(self):
        return self.__owner.get_name()

    def show_info(self, is_show_owner = True):
        print("""面积：{}平方米，
        价格：{}元，
        窗户：{},
        卫生间：{},
        厨房：{},
        地址：{},
        房东：{}""".format(self.__area,self.__price, "有" if self.__has_window else "没有",
                        self.__has_bathroom, "有" if self.__has_kitchen else "没有",
                        self.__address, self.get_owner_name() if is_show_owner else ""))


class HousingAgency:

    def __init__(self, name):
        self.__house_infos = []
        self.__name = name

    def get_name(self):
        return self.__name

    def add_house_info(self, house_info):
        self.__house_infos.append(house_info)
        if len(self.__house_infos) == 3:
            self.remove_house_info(house_info)

    def remove_house_info(self, house_info):
        self.__house_infos.remove(house_info)

    def get_search_condition(self, description):
        return description

    def get_match_infos(self, search_condition):
        print(self.get_name(), "为您找到以下最适合的房源：")
        [info.show_info(False) for info in self.__house_infos]
        return self.__house_infos

    def sign_contract(self, house_info:HouseInfo, period):
        print(self.get_name(),"与房东",house_info.get_owner_name(),"签订", house_info.get_address(),
              "的房子的租赁合同，租期",period,"年。合同期内",self.get_name(),"有权对其进行使用和转租！")

    def sign_contracts(self,period):
        [self.sign_contract(info, period) for info in self.__house_infos]


class HouseOwner:

    def __init__(self, name):
        self.__name = name
        self.__house_info = None

    def get_name(self):
        return self.__name

    def set_house_info(self, area, price, has_window, bathroom, kitchen, address):
        self.__house_info = HouseInfo(area,price,has_window,bathroom,kitchen,address,self)

    def publish_house_info(self, agency):
        agency.add_house_info(self.__house_info)
        print(self.get_name(),"在",agency.get_name(),"发布房源出租信息：")
        self.__house_info.show_info()


class Customer:

    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def find_house(self, description, agency:HousingAgency):
        print("我是{},人想找一个{}的房子\n".format(self.get_name(), description))
        return agency.get_match_infos(agency.get_search_condition(description))

    def see_house(self, house_infos):
        return house_infos[-1]

    def sign_contract(self, house_info, agency, period):
        print("{}与中介{}签订{}的房子的租赁合同，租期{}年。合同期内{}有权对其进行使用！".format(self.get_name(),
                                                                 agency.get_name(),house_info.get_address(),
                                                                 period,self.__name))


def test_renting():
    my_home = HousingAgency("我爱我家")
    zhangsan = HouseOwner("张三")
    zhangsan.set_house_info(20,2500,1,"独立卫生间",0,"上地西里")
    zhangsan.publish_house_info(my_home)

    lisi = HouseOwner("李四")
    lisi.set_house_info(16,1800,1,"公用卫生间",0,"当代城市家园")
    lisi.publish_house_info(my_home)

    wangwu = HouseOwner("王五")
    wangwu.set_house_info(18,2600,1,"独立卫生间",1,"金隅美和园")
    wangwu.publish_house_info(my_home)

    print()

    my_home.sign_contracts(3)
    print()

    tony = Customer("Tony")
    house_infos = tony.find_house("18 平方米左右， 要有独立卫生间，要有窗户，最好朝南，有厨房更好！价位在2000元左右", my_home)
    print()
    print("正在看房，寻找最合适的住巢......")
    print()
    appropriate_house = tony.see_house(house_infos)
    tony.sign_contract(appropriate_house, my_home, 1)


if __name__ == '__main__':
    test_renting()
