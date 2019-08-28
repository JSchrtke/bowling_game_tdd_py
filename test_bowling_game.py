import unittest
import bowling_game


class TestBowlingGame(unittest.TestCase):
    def setUp(self):
        self.g = bowling_game.BowlingGame()
        return super().setUp()

    def tearDown(self):
        return super().tearDown()

    def test_gutter_game(self):
        self.roll_ntimes_mpins(20, 0)
        self.assertEqual(self.g.score(), 0)

    def test_all_ones(self):
        self.roll_ntimes_mpins(20, 1)
        self.assertEqual(self.g.score(), 20)

    def test_one_spare(self):
        # Act
        self.g.roll(3)
        self.g.roll(7)
        self.g.roll(4)
        self.roll_ntimes_mpins(17, 0)
        # Assert
        self.assertEqual(self.g.score(), 18)

    def test_all_spares(self):
        # Act
        self.roll_ntimes_mpins(21, 5)
        # Assert
        self.assertEqual(self.g.score(), 150)

    def test_one_strike(self):
        # Act
        self.g.roll(10)
        self.g.roll(3)
        self.g.roll(3)
        self.roll_ntimes_mpins(17, 0)
        # Assert
        self.assertEqual(self.g.score(), 22)

    def test_all_strikes(self):
        # Act
        self.roll_ntimes_mpins(12, 10)
        # Assert
        self.assertEqual(self.g.score(), 300)

    def roll_ntimes_mpins(self, rolls, pins):
        for _ in range(rolls):
            self.g.roll(pins)
