# -*- coding:utf-8 -*-

"""
Ask users name
Date created: 06/09/2020
"""

import prompt


def welcome_user():
    """Return user's name."""
    name = prompt.string('\nMay I have your name? ')
    return print('Hello, {name}!'.format(name=name))
