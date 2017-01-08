# -*- coding: utf-8 -*-
__author__ = 'Kord J.'

from setuptools import setup

setup(
    name = 'tg_math_prog_bot',
    packages = ['tg_math_prog_bot'],
    version = '0.0.1.dev0',
    description = 'A Python Telegram Bot for different calculations.',
    author = 'Kord J.',
    author_email = 'xxkord@gmail.com',
    url = 'https://github.com/xkord/telegram_calc_bot',
    download_url = 'https://github.com/xkord/telegram_calc_bot',
    keywords='telegram python messenger bot mathematic programming',
    classifiers = [
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Development Status :: 1 - Beta',
        'Environment :: Other Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: The MIT License (MIT)',
        'Operating System :: OS Independent'
    ],
    entry_points = {
        'console_scripts': ['tg_math_prog_bot = tg_math_prog_bot:main'],
    },
    test_suite='tg_math_prog_bot.tests',
    long_description = '''\

A Python Telegram Bot for different calculations.
Report any issues at https://github.com/xkord
README.md
------------------
'''
)