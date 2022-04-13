from game_board import *
from experiments import *
import math
import random
"""
file: fanorona.py
main program for running the experiments
Author: Jian He
"""
def main():
    initial_board = [["X", "X", "X", "X", "X", "X", "X", "X", "X"],
                     ["X", "X", "X", "X", "X", "X", "X", "X", "X"],
                     ["X", "O", "X", "O", "E", "X", "O", "X", "O"],
                     ["O", "O", "O", "O", "O", "O", "O", "O", "O"],
                     ["O", "O", "O", "O", "O", "O", "O", "O", "O"]]

    small_board = [["X", "X", "X"],
                   ["X", "E", "O"],
                   ["O", "O", "O"]]

    print("Experiment Brute-force with large depth limit" +
          " and zero evaluation function vs the same, on the" +
          " 3*3 game is running")
    print("result: ")
    bf3eval0_33(small_board)
    print("---------")
    print("Experiment Random vs brute-force with limit of 3 with "
          "evaluation 1 (trial 1), on the 5*9 is running")
    print("result:")
    random_bf3Eval1(initial_board)
    print("---------")
    print("Experiment Random vs brute-force with limit of 3 with "
          "evaluation 1 (trial 2), on the 5*9 is running")
    print("result:")
    random_bf3Eval1(initial_board)
    print("---------")
    print("Experiment Random vs brute-force with limit of 3 with "
          "evaluation 1 (trial 3), on the 5*9 is running")
    print("result:")
    random_bf3Eval1(initial_board)
    print("---------")
    print("Experiment Random vs brute-force with limit of 3 with "
          "evaluation 2 (trial 1), on the 5*9 is running")
    print("result:")
    random_bf3Eval2(initial_board)
    print("---------")
    print("Experiment Random vs brute-force with limit of 3 with "
          "evaluation 2 (trial 2), on the 5*9 is running")
    print("result:")
    random_bf3Eval2(initial_board)
    print("---------")
    print("Experiment Random vs brute-force with limit of 3 with "
          "evaluation 2 (trial 3), on the 5*9 is running")
    print("result:")
    random_bf3Eval2(initial_board)
    print("---------")
    print("Experiment Brute force with limit 1"
          " vs brute-force with limit of 3 with "
          "evaluation 1, on the 5*9 is running")
    print("result:")
    bf1Eval1_bf3Eval1(initial_board)
    print("---------")
    print("Experiment Brute force with limit 3"
          " with evaluation 1 vs Brute force with limit 3"
          " with evaluation 2, on the 5*9 is running")
    bf3Eval1_bf3Eval2(initial_board)
    print("---------")
    print("Experiment Alpha-beta with limit of 3 with evaluation 1"
          "vs Alpha-beta with limit of 3 with evaluation 2, "
          "on the 5*9 is running")
    alpha3Eval1_alpha3Eval2(initial_board)
    print("---------")
    print("Extra Experiment Brute force with limit 1 with "
          "evaluation 2 vs brute-force with limit of 3 with "
          "evaluation 2, on the 5*9 is running")
    bf1Eval2_bf3Eval2(initial_board)
    print("---------")



if __name__ == '__main__':
    main()
