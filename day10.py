# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 15:20:23 2022

@author: gwilding
"""

import os
import sys

import numpy as np
import matplotlib.pyplot as plt

def load_instructions(input_path):
    """
    Load input.

    """
    rows = []
    with open(input_path) as f:
        for line in f:
            rows.append(line.strip().split())
    rows = [tuple(int(r2) if r2.lstrip('-+').isnumeric() else r2 for r2 in r) for r in rows]
    return rows

class tube():
    def __init__(self):
        self.X = 1
        self.cycles = 0
        self.log = []
        self.screen_width  = 40
        self.screen_height =  6
        self.screen = ['' for row in range(self.screen_height)]
    def __repr__(self):
        return '%i @ cycle %i'%(self.X,self.cycles)
    def run(self,instruction):
        if isinstance(instruction,list):
            for instr in instruction:
                self.run(instr)
        else:
            # print(instruction)
            if instruction[0] == 'noop':
                self.noop()
            elif instruction[0] == 'addx':
                self.addx(instruction[1])
    def noop(self, n_cycles = 1):
        self.incr_cycle()
    def addx(self, add, n_cycles = 2):
        self.incr_cycle(n_cycles)
        self.X += add
        
    def incr_cycle(self, n_cycles=1):
        for k in range(n_cycles):
            self.cycles += 1
            if self.cycles == 20 or (self.cycles+20)%40 == 0:
                self.log.append([self.cycles,self.X,self.cycles*self.X])
            draw_in_row = (self.cycles-1)//self.screen_width
            pixel = (self.cycles-1)%self.screen_width # draw at this pixel
            if abs(self.X - pixel) <= 1:
                self.screen[draw_in_row] = self.screen[draw_in_row] + '#'
            else:
                self.screen[draw_in_row] = self.screen[draw_in_row] + '.'
    def result(self):
        return np.array(self.log)[:,-1].sum()
        

def main():
    input_path = 'input_day10.txt'
    input_path_test1 = 'input_day10_test1.txt'
    input_path_test2 = 'input_day10_test2.txt'
    
    instructions = load_instructions(input_path)
    instructions_test1 = load_instructions(input_path_test1)
    instructions_test2 = load_instructions(input_path_test2)
    
    
    # part 1
    test1_solution = None
    test2_solution = 13140
    
    tube_test1 = tube()
    tube_test1.run(instructions_test1)
    
    tube_test2 = tube()
    tube_test2.run(instructions_test2)
    # tube_test2.log
    tube_test2.result()
    
    tube1 = tube()
    tube1.run(instructions)
    tube1.log
    tube1.result()
    
    test2 = tube_test2.result()
    solution1 = tube1.result()

    print("Test 1 = ", test2, '==', test2_solution, ":", test2 == test2_solution)
    print("Solution 2 = ", solution1, "Correct")
    
    # part 2
    test2_solution = ['##..##..##..##..##..##..##..##..##..##..',
                      '###...###...###...###...###...###...###.',
                      '####....####....####....####....####....',
                      '#####.....#####.....#####.....#####.....',
                      '######......######......######......####',
                      '#######.......#######.......#######.....']
    
    
    tube_test2 = tube()
    tube_test2.run(instructions_test2)
    tube_test2.screen
    tube_test2.result()
    test2 = tube_test2.screen
    
    tube2 = tube()
    tube2.run(instructions)
    tube2.screen
    
    solution2 = tube2.screen
    
    print("Test 2 = ", test2, '==', test2_solution, ":", test2 == test2_solution)
    print("Solution 2 = \n", solution2,"\nCORRECT")
    
if __name__ == "__main__":
    main()
