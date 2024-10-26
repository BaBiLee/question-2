import unittest
import q2

class TestSumTopTwo(unittest.TestCase):

    def test_1(self):
        self.assertEqual(q2.sum_top_two([1, 4, 2, 3, 5]), 9)

    def test_2(self):
        self.assertEqual(q2.sum_top_two([10, 20, 30, 40, 50]), 90)

    def test_3(self):
        self.assertEqual(q2.sum_top_two([-10, -20, -5, -1]), -6)

    def test_4(self):
        self.assertEqual(q2.sum_top_two([100, 200]), 300)

    def test_5(self):
        self.assertEqual(q2.sum_top_two([5, 4, 6, 7]), 13)

if __name__ == '__main__':
    unittest.main()