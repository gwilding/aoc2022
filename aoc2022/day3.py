# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 15:34:49 2022

@author: gwilding
"""

import os
import sys

import numpy as np
import matplotlib.pyplot as plt

def ord2(ch):
    if isinstance(ch,list):
        return [ord2(ch) for ch in ch]
    return ord(ch.lower())-ord('a')+1+26*ch.isupper()

def parse_rucksacks(rucksack_list):
    shared_items = []
    for rucksack in rucksack_list:
        r1 = rucksack[:len(rucksack)//2]
        r2 = rucksack[len(rucksack)//2:]
        
        shared_item = set(r1).intersection(r2)
        shared_items.append(list(shared_item)[0])
    return shared_items, sum(ord2(shared_items))

def parse_groups(rucksack_list):
    n_rucksack = len(rucksack_list)
    shared_items = []
    for group_id in range(n_rucksack//3):
        r1 = rucksack_list[group_id*3]
        r2 = rucksack_list[group_id*3+1]
        r3 = rucksack_list[group_id*3+2]
        
        shared_item = set(r1).intersection(r2).intersection(r3)
        shared_items.append(list(shared_item)[0])
    return shared_items, sum(ord2(shared_items))
    

def main():
    
    input_path = 'input_day3.txt'
    input_day3 = np.genfromtxt(input_path,str)
    
    test_input = ['vJrwpWtwJgWrhcsFMMfFFhFp',
                  'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL',
                  'PmmdzqPrVvPwwTWBwg',
                  'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn',
                  'ttgJtRGJQctTZtZT',
                  'CrZsJsPPZsGzwwsLwLmpwMDw']
    
    # first half of items compartment 1, second half compartment 2
    
    ## part 1
    shared_items = []
    for rucksack in test_input:
        r1 = rucksack[:len(rucksack)//2]
        r2 = rucksack[len(rucksack)//2:]
        
        shared_item = set(r1).intersection(r2)
        shared_items.append(list(shared_item)[0])
    
    shared_items_test, ssum_test = parse_rucksacks(test_input)
    shared_items, ssum = parse_rucksacks(input_day3)
    
    print("Day 2, part 1:")
    print("Test",ssum_test)
    print("Solution",ssum)
    
    ## Part 2
    shared_items2_test, ssum2_test = parse_groups(test_input)
    shared_items2, ssum2 = parse_groups(input_day3)
    
    print("Day 2, part 2:")
    print("Test",ssum2_test)
    print("Solution",ssum2)
    
if __name__ == "__main__":
    main()
