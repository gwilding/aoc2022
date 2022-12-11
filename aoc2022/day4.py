# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 08:15:27 2022

@author: gwilding
"""

import os
import sys

import numpy as np
import matplotlib.pyplot as plt

def parse_input(section_input):
    parsed_input = []
    for s in section_input:
        parsed_input.append([tuple(int(s) for s in s.split('-')) for s in s.split(',')])
    return parsed_input

def get_fully_contained(parsed_input):
    fully_contained = []
    for areas in parsed_input:
        fully_contained.append((areas[0][0] - areas[1][0])*(areas[0][1] - areas[1][1]) <= 0)
    return fully_contained

def get_any_overlap(parsed_input):
    any_overlap = []
    for areas in parsed_input:
        any_overlap.append(any([r in range(areas[0][0],areas[0][1]+1) for r in range(areas[1][0],areas[1][1]+1)]) or 
                           any([r in range(areas[1][0],areas[1][1]+1) for r in range(areas[0][0],areas[0][1]+1)]))
    return any_overlap

def main():
    
    input_path = 'input_day4.txt'
    input_day4 = np.genfromtxt(input_path,str)
    
    test_input = [
            '2-4,6-8',
            '2-3,4-5',
            '5-7,7-9',
            '2-8,3-7',
            '6-6,4-6',
            '2-6,4-8']
    
    ## part 1:
    fully_contained1_test = get_fully_contained(parse_input(test_input))
    fully_contained1 = get_fully_contained(parse_input(input_day4))
    
    print("Day 2, part 1:")
    print("Test",sum(fully_contained1_test))
    print("Solution",sum(fully_contained1))
    
    ## part 2:
    any_overlap_test = get_any_overlap(parse_input(test_input))
    any_overlap = get_any_overlap(parse_input(input_day4))
    
    print("Day 2, part 1:")
    print("Test",sum(any_overlap_test))
    print("Solution",sum(any_overlap))
    
    

if __name__ == "__main__":
    main()
