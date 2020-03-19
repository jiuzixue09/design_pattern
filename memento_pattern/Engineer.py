

class Engineer:

    def __init__(self, name):
        self.__name = name
        self.__work_items = []

    def add_work_item(self, item):
        self.__work_items.append(item)

    def forget(self):
        self.__work_items.clear()
        print('%s 工作太忙了，都忘记要做什么了！' % self.__name)

    def write_todo_list(self):
        todo_list = TodoList()
        for item in self.__work_items:
            todo_list.write_work_item(item)
        return todo_list

    def restrospect(self, todo_list):
        self.__work_items = todo_list.get_work_items()
        print('%s 想起要做什么了！' % self.__name)

    def show_work_item(self):
        if len(self.__work_items):
            print('%s 的工作项：' % self.__name)
            for idx, item in enumerate(self.__work_items):
                print('%d. %s;' % (idx + 1, item))
        else:
            print('%s 暂无工作项！' % self.__name)


class TodoList(object):

    def __init__(self):
        self.__work_items = []

    def write_work_item(self, item):
        self.__work_items.append(item)

    def get_work_items(self):
        return self.__work_items


class TodoListCaretaker:

    def __init__(self):
        self.__todo_list = None

    def set_todo_list(self, todo_list):
        self.__todo_list = todo_list

    def get_todo_list(self):
        return self.__todo_list


def test_engineer():
    tony = Engineer('Tony')
    tony.add_work_item('解决线上部分用户因昵称太长而无法显示全的问题')
    tony.add_work_item('完成PDF的解析')
    tony.add_work_item('在阅读器中显示PDF第一页的内容')
    tony.show_work_item()
    caretaker = TodoListCaretaker()
    caretaker.set_todo_list(tony.write_todo_list())

    print()
    tony.forget()
    tony.show_work_item()

    print()
    tony.restrospect(caretaker.get_todo_list())
    tony.show_work_item()


if __name__ == '__main__':
    test_engineer()

