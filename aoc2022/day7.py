# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 07:41:32 2022

@author: gwilding
"""

import os
import sys

import numpy as np
import matplotlib.pyplot as plt

def parse_input(input_path):
    commands = []
    with open(input_path) as f:
        for index, line in enumerate(f):
            commands.append(line.strip())
    return commands

def parse_commands(commands):
    coms = []
    for com in commands:
        if com[0] == '$':
            coms.append([com[2:]])
        else:
            coms[-1].append(com)
    # replace double names
    # store all dirs, if ls yields a dir name that came up already:
    # -> change that ls
    # change next cd with dir name
    
    k = 0
    visited_dirs = []
    repeating_dirs = []
    while k < len(coms):
        if (coms[k][0].split()[0] == 'cd'
            and coms[k][0].split()[1] != '..'): # cd
            if 'dir ' + coms[k][0].split()[1] in visited_dirs:
                print('dir ' + coms[k][0].split()[1])
                repeating_dirs.append('dir ' + coms[k][0].split()[1])
                new_name = 'dir ' + coms[k][0].split()[1] + repeating_dirs.count('dir ' + coms[k][0].split()[1])
                change_next_cd_occurance_of_to = ('dir ' + coms[k][0].split()[1],new_name)
            visited_dirs.append('dir ' + coms[k][0].split()[1])
        
        k += 1
    
    [[c2 for c2 in c if c2.split()[0] in ['dir','cd']] for c in coms if not 'cd ..' in c]
    
    [c for c in coms if not 'cd ..' in c]
    
    [c2 for c2 in [c for c in coms]]
    
    [item for sublist in coms for item in sublist if (not item in ['cd ..','ls'] and item.split()[0] in ['cd','dir'])]
    
    k = 0
    
    
    return coms

def calc_size(dir_tree):
    # get direct directory sizes
    directories = {'dir /': 0}
    for key in dir_tree:
        if key.split()[0] == 'dir':
            directories['dir ' + key.split()[1]] = 0
    
    for file in dir_tree:
        if not file.split()[0] == 'dir':
            file_size = int(file.split()[0])
            parent_dir = dir_tree[file]
            while not parent_dir == 'dir /':
                directories[parent_dir] += file_size
                parent_dir = dir_tree[parent_dir]
                
            # once more for root
            directories[parent_dir] += file_size
    return directories
    

def build_dir_tree(commands):
    # commands = commands1_test
    
    coms = parse_commands(commands)
    
    # check this dir creation: dir nbpsdm
    
    dir_tree = {}
    # start at top
    current_level = '/'
    repetition_counter = []
    change_next_cd_occurrence = []
    for command_id,com in enumerate(coms):
        print(com)
        c = com[0].split()
        # if 'dir nbpsdm' in com:
        #     break
        if c[0] == 'cd': # change dir
            # if 'dir ' + c[1] in dir_tree:
            #     break
            if c[1] == '/':
                current_level = 'dir /'
            elif c[1] == '..':
                if len(change_next_cd_occurrence) == 2 and current_level == change_next_cd_occurrence[0]:
                    current_level = change_next_cd_occurrence[1]
                current_level = dir_tree[current_level]
            else:
                
                current_level = 'dir ' + c[1] # + str(append_name)
                if len(change_next_cd_occurrence) == 2 and current_level == change_next_cd_occurrence[0]:
                    current_level = change_next_cd_occurrence[1]
                    
        elif c[0] == 'ls': # list dir
            contents = com[1:]
            for content in contents:
                if content in dir_tree:
                    repetition_counter.append(content)
                    append_name = repetition_counter.count(content)
                    # change next cd <content>
                    # for c2change in coms[command_id:]:
                        
                    
                    dir_tree[content + str(append_name)] = current_level
                    change_next_cd_occurrence = [content, content + str(append_name)]
                else: dir_tree[content] = current_level
    return dir_tree

    # dir1 = {'a':'/','584 i':'dir e','e':'a'}

class tree():
    def __init__(self, name, parent, size = 0):
        self.name = name
        self.parent = parent
        self.size = size
        self.children = []
    def add_child(self, node):
        self.children.append(node)
    def get_size(self):
        # if self.size == 0:
        #     return self.size
        for child in self.children:
            self.size += child.size
    # def __repr__(self):
    #     return '\n' + self.name + '  ' + '\n'.join([c.name for c in self.children])
    
def create_tree(commands):
    root = tree('/', None)
    current_dir = root
    current_path = ['/']
    
    for com in commands:
        com = com.split()
        
        if com[0] == '$':
            # this is a command
            if com[1] == 'cd':
                if com[2] == '..':
                    # move up
                    current_path.pop()
                    current_dir = current_dir.parent
                else:
                    # move into dir
                    for child in current_dir.children:
                        if child.name == com[2] and child.size == 0:
                            current_dir = child
                            break
                    # append dir to path
                    current_path.append(com[2])
        else:
            # if not a commmand, the first part will be "dir" or a file size
            if com[0] == 'dir':
                current_dir.add_child(tree(com[1], current_dir))
            else:
                current_dir.add_child(tree(com[1], current_dir, int(com[0])))
                
    directories = get_dir_size(root)
    return root, directories

def get_dir_size(current_dir, directories=None):
    if isinstance(directories,type(None)):
        directories = []
    for child in current_dir.children:
        if child.size == 0: # if children is another directory, calculate its size
            directories = get_dir_size(child, directories)
    
    current_dir.get_size()
    directories.append((current_dir.name, current_dir.size))
    
    return directories
    

# class DirTree(object):
#     "Generic tree node."
#     def __init__(self, name='/', children=None):
#         self.name = name
#         self.children = []
#         if children is not None:
#             for child in children:
#                 self.add_child(child)
#     def __repr__(self):
#         return self.name
#     def add_child(self, node):
#         assert isinstance(node, Tree)
#         self.children.append(node)

    
# def evaluate_com(com):
#     current_level = '/'
#     if com[0] == '$':
#         c = com[2:].split()
#         if c[0] == 'cd': # change dir
#             if c[1] == '/':
#                 pass
#             elif c[1] == '..':
#                 pass
#             else:
                
#         elif c[0] == 'ls': # list dir
#             pass
        
        
       

def main():
    input_path = 'input_day7.txt'
    input_path_test = 'input_day7_test.txt'
    test_solutions1 = 95437
    
    ## part 1:
    commands1 = parse_input(input_path)
    commands1_test = parse_input(input_path_test)
    
    # testing (old)
    dir_tree1 = build_dir_tree(commands1)
    dir_tree1_test = build_dir_tree(commands1_test)

    dir_sizes1 = calc_size(dir_tree1)
    dir_sizes1_test = calc_size(dir_tree1_test)
    
    solution_test_part1 = sum((np.array(list(dir_sizes1_test.values()))<100000)*np.array(list(dir_sizes1_test.values())))
    solution_part1 = sum((np.array(list(dir_sizes1.values()))<100000)*np.array(list(dir_sizes1.values())))
    
    # testing new
    root_test, directories_test = create_tree(commands1_test)
    root, directories = create_tree(commands1)
    
    directory_sizes_test = np.array([size for name, size in directories_test])
    test_part1 = sum(directory_sizes_test*(directory_sizes_test <= 100000))

    directory_sizes = np.array([size for name, size in directories])
    solution_part1 = sum(directory_sizes*(directory_sizes <= 100000))
    
    directory_sizes[(directory_sizes >= 30000000) & (directory_sizes <= 70000000)]
    
    
    
    print("Day 2, part 1:")
    print("Solution",solution_part1)
    
    ## part 2:
    # testing
    unused_space_test = 70000000 - root_test.size
    needed_space_test = 30000000 - unused_space_test
    test_part2 = min(directory_sizes_test[directory_sizes_test >= needed_space_test])
    
    # solution
    unused_space = 70000000 - root.size
    needed_space = 30000000 - unused_space
    
    solution_part2 = min(directory_sizes[directory_sizes >= needed_space])
    
    
    print("Day 2, part 1:")
    print("Solution",solution_part2)

    
if __name__ == "__main__":
    main()
