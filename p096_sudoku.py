#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 10:13:25 2024

@author: johannes
"""

import time
from sudoku import Board

if __name__ == '__main__':
    string_set = open("p096_sudoku.txt").read()
    puzzles = string_set.split('Grid')
    puzzles = [x[4:] for x in puzzles[1:]]
    total = 0
    
    t0 = time.time()
    for puzzle in puzzles:
        b = Board(puzzle)
        b.solve()
        total += b.array[0,2] + 10 * b.array[0,1] + 100 * b.array[0,0]
    print(total)
    t1 = time.time()
    print(f'Time: {t1-t0}')
