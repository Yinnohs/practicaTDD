import unittest
from counter import MyCounter
counter = MyCounter(2,2,12)

class TestCounter (unittest.TestCase):
    def test_default_startValue(self):
        self.assertEqual(counter.getCurrentNumber(),4)

