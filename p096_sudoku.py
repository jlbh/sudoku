#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 10:13:25 2024

@author: johannes
"""

import time
import numpy as np

class Board:
    def __init__(self, puzzle):
        self.array = np.fromiter(''.join(filter(str.isdigit, puzzle)), dtype=np.uint8).reshape((9,9))
        self.boxes = np.kron(np.arange(1,10).reshape((3,3)), np.ones((3,3)))
        self.save = []
        self.entropies = np.ones((9,9), dtype=np.int8)

    def move(self):
        choices = []
        twos = []
        for i in np.argwhere(self.array == 0):
            row = self.array[i[0],:]
            col = self.array[:,i[1]]
            box = self.array[np.where(self.boxes == self.boxes[tuple(i)])]

            choice = set(range(10)) - (set(row) | set(col) | set(box))
            entropy = len(choice)
            self.entropies[tuple(i)] = entropy
            
            if entropy == 0:
                self.array = np.copy(self.save.pop())
                return
            if entropy == 1:
                self.array[tuple(i)] = choice.pop()
                return
            if entropy == 2: 
                choices.append(choice)
                twos.append(i)
                
        record = 0
        holder = None
        where = None
        
        for n, i in enumerate(twos):
            count = 0
            for j in twos:
                if i.all() == j.all():
                    pass
                if self.boxes[tuple(i)] == self.boxes[tuple(j)]:
                    count += 1
                elif i[0] == j[0] or i[1] == j[1]:
                    count +=1
            if count >= record: 
                holder = i
                where = n
                record = count
        
        save = np.copy(self.array)
        save[tuple(holder)] = choices[where].pop()
        self.array[tuple(holder)] = choices[where].pop()
        self.save.append(save)
    
    def solve(self):
        while np.count_nonzero(self.array == 0):
            self.move()

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