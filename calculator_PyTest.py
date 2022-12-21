import pytest
from calculator import calculator


@pytest.mark.parametrize ('param, result',[('2+2', 4),
                                           ('5-7', -2),
                                           ('11*3', 33),
                                           ('36/3', 12),
                                           ('-10/5',-2),
                                           ('-5/10',-0.5),
                                           ('-5/-10',0.5),
                                           ('10/0','На ноль нельзя делить')])
def test_operation(param, result):
    assert calculator(param) == result


@pytest.mark.parametrize ('error, param',[(TypeError, []),
                                          (ValueError, '2.0+3.1')])
def test_raise_error(error,param):
    with pytest.raises(error):
        calculator(param)

def test_TypeError_message():
    with pytest.raises(TypeError) as er:
        calculator(1)
    assert er.value.args[0] == 'Необходимо ввести строку'

@pytest.mark.parametrize ('param',[('2.0+3.1'),('%_$@!_@')])
def test_ValueError_message(param):
    with pytest.raises(ValueError) as er:
        calculator(param)
    assert er.value.args[0] == 'Необходимо вводить целые числа в формате: a+b'