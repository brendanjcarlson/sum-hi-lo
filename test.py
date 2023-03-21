import unittest
from whiteboard import solution

class TestWhiteboard(unittest.TestCase):
    def test_1(self):
        self.assertEqual(solution([1, 1, 11, 2, 3]), 6)

    def test_2(self):
        self.assertEqual(solution([6, 2, 1, 8, 10]), 16)

    def test_3(self):
        self.assertEqual(solution([1, 1, 1, 1, 1]), 3)

    def test_4(self):
        self.assertEqual(solution([-1, 100000000, 2]), 2)

    def test_5(self):
        self.assertEqual(solution([5]), 0)

    def test_6(self):
        self.assertEqual(solution([]), 0)

if __name__ == "__main__":
    unittest.main()