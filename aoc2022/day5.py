# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 08:34:32 2022

@author: gwilding
"""

import os
import sys

import numpy as np
import matplotlib.pyplot as plt

def parse_input(input_path):
    header = []
    instructions = []
    with open(input_path) as f:
        for index, line in enumerate(f):
            header.append(line.strip('\n'))
            if not line.strip():
                header.pop(-1)
                break
        for index, line in enumerate(f):
            instructions.append(line.strip())
    return header, instructions

def parse_cargo_piles(header):
    n_stacks = len(header[-1].split())
    stack_height = len(header) - 1
    stack_ids = list(range(n_stacks))
    
    expected_str_len = n_stacks*3 + n_stacks - 1
    
    stacks_raw = header[:-1]
    
    
    
    stacks = []# [[] for ks in range(n_stacks)]
    for stack in stack_ids:
        # parse vertically
        stacks.append([])
        for yid in range(stack_height):
            if stacks_raw[yid][stack*4+1:stack*4+2].strip():
                stacks[-1].append(stacks_raw[yid][stack*4+1:stack*4+2].strip())
        stacks[-1] = stacks[-1][::-1]
    return stacks
    
class manifest:
    def __init__(self,header):
        if isinstance(header,str):
            header, instructions = parse_input(header)
        stacks = parse_cargo_piles(header)
        self.stacks = stacks
    
    def __str__(self):
        return stacks
    
    def evaluate(self):
        return ''.join([s[-1] for s in self.stacks])
    
    def do(self,instruction_str):
        if isinstance(instruction_str,list):
            for instr in instruction_str:
                self.do(instr)
        else:
            
            number, source, target = self.parse_instruction(instruction_str)
            # print(instruction_str,":",number, source, target)
            for n in range(number):
                moving = self.stacks[source].pop()
                self.stacks[target].append(moving)
                # print(self.stacks,'\n')
            # for s in self.stacks:
                
    def do9001(self,instruction_str):
        if isinstance(instruction_str,list):
            for instr in instruction_str:
                self.do9001(instr)
        else:
            
            number, source, target = self.parse_instruction(instruction_str)
            # print(instruction_str,":",number, source, target)
            moving = self.stacks[source][-number:]
            for n in range(number):
                self.stacks[source].pop()
            self.stacks[target].extend(moving)  
        
    def parse_instruction(self,instruction_str):
        _, number, _, source, _, target = instruction_str.split(' ')
        number = int(number)
        source = int(source) - 1
        target = int(target) - 1
        return number, source, target
    
    def parse_cargo_piles(header):
        n_stacks = len(header[-1].split())
        stack_height = len(header) - 1
        stack_ids = list(range(n_stacks))
        
        expected_str_len = n_stacks*3 + n_stacks - 1
        
        stacks_raw = header[:-1]
        
        stacks = []
        for stack in stack_ids:
            # parse vertically
            stacks.append([])
            for yid in range(stack_height):
                if stacks_raw[yid][stack*4+1:stack*4+2].strip():
                    stacks[-1].append(stacks_raw[yid][stack*4+1:stack*4+2].strip())
            stacks[-1] = stacks[-1][::-1]
        return stacks
    def parse_input(input_path):
        header = []
        instructions = []
        with open(input_path) as f:
            for index, line in enumerate(f):
                header.append(line.strip('\n'))
                if not line.strip():
                    header.pop(-1)
                    break
            for index, line in enumerate(f):
                instructions.append(line.strip())
        return header, instructions

def main():
    
    input_path = 'input_day5.txt'
    input_path_test = 'input_day5_test.txt'
    
    header_test, instructions_test = parse_input(input_path_test)
    header, instructions = parse_input(input_path)
    
    stacks_test = parse_cargo_piles(header_test)
    stacks = parse_cargo_piles(header)
    
    ## part 1:
    cargo_test = manifest(header_test)
    cargo_test.do(instructions_test)
    cargo_test.stacks
    cargo_test.evaluate()
    
    cargo = manifest(header)
    cargo.do(instructions)
    cargo.stacks
    cargo.evaluate()

    
    print("Day 2, part 1:")
    print("Test",cargo_test.evaluate())
    print("Solution",cargo.evaluate())
    
    ## part 2:
    cargo_test2 = manifest(header_test)
    cargo_test2.do9001(instructions_test)
    cargo_test2.stacks
    cargo_test2.evaluate()
    
    cargo2 = manifest(header)
    cargo2.do9001(instructions)
    cargo2.stacks
    cargo2.evaluate()
    
    
    print("Day 2, part 1:")
    print("Test",cargo_test2.evaluate())
    print("Solution",cargo2.evaluate())
    

if __name__ == "__main__":
    main()
