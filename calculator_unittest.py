from unittest import TestCase, main
from calculator import calculator

class Calculator(TestCase):
    def test_plus(self):
        self.assertEqual(calculator('2+2'),4)

    def test_minus(self):
        self.assertEqual(calculator('5-7'),-2)

    def test_mult(self):
        self.assertEqual(calculator('11*3'),33)

    def test_division(self):
        self.assertEqual(calculator('36/3'),12)

    def test_division_by_zero(self):
        self.assertEqual(calculator('10/0'),'На ноль нельзя делить')

    def test_first_number_negative(self):
        self.assertEqual(calculator('-10/5'),-2)

    def test_second_number_negative(self):
        self.assertEqual(calculator('10/-5'),-2)

    def test_numbers_negative(self):
        self.assertEqual(calculator('-10/-5'), 2)

    def test_type_int(self):
        self.assertEqual(type(calculator('5*2')), int)

    def test_type_float(self):
        self.assertEqual(type(calculator('5/2')), float)

    def test_error_type(self):
        with self.assertRaises(TypeError) as er:
            calculator([123])
        self.assertEqual('Необходимо ввести строку',er.exception.args[0])

    def test_error_value(self):
         with self.assertRaises(ValueError) as er:
                calculator('2.0+3.1')
         self.assertEqual('Необходимо вводить целые числа в формате: a+b', er.exception.args[0])
