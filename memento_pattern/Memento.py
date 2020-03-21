import logging
from copy import deepcopy


class Memento:

    def set_attributes(self, dict):

        self.__dict__ = deepcopy(dict)

    def get_attributes(self):
        return self.__dict__


class Caretaker:

    def __init__(self):
        self._mementos = {}

    def add_memento(self, name, memento):
        self._mementos[name] = memento

    def get_memento(self, name):
        return self._mementos[name]


class Originator:

    def create_memento(self):
        memento = Memento()
        memento.set_attributes(self.__dict__)
        return memento

    def restore_from_memento(self, memento):
        self.__dict__.update(memento.get_attributes())


class TerminalCmd(Originator):

    def __init__(self, text):
        self.__cmd_name = ''
        self.__cmd_args = []
        self.parse_cmd(text)

    def parse_cmd(self, text):
        sub_strs = self.get_attributes_from_string(text, ' ')

        if len(sub_strs) > 0:
            self.__cmd_name = sub_strs[0]

        if len(sub_strs) > 1:
            self.__cmd_args = sub_strs[1:]

    def get_attributes_from_string(self, str, split_flag):

        if split_flag == "":
            logging.warning('split_flag 为空！')
            return ''

        data = str.split(split_flag)
        result = [item.strip() for item in data if item.strip() != ""]
        return result

    def show_cmd(self):
        print(self.__cmd_name, self.__cmd_args)


class TerminalCaretaker(Caretaker):

    def show_history_cmds(self):

        for key, obj in self._mementos.items():
            name = ''
            value = []
            if obj._TerminalCmd__cmd_name:
                name = obj._TerminalCmd__cmd_name
            if obj._TerminalCmd__cmd_args:
                value = obj._TerminalCmd__cmd_args
            print('第%s条命令：%s %s' % (key, name, value))


def test_terminal():
    cmd_idx = 0
    caretaker = TerminalCaretaker()
    # cur_cmd = TerminalCmd('')

    while True:
        str_cmd = input('请输入指令：')
        str_cmd = str_cmd.lower()
        if str_cmd.startswith('q'):
            exit(0)
        elif str_cmd.startswith('h'):
            caretaker.show_history_cmds()
        elif str_cmd.startswith('!'):
            idx = int(str_cmd[1:])
            cur_cmd.restore_from_memento(caretaker.get_memento(idx))
            cur_cmd.show_cmd()
        else:
            cur_cmd = TerminalCmd(str_cmd)
            cur_cmd.show_cmd()
            caretaker.add_memento(cmd_idx, cur_cmd.create_memento())
            cmd_idx += 1


test_terminal()

