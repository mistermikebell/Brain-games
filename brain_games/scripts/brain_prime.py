# -*- coding:utf-8 -*-

"""Prime game."""

from brain_games.games import game_process


def main():
    """Starting prime game."""
    print('Welcome to the Brain Games!\nAnswer "yes" if given number\
 is prime. Otherwise answer "no".')
    game_process.game('prime')


if __name__ == '__main__':
    main()
