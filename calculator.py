# ТЗ: Необходимо создать функцию calculator с использованием встроенного модуля re,
# которая будет принимать строку, содержащую простое алгеброическое выражение с двумя целыми числами, например a+b.
# Знак может быть + - / *. Числа будут только целые. Функция должна возвращать результат выражения.
# Если введена не строка, то возбуждается исключение TypeError 'Необходимо ввести строку'.
# Если введена некорректная строка, то возбуждается исключение ValueError с произвольным текстом.
# Если происходит деление на ноль, то должно возвращаться сообщение "На ноль нельзя делить"

from re import fullmatch

def calculator(string: str) -> int|float|str:
    '''Это тестовый калькулятор для демонстрации UnitTest и PyTest'''
    if not isinstance(string,str):
        raise TypeError ('Необходимо ввести строку')
    if fullmatch(r'[+-/*]*\d+[+-/*][+-/*]*\d+',string):
        try:
            return eval(string)
        except ZeroDivisionError:
            return 'На ноль нельзя делить'
    else:
        raise ValueError('Необходимо вводить целые числа в формате: a+b')