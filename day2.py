# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 07:32:18 2022

@author: gwilding
"""

import os
import sys

import numpy as np
import matplotlib.pyplot as plt

def play(p1, p2):
    pass

def main():
    input_path = 'input_day2.txt'
    input_day2 = np.genfromtxt(input_path,str)
    
    test_input = [['A', 'Y'],
                  ['B', 'X'],
                  ['C', 'Z']]
    
    # convert character to number
    conv = {'A': 0, 'B': 1, 'C': 2,
            'X': 0, 'Y': 1, 'Z': 2 }
    
    # 0 = Rock
    # 1 = Paper
    # 2 = Scissor
    
    # convert game result to number
    conv2 = {'X': -1, 'Y': 0, 'Z': 1}
    
    # game result matrix: RPS <> RPS
    game_matrix = np.array([[ 0,-1, 1],
                            [ 1, 0,-1],
                            [-1, 1, 0]])
    # part 1
    round_results = []
    for play in input_day2:
        p1_wins = game_matrix[tuple([conv[p] for p in play])]
        round_results.append([conv[play[1]],p1_wins*-1])
    round_results = np.array(round_results)
    
    print("Day 2, part 1:")
    print(np.sum((round_results[:,1]+1)*3 + round_results[:,0]+1))

    # part 2
    round_results = []
    for play in input_day2:
        # need to play[1]
        opponent_plays = conv[play[0]]
        wanted_result = conv2[play[1]]
        I_play = np.where(game_matrix[:,opponent_plays] == wanted_result)[0][0]
        round_results.append([conv2[play[1]],I_play,opponent_plays])
        
    round_results = np.array(round_results)
    print("Day 2, part 2:")
    print(np.sum((round_results[:,0]+1)*3 + round_results[:,1]+1))
    
if __name__ == "__main__":
    main()
