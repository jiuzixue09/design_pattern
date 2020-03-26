from abc import ABCMeta, abstractmethod


class DataNode(metaclass=ABCMeta):

    def accept(self, visitor):
        visitor.visit(self)


class Visitor(metaclass=ABCMeta):

    @abstractmethod
    def visit(self, data):
        pass


class ObjectStructure:

    def __init__(self):
        self.__datas = []

    def add(self, data_element):
        self.__datas.append(data_element)

    def action(self, visitor):
        [data.accept(visitor) for data in self.__datas]


class Animal(DataNode):

    def __init__(self, name, is_male, age, weight):
        self.__name = name
        self.__is_male = is_male
        self.__age = age
        self.__weight = weight


    def get_name(self):
        return self.__name

    def is_male(self):
        return self.__is_male

    def get_age(self):
        return self.__age

    def get_weight(self):
        return self.__weight


class Cat(Animal):

    def __init__(self, name, is_male, age, weight):
        super().__init__(name,is_male,age,weight)

    def speak(self):
        print('miao~')


class Dog(Animal):

    def __init__(self, name, is_male, age, weight):
        super().__init__(name, is_male, age, weight)

    def speak(self):
        print('wang~')


class GenderCounter(Visitor):

    def __init__(self):
        self.__male_cat = 0
        self.__female_cat = 0
        self.__male_dog = 0
        self.__female_dog = 0

    def visit(self, data):

        if isinstance(data, Cat):
            if data.is_male():
                self.__male_cat += 1
            else:
                self.__female_cat += 1
        elif isinstance(data, Dog):
            if data.is_male():
                self.__male_dog += 1
            else:
                self.__female_dog += 1
        else:
            print('Not support this type')

    def get_info(self):
        print('%d 只雄猫， %d 只雌猫， %d 只雄狗， %d 只雌狗' % (self.__male_cat, self.__female_cat,
                                                  self.__male_dog, self.__female_dog))


class WeightCounter(Visitor):

    def __init__(self):
        self.__cat_num = 0
        self.__cat_weight = 0
        self.__dog_num = 0
        self.__dog_weight = 0

    def visit(self, data):

        if isinstance(data, Cat):
            if data.is_male():
                self.__cat_num += 1
                self.__cat_weight += data.get_weight()
        elif isinstance(data, Dog):
            self.__dog_num += 1
            self.__dog_weight += data.get_weight()
        else:
            print('Not support this type')

    def get_info(self):
        print('猫的平均体重是：%0.2fkg，狗的平均体重是：%0.2fkg' % ((self.__cat_weight / self.__cat_num),
                                                   (self.__dog_weight / self.__dog_num)))


class AgeCounter(Visitor):

    def __init__(self):
        self.__cat_max_age = 0
        self.__dog_max_age = 0

    def visit(self, data):

        if isinstance(data, Cat):
            if data.is_male():
                if self.__cat_max_age < data.get_age():
                    self.__cat_max_age = data.get_age()
        elif isinstance(data, Dog):
            if self.__dog_max_age < data.get_age():
                self.__dog_max_age = data.get_age()
        else:
            print('Not support this type')

    def get_info(self):
        print('猫的最大年龄是：%s，狗的最大年龄是：%s' % (self.__cat_max_age, self.__dog_max_age))


def test_animal():
    animals = ObjectStructure()
    animals.add(Cat('Cat1', True, 1, 5))
    animals.add(Cat('Cat2', False, 0.5, 3))
    animals.add(Cat('Cat3', False, 1.2, 4.2))
    animals.add(Dog('Dog1', True, 0.5, 8))
    animals.add(Dog('Dog2', True, 3, 52))
    animals.add(Dog('Dog3', False, 1, 21))
    animals.add(Dog('Dog4', False, 2, 25))
    gender_counter = GenderCounter()
    animals.action(gender_counter)
    gender_counter.get_info()
    print()

    weight_counter = WeightCounter()
    animals.action(weight_counter)
    weight_counter.get_info()
    print()

    age_counter = AgeCounter()
    animals.action(age_counter)
    age_counter.get_info()


test_animal()


