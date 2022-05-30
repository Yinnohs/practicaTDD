import unittest
from counter import MyCounter
counter = MyCounter()

class TestCounter (unittest.TestCase):
    def test_default_startValue(self):
        self.assertEqual(counter.incrementalValue_,1)

if __name__ == '__main__':
    unittest.main()

