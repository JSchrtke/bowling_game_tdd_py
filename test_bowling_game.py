import pytest
import bowling_game

# setup
@pytest.fixture
def game():
    return bowling_game.BowlingGame()


# utility functions
def roll_ntimes_mpins(game, rolls, pins):
    for i in range(rolls):
        game.roll(pins)


def roll_many(game, *pins):
    for pin in pins:
        game.roll(pin)


# tests
def test_gutter_game(game):
    roll_ntimes_mpins(game, 20, 0)
    assert game.score() == 0


def test_all_ones(game):
    roll_ntimes_mpins(game, 20, 1)
    assert game.score() == 20


def test_one_spare(game):
    roll_many(game, 3, 7, 4)
    roll_ntimes_mpins(game, 17, 0)
    assert game.score() == 18


def test_all_spares(game):
    roll_ntimes_mpins(game, 21, 5)
    assert game.score() == 150


def test_one_strike(game):
    roll_many(game, 10, 3, 3)
    roll_ntimes_mpins(game, 17, 0)
    assert game.score() == 22


def test_all_strikes(game):
    roll_ntimes_mpins(game, 12, 10)
    assert game.score() == 300
