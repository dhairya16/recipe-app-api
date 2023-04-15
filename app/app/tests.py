
from django.test import SimpleTestCase

from app import calc


class CalcTest(SimpleTestCase):
    """Test the calc module"""

    def test_add_number(self):
        res = calc.add_number(1, 2)
        self.assertEqual(3, res)
