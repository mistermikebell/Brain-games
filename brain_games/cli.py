# -*- coding:utf-8 -*-

import prompt

def welcome_user():
	name = prompt.string('\nMay I have your name? ')
	print('Hello, {name}!'.format(name=name))
