import unittest
from counter import MyCounter
counter = MyCounter(2,2,12)

class TestCounter (unittest.TestCase):
    def test_default_startValue(self):
        counter.count()
        self.assertEqual(counter.getCurrentNumber(),4)


if __name__ == '__main__':
    unittest.main()

