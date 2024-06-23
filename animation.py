#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 10:13:25 2024

@author: johannes
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from sudoku import Board

fig = plt.figure(0)
plt.axis('off')
frames = []

b = Board(open("puzzle.txt").read())
while np.count_nonzero(b.array == 0):
    b.move()
    frames.append([plt.imshow(b.entropies, cmap='inferno', vmin = 0, vmax = 9, animated=True)])

anim = animation.ArtistAnimation(fig, frames, interval=7)

writergif = animation.PillowWriter(fps=30)
anim.save('movie.gif', writer=writergif)
plt.show()
