#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 21:34:51 2023

@author: johannes
"""

import numpy as np

class Puzzle:
    def __init__(self, board):
        self.board = np.fromiter(''.join(filter(str.isdigit, board)), dtype=np.uint8).reshape((9,9))
        self.squares = np.kron(np.arange(1,10).reshape((3,3)), np.ones((3,3))).astype(np.uint8)
        self.save = self.board
        self.choice = []
        self.options = self.board.astype(set)

    def getOptions(self):
        for pos in np.argwhere(self.board == 0):
            loc = tuple(pos)
            cols = set(self.board[:,loc[1]])
            rows = set(self.board[loc[0],:])
            sqrs = set(self.board[np.where(self.squares == self.squares[loc])])
            self.options[loc] = set(np.arange(1,10)) - (cols | rows | sqrs)

    def sureMoves(self):
        for pos in np.argwhere(self.board == 0):
            loc = tuple(pos)
            if len(self.options[loc]) == 1:
                self.board[loc] = self.options[loc].pop()

def procedure():
    puzzle = Puzzle(open("puzzle.txt").read())
    print(puzzle.board)
    while np.count_nonzero(puzzle.board==0) > 0:
        puzzle.getOptions()
        puzzle.sureMoves()
        print(".")
    print(puzzle.board)

if __name__ == "__main__":
    procedure()
