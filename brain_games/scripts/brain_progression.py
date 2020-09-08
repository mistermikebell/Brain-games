# -*- coding:utf-8 -*-

"""Odd game."""

from brain_games.games import game_process


def main():
    """Starting even game."""
    print("Welcome to the Brain Games!\nWhat number is missing in the progression?.")
    game_process.game('progression')


if __name__ == '__main__':
    main()