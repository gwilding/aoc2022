# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 17:48:56 2022

@author: gwilding
"""

import os
import sys

import numpy as np
import matplotlib.pyplot as plt

def load_map(input_path):
    rows = []
    with open(input_path) as f:
        for index, line in enumerate(f):
            rows.append(line.strip())
    
    map_size = (len(rows),len(rows[0]))
    
    forest = np.zeros(map_size,dtype=int)
    
    for row_id,row in enumerate(rows):
        for col_id,value in enumerate(row):
            forest[row_id,col_id] = value
    return forest

def view_from_left(forest,visible):
    # from left
    for row_id,row in enumerate(forest):
        current_height = -1
        for col_id, height in enumerate(row):
            if height > current_height:
                visible[row_id,col_id] = True
                current_height = height
            elif current_height == 9:
                break
    return visible

def get_visible_trees(forest):
    # visible from left
    visible = forest*False
    visible[:,0] = True
    visible[0,:] = True
    visible[:,-1] = True
    visible[-1,:] = True
    
    # from left
    visible = view_from_left(forest,visible)
    # plt.matshow(visible)
    
    # view from right
    visible = np.fliplr(view_from_left(np.fliplr(forest),np.fliplr(visible)))
    # plt.matshow(visible)
    
    # top (transposed)
    visible = view_from_left(forest.T,visible.T).T
    # plt.matshow(visible)
    
    # bottom (transposed)
    visible = np.fliplr(view_from_left(np.fliplr(forest.T),np.fliplr(visible.T))).T
    # plt.matshow(visible)
    
    return visible, np.sum(visible)

def look(trees):
    tmp = np.where(trees[1:] >= trees[0])
    if len(tmp[0]):
        tmp = tmp[0][0] + 1
    else:
        tmp = len(trees) - 1
    return tmp

def look_row(trees):
    start = 0
    scene = trees*0 + 1
    while start < len(trees):
        scene[start] = look(trees[start:])
        start += 1
    return scene

def evaluate_scenic_score(forest):
    scenic_score = np.ones_like(forest)
    scenic_score[:,0] = 0
    scenic_score[0,:] = 0
    scenic_score[:,-1] = 0
    scenic_score[-1,:] = 0
    
    # look right
    look_right = np.zeros_like(forest)
    look_left = np.zeros_like(forest)
    look_up = np.zeros_like(forest)
    look_down = np.zeros_like(forest)
    for row_id, trees in enumerate(forest):
        look_right[row_id,:] = look_row(trees)
    # look down
    for row_id, trees in enumerate(forest.T):
        look_down.T[row_id,:] = look_row(trees)
        # scenic_score.T[row_id,:] *= look_row(trees)
    # look left
    for row_id, trees in enumerate(np.fliplr(forest)):
        look_left[row_id,::-1] = look_row(trees)
        # np.fliplr(scenic_score)[row_id,:] *= look_row(trees)
    # look up
    for row_id, trees in enumerate(np.fliplr(forest.T)):
        look_up.T[row_id,::-1] = look_row(trees)
    
    scenic_score *= (look_right*look_left*look_up*look_down)
            
    return scenic_score
    

def main():
    input_path = 'input_day8.txt'
    input_path_test = 'input_day8_test.txt'
    
    test_forest = load_map(input_path_test)
    forest = load_map(input_path)
    
    
    
    
    
    # part 1
    vis_test, sum1_test = get_visible_trees(test_forest)
    vis, sum1 = get_visible_trees(forest)
    
    print("Test 1 = ", sum1_test,'==',21)
    print("Solution 1 = ",sum1,"CORRECT")
    
    
    # part 2
    scene_test = evaluate_scenic_score(test_forest)
    scene = evaluate_scenic_score(forest)
    
    print("Test 1 = ",scene_test.max(),'==',8)
    print("Solution 2 = ",scene.max(),"CORRECT")

if __name__ == "__main__":
    main()
