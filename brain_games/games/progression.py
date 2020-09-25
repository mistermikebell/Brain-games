# -*- coding:utf-8 -*-

"""Find missing number in a progression."""

from brain_games import game_logic

import random


def generate_task():
    """Missing number in a progression function."""
    STEP_LIMIT = 9
    FIRST_NUM_LIMIT = 100
    LAST_NUM_LIMIT = 200
    PROGRESSION_LEN = 9
    step = random.randint(1, STEP_LIMIT)
    first_number = random.randint(1, FIRST_NUM_LIMIT)
    full_progression = range(first_number, LAST_NUM_LIMIT, step)
    progression = [str(i) for i in full_progression[:PROGRESSION_LEN]]
    question_index = random.randint(0, PROGRESSION_LEN)
    answer = progression[question_index]
    progression[question_index] = ".."
    question = " ".join(progression)
    return question, answer


def init_game():
    DESCRIPTION = 'What number is missing in the progression?'
    game_logic.play(generate_task, DESCRIPTION)
