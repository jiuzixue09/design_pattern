from abc import ABCMeta, abstractmethod

class Person:

    def __init__(self, name, age, weight, height):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height

    def show_myself(self):
        print('%s 年龄：%d 岁，体重：%0.2fkg，身高：%0.2fm' % (self.name, self.age, self.weight, self.height))


class ICompare(metaclass=ABCMeta):

    @abstractmethod
    def comparable(self, person1, person2):
        pass


class CompareByAge(ICompare):

    def comparable(self, person1:Person, person2:Person):
        return person1.age - person2.age


class CompareByHeight(ICompare):

    def comparable(self, person1: Person, person2: Person):
        return person1.height - person2.height


class SortPerson:

    def __init__(self, compare:ICompare):
        self.__compare = compare

    def sort(self, person_list):
        n = len(person_list)

        for i in range(0, n-1):
            for j in range(0, n-i-1):
                if self.__compare.comparable(person_list[j],person_list[j + 1]) > 0:
                    person_list[j], person_list[j + 1] = person_list[j + 1], person_list[j]


def test_sort_person():
    person_list = [
        Person('Jack', 31, 74.5, 1.80),
        Person('Tony', 2, 54.5, 0.82),
        Person('Nick', 53, 44.5, 1.59),
        Person('Eric', 23, 62.0, 1.78),
        Person('Helen', 16, 45.7, 1.60)
    ]
    age_sorter = SortPerson(CompareByAge())
    age_sorter.sort(person_list)
    print('根据年龄进行排序后的结果：')
    for person in person_list:
        person.show_myself()

    print()

    height_sorter = SortPerson(CompareByHeight())
    height_sorter.sort(person_list)
    print('根据身高进行排序后的结果：')
    for person in person_list:
        person.show_myself()

    print()


if __name__ == '__main__':
    test_sort_person()

