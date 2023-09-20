import unittest
from bowlingscore import score


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual([], score())

    def test_partial_frame(self):
        self.assertEqual(['open'], score(4))

    def test_complete_frame(self):
        self.assertEqual([9], score(4, 5))

    def test_two_complete_frames(self):
        self.assertEqual([9, 4], score(4, 5, 1, 3))

    def test_spare(self):
        self.assertEqual([15, 'open'], score(9,1,5))

    def test_strike(self):
        self.assertEqual([16, 6], score(10, 3, 3))

    def test_three_strikes(self):
        self.assertEqual([30, 20, 10, 0], score(10, 10, 10, 0, 0))

    def test_perfect_game(self):
        frames = 10 * [30]
        bowls = 12 * [10]
        self.assertEqual(frames, score(*bowls))

    def test_last_bowl_in_perfect(self):
        frames = 9 * [30] + ['open']
        bowls = 11 * [10]
        self.assertEqual(frames, score(*bowls))

    def test_all_spares_minus_one(self):
        frames = 9 * [19] + ['open']
        bowls = 10 * ([9, 1])
        self.assertEqual(frames, score(*bowls))


if __name__ == '__main__':
    unittest.main()
