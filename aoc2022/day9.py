# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 20:46:19 2022

@author: gwilding
"""

import os
import sys

import numpy as np
import matplotlib.pyplot as plt

def load_motions(input_path):
    """
    Load input motions.

    """
    rows = []
    with open(input_path) as f:
        for line in f:
            rows.append(line.strip().split())
    rows = [(r[0], int(r[1])) for r in rows]
    return rows

# old rope class for part 1, only small delta needed for chain class to also
# work for part 1
# class rope():
#     def __init__(self):
#         self.H = np.array([0,0])
#         self.T = np.array([0,0])
#         self.trans = {'U': np.array([0,1]),
#                       'D': np.array([0,-1]),
#                       'R': np.array([1,0]),
#                       'L': np.array([-1,0])}
#         self.Hlog = np.array([0,0])
#         self.Tlog = np.array([0,0])
#         # up -> column index positiv
#     def __repr__(self):
#         return 'H: %s - T: %s'%(str(self.H),str(self.T))
#     def line2motion(self,line):
#         return self.trans[line[0]]*line[1]

#     def moveH(self,line):
#         if isinstance(line,list):
#             for l in line:
#                 self.moveH(l)
#         else:
#             n = line[1]
#             line = (line[0],np.sign(line[1]))
#             for k in range(n):
#                 self.H = self.H + self.line2motion(line)
#                 self.Hlog = np.vstack((self.Hlog,self.H))
#                 self.CheckAndCorrect()
#     def CheckAndCorrect(self):
#         diff = self.H - self.T
#         while np.any(np.abs(diff) > 1):
#             self.T += np.sign(diff)*np.any(np.abs(diff) > 1)
#             self.Tlog = np.vstack((self.Tlog,self.T))
#             diff = self.H - self.T

#     def make_map_tail(self):
#         step_map_size = (np.min(self.Hlog),np.max(self.Hlog))
#         incr = -step_map_size[0]
#         n = step_map_size[1] + incr

#         step_map = np.zeros((n+1,n+1),int)
#         for s in self.Tlog:
#             step_map[s[1]+incr,s[0]+incr] += 1
#         self.step_map = step_map
#         return step_map[::-1,:]

class chain():
    """
    Class to simulate a chain of n moving links. Not very efficient.
    """
    def __init__(self, n=2):
        self.knots = [np.array([0, 0]) for k in range(n)]
        self.trans = {'U': np.array([0, 1]),
                      'D': np.array([0, -1]),
                      'R': np.array([1, 0]),
                      'L': np.array([-1, 0])}
        # up -> column index positiv
        self.Tlog = np.array([0, 0])

    def __repr__(self):
        return 'T' + '-'.join([str(k) for k in self.knots]) + 'H'
    def line2motion(self, line):
        """
        Convert line input (<U/D/L/R> n) to (dx, dy).
        """
        return self.trans[line[0]]*line[1]

    def moveH(self, line):
        """
        Move head according to line, or a list of lines.
        """
        if isinstance(line, list):
            for l in line:
                self.moveH(l)
        else:
            n = line[1]
            line = (line[0], np.sign(line[1]))
            for k in range(n):
                self.knots[-1] = self.knots[-1] + self.line2motion(line)
                self.CheckAndCorrect()
    def CheckAndCorrect(self):
        """
        Update positions of chain of knots.
        """
        for k in range(len(self.knots)-2, -1, -1):
            diff = self.knots[k+1] - self.knots[k]
            self.knots[k] += np.sign(diff)*np.any(np.abs(diff) > 1)
        self.Tlog = np.vstack((self.Tlog, self.knots[0]))

    def make_map_tail(self):
        """
        Create a map of tiles visited by the tail.
        """
        step_map_size = (np.min(self.Tlog), np.max(self.Tlog))
        incr = -step_map_size[0]
        size = step_map_size[1] + incr

        step_map = np.zeros((size+1, size+1), int)
        for step in self.Tlog:
            step_map[step[1]+incr, step[0]+incr] += 1
        self.step_map = step_map

        return step_map[::-1, :]


def main():
    input_path = 'input_day9.txt'
    input_path_test = 'input_day9_test.txt'
    input_path_test_large = 'input_day9_test_large.txt'

    test_motions = load_motions(input_path_test)
    test_motions_large = load_motions(input_path_test_large)
    motions = load_motions(input_path)

    # part 1
    test1_solution = 13
    test_rope = chain()
    test_rope.moveH(test_motions)
    test_map1 = test_rope.make_map_tail()

    rope1 = chain()
    rope1.moveH(motions)
    map1 = rope1.make_map_tail()

    test1 = (test_map1 >= 1).sum()
    solution1 = (map1 >= 1).sum()

    print("Test 1 = ", test1, '==', test1_solution, ":", test1 == test1_solution)
    print("Solution 2 = ", solution1, "Correct")


    # part 2
    # testing consistency with part 1
    test_chain1 = chain()
    test_chain1.moveH(test_motions)
    test_map1 = test_chain1.make_map_tail()

    # testing part 2
    test2_solution = 36
    test_chain2 = chain(10)
    test_chain2.moveH(test_motions_large)
    test_map2 = test_chain2.make_map_tail()
    test2 = (test_map2 >= 1).sum()

    chain2 = chain(10)
    chain2.moveH(motions)
    map2 = chain2.make_map_tail()
    solution2 = (map2 >= 1).sum()

    print("Test 2 = ", test2, '==', test2_solution, ":", test2 == test2_solution)
    print("Solution 2 = ", solution2)

if __name__ == "__main__":
    main()
