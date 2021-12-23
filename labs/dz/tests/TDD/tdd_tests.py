import unittest

from app.handlers.rk import *
from app.handlers.exam import *


class Test(unittest.TestCase):
    def test_ticket(self):
        self.assertEqual(is_ticket('3'), True)
        self.assertEqual(is_ticket('Я билет, честно'), False)

    def test_subject(self):
        self.assertEqual(is_subject('Физика'), True)
        self.assertEqual(is_subject('Болтология'), False)

    def test_module(self):
        self.assertEqual(is_module('Максвелл и ЭМ волны'), True)
        self.assertEqual(is_module('Модуль four(четыре)'), False)

    def test_problem(self):
        self.assertEqual(is_problem('1'), True)
        self.assertEqual(is_problem('Задача номер забыл'), False)
