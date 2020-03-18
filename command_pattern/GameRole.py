import time
from abc import ABCMeta, abstractmethod


class GameRole:
    STEP = 5

    def __init__(self, name):
        self.__name = name
        self.__x = 0
        self.__y = 0
        self.__z = 0

    def left_move(self):
        self.__x -= self.STEP

    def right_move(self):
        self.__x += self.STEP

    def up_move(self):
        self.__y += self.STEP

    def down_move(self):
        self.__y -= self.STEP

    def jump_move(self):
        self.__z += self.STEP

    def squat_move(self):
        self.__z -= self.STEP

    def attack(self):
        print('%s 发动攻击...' % self.__name)

    def show_position(self):
        print('%s 的位置：（x：%s，y：%s，z：%s）' % (self.__name,self.__x, self.__y, self.__z))


class GameCommand(metaclass=ABCMeta):

    def __init__(self, role:GameRole):
        self._role = role

    def set_role(self, role):
        self._role = role

    @abstractmethod
    def execute(self):
        pass


class Left(GameCommand):

    def execute(self):
        self._role.left_move()
        self._role.show_position()


class Right(GameCommand):

    def execute(self):
        self._role.right_move()
        self._role.show_position()


class Up(GameCommand):

    def execute(self):
        self._role.up_move()
        self._role.show_position()


class Down(GameCommand):

    def execute(self):
        self._role.down_move()
        self._role.show_position()


class Jump(GameCommand):

    def execute(self):
        self._role.jump_move()
        self._role.show_position()
        time.sleep(0.5)


class Squat(GameCommand):

    def execute(self):
        self._role.squat_move()
        self._role.show_position()
        time.sleep(0.5)


class Attack(GameCommand):

    def execute(self):
        self._role.attack()


class MacroCommand(GameCommand):

    def __init__(self, role = None):
        super().__init__(role)
        self.__commands = []

    def add_command(self, command):
        self.__commands.append(command)

    def remove_command(self, command):
        self.__commands.remove(command)

    def execute(self):
        [command.execute() for command in self.__commands]


class GameInvoker:

    def __init__(self):
        self.__command:GameCommand = None

    def set_command(self, command):
        self.__command = command
        return self

    def action(self):
        if self.__command is not None:
            self.__command.execute()


def test_game():

    role = GameRole('常山赵子龙')
    invoker = GameInvoker()

    while True:
        str_cmd = input('请输入命令：')
        str_cmd = str_cmd.upper()

        if str_cmd == 'L':
            invoker.set_command(Left(role)).action()
        elif str_cmd == 'R':
            invoker.set_command(Right(role)).action()
        elif str_cmd == 'U':
            invoker.set_command(Up(role)).action()
        elif str_cmd == 'D':
            invoker.set_command(Down(role)).action()
        elif str_cmd == 'A':
            invoker.set_command(Attack(role)).action()
        elif str_cmd == 'JP':
            cmd = MacroCommand()
            cmd.add_command(Jump(role))
            cmd.add_command(Squat(role))
            invoker.set_command(cmd).action()
        elif str_cmd == 'LU':
            cmd = MacroCommand()
            cmd.add_command(Left(role))
            cmd.add_command(Up(role))
            invoker.set_command(cmd).action()
        elif str_cmd == 'LD':
            cmd = MacroCommand()
            cmd.add_command(Left(role))
            cmd.add_command(Down(role))
            invoker.set_command(cmd).action()
        elif str_cmd == 'RU':
            cmd = MacroCommand()
            cmd.add_command(Right(role))
            cmd.add_command(Up(role))
            invoker.set_command(cmd).action()
        elif str_cmd == 'RD':
            cmd = MacroCommand()
            cmd.add_command(Right(role))
            cmd.add_command(Down(role))
            invoker.set_command(cmd).action()
        elif str_cmd == 'LA':
            cmd = MacroCommand()
            cmd.add_command(Left(role))
            cmd.add_command(Attack(role))
            invoker.set_command(cmd).action()
        elif str_cmd == 'RA':
            cmd = MacroCommand()
            cmd.add_command(Right(role))
            cmd.add_command(Attack(role))
            invoker.set_command(cmd).action()
        elif str_cmd == 'UA':
            cmd = MacroCommand()
            cmd.add_command(Up(role))
            cmd.add_command(Attack(role))
            invoker.set_command(cmd).action()
        elif str_cmd == 'DA':
            cmd = MacroCommand()
            cmd.add_command(Down(role))
            cmd.add_command(Attack(role))
            invoker.set_command(cmd).action()
        elif str_cmd == 'JA':
            cmd = MacroCommand()
            cmd.add_command(Jump(role))
            cmd.add_command(Attack(role))
            cmd.add_command(Squat(role))
            invoker.set_command(cmd).action()
        elif str_cmd == 'Q':
            exit()


test_game()