import unittest

from conway import count_neighbors


class NeighborTests(unittest.TestCase):
    a = [
        [0, 1, 0],
        [1, 0, 1],
        [0, 1, 0]
    ]
    b = [
        [1, 0, 1],
        [0, 1, 0],
        [1, 0, 1]
    ]
    c = [
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 1, 0, 1, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0]
    ]

    def test_1(self):
        self.assertEqual(count_neighbors(NeighborTests.a, 1, 1), 4)

    def test_2(self):
        self.assertEqual(count_neighbors(NeighborTests.b, 0, 0), 4)

    def test_3(self):
        self.assertEqual(count_neighbors(NeighborTests.c, 2, 2), 8)


if __name__ == '__main__':
    unittest.main()
