import unittest
from is_three_is_five import is_three_is_five


class TestIsThreeIsFive(unittest.TestCase):
    def test_three(self):
        for num in (3, 6, 9):
            assert is_three_is_five(num) == "three"

    def test_five(self):
        for num in (5, 10, 20):
            assert is_three_is_five(num) == "five"

    def test_threefive(self):
        for num in (15, 30, 45):
            assert is_three_is_five(num) == "threefive"

    def test_number(self):
        for num in (1, 2, 4):
            assert is_three_is_five(num) == num
