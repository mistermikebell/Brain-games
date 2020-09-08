# -*- coding:utf-8 -*-

"""Odd game."""

from brain_games.games import game_process


def main():
    """Starting odd game."""
    print('Welcome to the Brain Games!\nAnswer\
 "yes" if number even otherwise answer "no".')
    game_process.game('even')


if __name__ == '__main__':
    main()
