import unittest

counter = MyCounter()

class TestCounter (unittest.TestCase):
    def test_default_startValue(self):
        self.assertEqual(counter.getCurrentNumber,0)

