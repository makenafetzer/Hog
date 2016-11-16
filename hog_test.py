"""CS 61A Presents The Game of Hog."""

from dice import four_sided, six_sided, make_test_dice
from ucb import main, trace, log_current_line, interact

GOAL_SCORE = 100  # The goal of Hog is to score 100 points.


######################
# Phase 1: Simulator #
######################

def roll_dice(num_rolls, dice=six_sided):
    """Simulate rolling the DICE exactly NUM_ROLLS>0 times. Return the sum of
    the outcomes unless any of the outcomes is 1. In that case, return the
    number of 1's rolled.
    """
    # These assert statements ensure that num_rolls is a positive integer.
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls > 0, 'Must roll at least once.'
    # BEGIN PROBLEM 1
    points = 0
    ones_counter = 0
    for i in range(num_rolls):
        roll = dice()
        if roll == 1:
            ones_counter += 1
        points += roll
    if ones_counter:
        return ones_counter
    return points
    # END PROBLEM 1

def free_bacon(opponent_score):
    """Return the points scored from rolling 0 dice (Free Bacon)."""
    # BEGIN PROBLEM 2
    if opponent_score < 10:
        return opponent_score + 1
    digits = []
    for x in str(opponent_score):
        digits.append(int(x))
    return max(digits) + 1

def hogtimus_prime(score):
    """Returns the next highest prime if the player's current score
    is prime.

    >>>hogtimus_prime(11)
    >>>13
    """
    def is_prime(score):
        if score == 1:
            return False
        elif score == 2:
            return True
        for i in range(2, (score//2 + 2)):
            if score%i == 0:
                return False
        return True
    def next_prime(score):
        score += 1
        # so that we are testing the confirmed prime number + 1
        while not(is_prime(score)):
        # runs the while loop until is_prime returns true
            score += 1
        return score
    if is_prime(score):
        return next_prime(score)
    return False


def take_turn(num_rolls, opponent_score, dice=six_sided):
    """Simulate a turn rolling NUM_ROLLS dice, which may be 0 (Free Bacon).
    Return the points scored for the turn by the current player. Also
    implements the Hogtimus Prime and When Pigs Fly rules.

    num_rolls:       The number of dice rolls that will be made.
    opponent_score:  The total score of the opponent.
    dice:            A function of no args that returns an integer outcome.
    """
    # Leave these assert statements here; they help check for errors.
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls >= 0, 'Cannot roll a negative number of dice in take_turn.'
    assert num_rolls <= 10, 'Cannot roll more than 10 dice.'
    assert opponent_score < 100, 'The game should be over.'
    # BEGIN PROBLEM 2
    if num_rolls == 0:
        return free_bacon(opponent_score)
    else:
        uncapped_score = roll_dice(num_rolls, dice)
        if hogtimus_prime(uncapped_score):
            uncapped_score = hogtimus_prime(uncapped_score)
            print(uncapped_score)
        elif uncapped_score > (25 - num_rolls):
            return (25 - num_rolls)
    return uncapped_score

print(take_turn(1,0,make_test_dice(3)))

    # END PROBLEM 2
