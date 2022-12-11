# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 18:59:14 2022

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

def main():
    input_path = 'input_day12.txt'
    input_path_test1 = 'input_day12_test1.txt'
    input_path_test2 = 'input_day12_test2.txt'
    
    instructions = load_instructions(input_path)
    instructions_test1 = load_instructions(input_path_test1)
    instructions_test2 = load_instructions(input_path_test2)
    
    ##! part 1
    test1_solution = None
    test2_solution = None
    
    # test code here
    test1 = None
    test2 = None
    
    # solution code here
    solution1 = None

    print("Test 1 = ", test1, '==', test1_solution, ":", test1 == test1_solution)
    print("Test 2 = ", test2, '==', test2_solution, ":", test2 == test2_solution)
    print("Solution 1 = ", solution1, "Correct")
    
    ##! part 2
    test1_solution = None
    test2_solution = None
    
    # test code here
    test1 = None
    test2 = None
    
    # solution code here
    solution2 = None

    print("Test 1 = ", test1, '==', test1_solution, ":", test1 == test1_solution)
    print("Test 2 = ", test2, '==', test2_solution, ":", test2 == test2_solution)
    print("Solution 2 = ", solution2, "Correct")

if __name__ == "__main__":
    main()
