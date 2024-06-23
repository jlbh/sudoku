#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 10:13:25 2024

@author: johannes
"""

from sudoku import Board

def main():
    b = Board(open("puzzle.txt").read())
    print(f'Puzzle:\n{b.array}')
    b.solve()
    print(f'Solution:\n{b.array}')
    return

if __name__ == '__main__': main()
