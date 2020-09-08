# -*- coding:utf-8 -*-

"""Odd game."""

from brain_games.games import game_process


def main():
    """Starting even game."""
    print('Welcome to the Brain Games!\nWhat is the result of the expression?')
    game_process.game('calc')


if __name__ == '__main__':
    main()
