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
        self.count = 0
        self.solutions = []

    def getOptions(self):
        if np.all(self.board):
            print("Done with this branch!")
            self.solutions.append(self.board)
            self.count += 1
            self.backTrack()
            return True
        for pos in np.argwhere(self.board == 0):
            loc = tuple(pos)
            cols = set(self.board[:,loc[1]])
            rows = set(self.board[loc[0],:])
            sqrs = set(self.board[np.where(self.squares == self.squares[loc])])
            self.options[loc] = set(np.arange(1,10)) - (cols | rows | sqrs)
            if len(self.options[loc]) == 0:
                if len(self.choice) == 0:
                    print("No more branches!")
                    print(f"{self.count} solutions found!")
                    return False
                print("Wrong choice")
                self.backTrack()
        return True

    def sureMove(self):
        did_move = False
        for pos in np.argwhere(self.board == 0):
            loc = tuple(pos)
            if len(self.options[loc]) == 1:
                did_move = True
                move = self.options[loc].pop()
                self.board[loc] = move
                self.options[loc] = move
        return did_move
                
    def guessAndSave(self):
        record = 10
        for pos in np.argwhere(self.board == 0):
            loc = tuple(pos)
            if len(self.options[loc]) < record:
                record = len(self.options[loc])
                winner = loc
        move = self.options[winner].pop()
        self.save = np.dstack((self.save, self.board))
        self.board[winner] = move
        self.choice.append([winner, move])
            
    def backTrack(self):
        self.board = self.save[:,:,-1]
        self.getOptions()
        self.options[self.choice[-1][0]] -= ({self.choice[-1][1]})
        self.choice = self.choice[:-1]
        self.save = self.save[:,:,:-1]

def procedure():
    puzzle = Puzzle(open("puzzle.txt").read())
    print(puzzle.board)
    keep_going = True
    while keep_going:
        keep_going = puzzle.getOptions()
        if puzzle.sureMove():
            pass
        else: puzzle.guessAndSave()
    print(puzzle.solutions)

if __name__ == "__main__":
    procedure()
