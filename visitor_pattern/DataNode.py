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


class DesignPatternBook(DataNode):

    @staticmethod
    def get_name():
        return '《从生活的角度解读设计模式》'


class Engineer(Visitor):

    def visit(self, book:DesignPatternBook):
        print('技术人读%s 一书后的感受：能抓信模式的核心思想，深入浅出，很有见地！' % book.get_name())


class ProductManager(Visitor):

    def visit(self, book:DesignPatternBook):
        print('产品经理读%s 一书后的感受：配图非常有趣，文章很有层次感！' % book.get_name())


class OtherFriend(Visitor):

    def visit(self, book:DesignPatternBook):
        print('IT 圈外朋友读%s 一书后的感受：技术内容一脸蒙，但故事很精彩，像看小说或故事集！' % book.get_name())


def test_visit_book():

    book = DesignPatternBook()

    obj_mgr = ObjectStructure()
    obj_mgr.add(book)
    obj_mgr.action(Engineer())
    obj_mgr.action(ProductManager())
    obj_mgr.action(OtherFriend())


test_visit_book()

