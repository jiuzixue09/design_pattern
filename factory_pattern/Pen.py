from abc import ABCMeta, abstractmethod
from enum import Enum


class PenType(Enum):
    pen_type_line = 1
    pen_type_rect = 2
    pen_type_ellipse = 3


class Pen(metaclass=ABCMeta):

    def __init__(self, name):
        self.__name = name

    @abstractmethod
    def get_type(self):
        pass

    def get_name(self):
        return self.__name


class LinePen(Pen):

    def __init__(self, name):
        super().__init__(name)

    def get_type(self):
        return PenType.pen_type_line


class RectanglePen(Pen):

    def __init__(self, name):
        super().__init__(name)

    def get_type(self):
        return PenType.pen_type_rect


class EllipsePen(Pen):

    def __init__(self, name):
        super().__init__(name)

    def get_type(self):
        return PenType.pen_type_ellipse


class PenFactory:

    def __init__(self):
        self.__pens = {}

    def get_single_obj(self, pen_type, name):
        pass

    def create_pen(self, pen_type) -> Pen:

        if self.__pens.get(pen_type) is None:
            if pen_type == PenType.pen_type_line:
                pen = LinePen('直线画笔')
            elif pen_type == PenType.pen_type_rect:
                pen = RectanglePen('矩形画笔')
            elif pen_type == PenType.pen_type_ellipse:
                pen = EllipsePen('椭圆画笔')
            else:
                pen = Pen('')
            self.__pens[pen_type] = pen

        return self.__pens[pen_type]


def test_pen_factory():
    factory = PenFactory()
    line_pen = factory.create_pen(PenType.pen_type_line)
    print('创建了 %s，对象id：%s，类型：%s' % (line_pen.get_name(), id(line_pen), line_pen.get_type()))
    rect_pen = factory.create_pen(PenType.pen_type_rect)
    print('创建了 %s，对象id：%s，类型：%s' % (rect_pen.get_name(), id(rect_pen), rect_pen.get_type()))
    rect_pen2 = factory.create_pen(PenType.pen_type_rect)
    print('创建了 %s，对象id：%s，类型：%s' % (rect_pen2.get_name(), id(rect_pen2), rect_pen2.get_type()))
    ellipse_pen = factory.create_pen(PenType.pen_type_ellipse)
    print('创建了 %s，对象id：%s，类型：%s' % (ellipse_pen.get_name(), id(ellipse_pen), ellipse_pen.get_type()))


if __name__ == '__main__':
    test_pen_factory()

