#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 10:13:25 2024

@author: johannes
"""

from sudoku import Board
import time

if __name__ == '__main__':
    b = Board(open("puzzle.txt").read())
    print(f'Puzzle:\n{b.array}')
    t0 = time.time()
    b.solve()
    t1 = time.time()
    print(f'Solution:\n{b.array}\nTime: {t1-t0}')