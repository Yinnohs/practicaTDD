import unittest
from counter import MyCounter
counter = MyCounter(2,2,12)

class TestCounter (unittest.TestCase):
    def test_default_startValue(self):
        counter.reset()
        self.assertEqual(counter.getCurrentNumber(),counter.startValue_)
