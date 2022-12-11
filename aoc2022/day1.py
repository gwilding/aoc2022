# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 07:18:47 2022

@author: gwilding
"""

import os
import sys

import numpy as np
import matplotlib.pyplot as plt

def main():
    input_path = 'input_day1.txt'
    input_day1 = np.genfromtxt("input_day1.txt")

        
    with open(input_path) as f:
        elves_list = []
        elves_list.append(0)
        for index, line in enumerate(f):
            if line.strip():
                elves_list[-1] += int(line.strip())
            else:
                elves_list.append(0)
    
    # part 1
    print("Day 1, part 1:")
    print(max(elves_list))
    
    # part 2
    print("Day 1, part 2:")
    print(sum(sorted(elves_list,reverse=True)[:3]))

if __name__ == "__main__":
    main()
