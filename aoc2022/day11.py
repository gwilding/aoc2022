# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 18:56:13 2022

@author: gwilding
"""

import os
import sys

import numpy as np
import matplotlib.pyplot as plt
import math

def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)

def prod(lin):
    r = 1
    for l in lin:
        r *= l
    return r

def load_input(input_path):
    """
    Load input.

    """
    rows = []
    with open(input_path) as f:
        for line in f:
            rows.append(line.strip().split())
            
    monkeys = []
    collect = []
    for row in rows:
        if len(collect) < 6:
            collect.append(row)
        else: # make monkey
            items = [int(c.strip(',')) for c in collect[1][2:]]
            operation = eval('lambda old: %s'%' '.join(collect[2][3:]) )
            test = int(collect[3][-1].strip())
            pass_to = (int(collect[5][-1].strip()),int(collect[4][-1].strip()))
            monkeys.append((items,
                      operation,
                      test,
                      pass_to
                      ))
            collect = []
    items = [int(c.strip(',')) for c in collect[1][2:]]
    operation = eval('lambda old: %s'%' '.join(collect[2][3:]) )
    test = int(collect[3][-1].strip())
    pass_to = (int(collect[5][-1].strip()),int(collect[4][-1].strip()))
    monkeys.append((items,
              operation,
              test,
              pass_to
              ))
    return monkeys

def monkeys_play(monkeys, rounds, worry_decrease = 3):
    
    # monkeys = list_of_monkeys
    inpsect_counts = [0 for m in monkeys]
    
    # worry needs to be checked against:
    mod = prod([m[2] for m in monkeys])
    
    for r in range(rounds):
        # loop through monkeys:
        for monkey_id, monkey in enumerate(monkeys):
            while len(monkey[0]):
                item = monkey[0].pop(0)
                item = (monkey[1](item)//worry_decrease)%mod # inspect
                pass_to_monkey = monkey[3][item%monkey[2] == 0]
                monkeys[pass_to_monkey][0].append(item)
                inpsect_counts[monkey_id] += 1
    return inpsect_counts
            
            # 
    

def main():
    input_path = 'input_day11.txt'
    input_path_test1 = 'input_day11_test1.txt'
    
    monkeys1 = load_input(input_path)
    
    ##! part 1
    test1_solution = 10605
    
    
    # test code here
    # monkeys = [([79, 98],
    #             lambda x: x*19,
    #             23,
    #             (3, 2)),
    #            ([54, 65, 75, 74],
    #             lambda x: x + 6,
    #             19,
    #             (0, 2)),
    #            ([79, 60, 97],
    #             lambda x: x*x,
    #             13,
    #             (3, 1)),
    #            ([74],
    #             lambda x: x + 3,
    #             17,
    #             (1,0))]
    
    monkeys_test = load_input(input_path_test1)
    inspection_count_test = monkeys_play(monkeys_test,20)
    test1 = np.prod(sorted(inspection_count_test)[-2:])
    
    # solution code here
    inspection_count1 = monkeys_play(monkeys1,20)
    solution1 = np.prod(sorted(inspection_count1)[-2:])

    print("Test 1 = ", test1, '==', test1_solution, ":", test1 == test1_solution)
    print("Solution 1 = ", solution1, "Correct")
    
    ##! part 2
    
    
    test2_solution = 2713310158
    
    # test code here
    monkeys_test = load_input(input_path_test1)
    # recheck test 1
    inspection_count_test = monkeys_play(monkeys_test,20)
    test1 = np.prod(sorted(inspection_count_test)[-2:])
    # test 2
    monkeys_test = load_input(input_path_test1)
    inspection_count_test = monkeys_play(monkeys_test,10000, worry_decrease = 1)
    test2 = prod(sorted(inspection_count_test)[-2:])
    
    # solution code here
    monkeys1 = load_input(input_path)
    inspection_count2= monkeys_play(monkeys1,10000, worry_decrease = 1)
    solution2 = prod(sorted(inspection_count2)[-2:])


    print("Test 2 = ", test2, '==', test2_solution, ":", test2 == test2_solution)
    print("Solution 2 = ", solution2, "Correct")
    
if __name__ == "__main__":
    main()
