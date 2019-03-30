"""
2. Создать пользовательский класс данных (или использовать) один из классов,
реализованных в курсе Python.Основы. Реализовать класс с применением слотов
и обычным способом. Для объекта обычного класса проверить отображение словаря
атрибутов. Сравнить, сколько выделяется памяти для хранения атрибутов обоих
классов.
"""
from sys import getsizeof


class NotSlotted:
    def __init__(self, name):
        self.name = name


class Slotted(object):
    __slots__ = 'name'

    def __init__(self, name):
        self.name = name


if getsizeof(NotSlotted('Mike')) > getsizeof(Slotted('Mike')):
    print('__slots__ saves memory!')
