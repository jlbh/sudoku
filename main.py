#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 10:13:25 2024

@author: johannes
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation


std = np.array([[4,0,5,7,0,0,0,0,0],
                [9,2,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,1,5,8],
                [0,0,0,0,0,0,0,6,9],
                [0,8,0,0,0,6,7,0,0],
                [0,9,0,0,0,0,0,0,1],
                [6,0,0,0,9,0,0,0,3],
                [0,0,0,0,0,7,6,0,0],
                [5,0,0,1,0,0,0,0,2]], dtype=np.int8)

class Board:
    def __init__(self, array):
        self.array = np.copy(array)
        self.boxes = np.kron(np.arange(1,10).reshape((3,3)), np.ones((3,3)))
        self.save = []
        self.entropies = 9 * np.ones((9,9), dtype=np.int8)

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
                else: 
                    if i[0] == j[0] or i[1] == j[1]:
                        count +=1
            if count >= record: 
                holder = i
                where = n
                record = count
        
        save = np.copy(self.array)
        save[tuple(holder)] = choices[where].pop()
        self.array[tuple(holder)] = choices[where].pop()
        self.save.append(save)
        return

def main():
    b = Board(std)
    print('Puzzle:')
    print(b.array)
    while np.count_nonzero(b.array == 0):
        b.move()
    print('Solution:')
    print(b.array)
    return

if __name__ == '__main__': main()