class ClassDecorator:

    def __init__(self, func):
        self.__num_of_call = 0
        self.__func = func

    def __call__(self, *args, **kwargs):
        self.__num_of_call += 1
        obj = self.__func(*args, *kwargs)
        print('创建%s 的第%s 个实例：%s' % (self.__func.__name__, self.__num_of_call, id(obj)))
        return obj


@ClassDecorator
class MyClass:

    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name


tony = MyClass('Tony')
karry = MyClass('Karry')
print(id(tony))
print(id(karry))
