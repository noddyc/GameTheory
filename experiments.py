from game_board import *
import math
"""
file: experiments.py
program for experiments implementations
Author: Jian He
"""

# structure use in experiment
class Node:
    def __init__(self, Board):
        self.Board = Board
        self.children = []
        self.eval1 = self.Board.eval1()
        self.eval2 = self.Board.eval2()


# function to form a tree for white player with depth 1
def tree_white_depth1(b1):
    node = Node(b1)
    for i in node.Board.get_successor("White"):
        temp = Node(Board(i))
        node.children.append(temp)
    return node


# function to form a tree for black player with depth 1
def tree_black_depth1(b1):
    node = Node(b1)
    for i in node.Board.get_successor("Black"):
        temp = Node(Board(i))
        node.children.append(temp)
    return node


# function to form a tree for white player with depth 3
def tree_white_depth3(b1):
    node = Node(b1)
    for i in node.Board.get_successor("White"):
        temp = Node(Board(i))
        node.children.append(temp)

    for j in node.children:
        temp = j.Board.get_successor("Black")
        for k in temp:
            j.children.append(Node(Board(k)))

    for i in node.children:
        for j in i.children:
            temp = j.Board.get_successor("White")
            for z in temp:
                j.children.append(Node(Board(z)))
    return node



# function to form a tree for white player with depth 3
def tree_black_depth3(b1):
    node = Node(b1)
    for i in node.Board.get_successor("Black"):
        temp = Node(Board(i))
        node.children.append(temp)

    for j in node.children:
        temp = j.Board.get_successor("White")
        for k in temp:
            j.children.append(Node(Board(k)))

    for i in node.children:
        for j in i.children:
            temp = j.Board.get_successor("Black")
            for z in temp:
                j.children.append(Node(Board(z)))
    return node


# this is to find all the paths of the tree using in minimax and alpha-beta solver
def minimax_pathfinder_help(node,dest,eval):
    path = []
    finalPath = []
    if eval == 1:
        finalPath = minimax_pathfinder_eval1(node, dest, path, finalPath)
    else:
        finalPath = minimax_pathfinder_eval2(node, dest, path, finalPath)
    return finalPath

# this is to find all the paths of the tree
# using in minimax and alpha-beta solver matching with target evaluation 2
def minimax_pathfinder_eval2(node,dest,path,finalPath):
    visited_set = set()
    visited_set.add(node)
    path.append(node)
    if node.eval2 == dest:
        finalPath.append(path[:])
    else:
        for i in node.children:
            if i not in visited_set:
                minimax_pathfinder_eval2(i, dest, path, finalPath)
    path.pop()
    visited_set.remove(node)
    return finalPath


# this is to find all the paths of the tree
# using in minimax and alpha-beta solver matching with target evaluation 1
def minimax_pathfinder_eval1(node,dest,path,finalPath):
    visited_set = set()
    visited_set.add(node)
    path.append(node)
    if node.eval1 == dest:
        finalPath.append(path[:])
    else:
        for i in node.children:
            if i not in visited_set:
                minimax_pathfinder_eval1(i, dest, path, finalPath)
    path.pop()
    visited_set.remove(node)
    return finalPath


# this is the helper to find all the paths of the tree
# using in brute force solver
def bf_pathfinder_help(node):
    path = []
    finalPath = []
    finalPath = bf_pathfinder(node, path, finalPath)
    return finalPath

# this is to find all the paths of the tree
# using in brute force solver
def bf_pathfinder(node, path ,finalPath):
    visited_set = set()
    visited_set.add(node)
    path.append(node)
    if len(node.children) == 0:
        finalPath.append(path[:])
    else:
        for i in node.children:
            if i not in visited_set:
                bf_pathfinder(i, path, finalPath)
    path.pop()
    visited_set.remove(node)
    return finalPath


# this is to select all the paths of the tree
# using in brute force solver that has best evaluation 1
def select_pathEval1(lst, player):
    if player == "White":
        target_path = []
        target_num = -math.inf
        for i in lst:
            if i[-1].eval1 > target_num:
                target_num = i[-1].eval1
                target_path = i
        return target_path
    else:
        target_path = []
        target_num = math.inf
        for i in lst:
            if i[-1].eval1 < target_num:
                target_num = i[-1].eval2
                target_path = i
        return target_path


# this is to select all the paths of the tree
# using in brute force solver that has best evaluation 2
def select_pathEval2(lst, player):
    if player == "White":
        target_path = []
        target_num = -math.inf
        for i in lst:
            if i[-1].eval2 > target_num:
                target_num = i[-1].eval2
                target_path = i
        return target_path
    else:
        target_path = []
        target_num = math.inf
        for i in lst:
            if i[-1].eval2 < target_num:
                target_num = i[-1].eval2
                target_path = i
        return target_path


# this is to select all the paths of the tree
# using in brute force solver that has best evaluation 0
def select_pathEval0(lst):
    target_path = []
    target_num = math.inf
    for i in lst:
        if abs(i[-1].eval1-0) < abs(target_num):
            target_num = i[-1].eval1
            target_path = i
    return target_path

# experiment random vs brute force depth 3 with evaluation 1
def random_bf3Eval1(initial_board):
    game = Board(initial_board)
    player = "White"
    white_evaluation = 0
    black_evaluation = 0
    while True:
        if player == "White":
            new_board = random_solver(game, player)
            game = Board(new_board)
            white_evaluation += len(game.get_successor(player))
            if game.is_win()[0] == True and game.is_win()[1] == "O":
                print("White wins")
                print("number of white evaluation is {}".format(white_evaluation))
                print("number of black evaluation is {}".format(black_evaluation))
                break
            if game.goingTo_Win("Black")[0] == True and game.goingTo_Win("Black")[1] == "X":
                print("Black wins")
                print("number of white evaluation is {}".format(white_evaluation))
                print("number of black evaluation is {}".format(black_evaluation + 1))
                break
            if game.goingTo_Draw():
                print("Draw")
                print("number of white evaluation is {}".format(white_evaluation))
                print("number of black evaluation is {}".format(black_evaluation))
                break
            player = "Black"
            continue
        if player == "Black":
            node = tree_black_depth3(game)
            paths = bf_pathfinder_help(node)
            new_board = select_pathEval1(paths, "Black")[1].Board
            game = new_board
            black_evaluation += len(paths)
            if game.is_win()[0] == True and game.is_win()[1] == "":
                print("Black wins")
                print("number of white evaluation is {}".format(white_evaluation))
                print("number of black evaluation is {}".format(black_evaluation))
                break
            if game.goingTo_Win("White")[0] == True and game.goingTo_Win("White")[1] == "O":
                print("White wins")
                print("number of white evaluation is {}".format(white_evaluation+1))
                print("number of black evaluation is {}".format(black_evaluation))
                break
            if game.goingTo_Draw():
                print("Draw")
                print("number of white evaluation is {}".format(white_evaluation))
                print("number of black evaluation is {}".format(black_evaluation))
                break
            player = "White"
            continue

# experiment random vs brute force depth 3 with evaluation 2
def random_bf3Eval2(initial_board):
    game = Board(initial_board)
    player = "White"
    white_evaluation = 0
    black_evaluation = 0
    while True:
        if player == "White":
            new_board = random_solver(game, player)
            game = Board(new_board)
            white_evaluation += len(game.get_successor(player))
            if game.is_win()[0] == True and game.is_win()[1] == "O":
                print("White wins")
                print("number of white evaluation is {}".format(white_evaluation))
                print("number of black evaluation is {}".format(black_evaluation))
                break
            if game.goingTo_Win("Black")[0] == True and game.goingTo_Win("Black")[1] == "X":
                print("Black wins")
                print("number of white evaluation is {}".format(white_evaluation))
                print("number of black evaluation is {}".format(black_evaluation + 1))
                break
            if game.goingTo_Draw():
                print("Draw")
                print("number of white evaluation is {}".format(white_evaluation))
                print("number of black evaluation is {}".format(black_evaluation))
                break
            player = "Black"
            continue
        if player == "Black":
            node = tree_black_depth3(game)
            paths = bf_pathfinder_help(node)
            new_board = select_pathEval2(paths, "Black")[1].Board
            game = new_board
            black_evaluation += len(paths)
            if game.is_win()[0] == True and game.is_win()[1] == "":
                print("Black wins")
                print("number of white evaluation is {}".format(white_evaluation))
                print("number of black evaluation is {}".format(black_evaluation))
                break
            if game.goingTo_Win("White")[0] == True and game.goingTo_Win("White")[1] == "O":
                print("White wins")
                print("number of white evaluation is {}".format(white_evaluation+1))
                print("number of black evaluation is {}".format(black_evaluation))
                break
            if game.goingTo_Draw():
                print("Draw")
                print("number of white evaluation is {}".format(white_evaluation))
                print("number of black evaluation is {}".format(black_evaluation))
                break
            player = "White"
            continue


# experiment brute force depth 1 with evaluation 1 vs brute force depth 3 with evaluation 1
def bf1Eval1_bf3Eval1(initial_board):
    game = Board(initial_board)
    player = "White"
    white_evaluation = 0
    black_evaluation = 0
    while True:
        if player == "White":
            node = tree_white_depth1(game)
            paths = bf_pathfinder_help(node)
            new_board = select_pathEval1(paths, "White")[1].Board
            game = new_board
            white_evaluation += len(paths)
            if game.is_win()[0] == True and game.is_win()[1] == "O":
                print("White wins")
                print("number of white evaluation is {}".format(white_evaluation))
                print("number of black evaluation is {}".format(black_evaluation))
                break
            if game.goingTo_Win("Black")[0] == True and game.goingTo_Win("Black")[1] == "X":
                print("Black wins")
                print("number of white evaluation is {}".format(white_evaluation))
                print("number of black evaluation is {}".format(black_evaluation + 1))
                break
            if game.goingTo_Draw():
                print("Draw")
                print("number of white evaluation is {}".format(white_evaluation))
                print("number of black evaluation is {}".format(black_evaluation))
                break
            player = "Black"
            continue
        if player == "Black":
            node = tree_black_depth3(game)
            paths = bf_pathfinder_help(node)
            new_board = select_pathEval1(paths, "Black")[1].Board
            game = new_board
            black_evaluation += len(paths)
            if game.is_win()[0] == True and game.is_win()[1] == "":
                print("Black wins")
                print("number of white evaluation is {}".format(white_evaluation))
                print("number of black evaluation is {}".format(black_evaluation))
                break
            if game.goingTo_Win("White")[0] == True and game.goingTo_Win("White")[1] == "O":
                print("White wins")
                print("number of white evaluation is {}".format(white_evaluation + 1))
                print("number of black evaluation is {}".format(black_evaluation))
                break
            if game.goingTo_Draw():
                print("Draw")
                print("number of white evaluation is {}".format(white_evaluation))
                print("number of black evaluation is {}".format(black_evaluation))
                break
            player = "White"
            continue

# experiment brute force depth 3 with evaluation 1 vs brute force depth 3 with evaluation 2
def bf3Eval1_bf3Eval2(initial_board):
    game = Board(initial_board)
    player = "White"
    white_evaluation = 0
    black_evaluation = 0
    while True:
        if player == "White":
            node = tree_white_depth3(game)
            paths = bf_pathfinder_help(node)
            new_board = select_pathEval1(paths, "White")[1].Board
            game = new_board
            white_evaluation += len(paths)
            if game.is_win()[0] == True and game.is_win()[1] == "O":
                print("White wins")
                print("number of white evaluation is {}".format(white_evaluation))
                print("number of black evaluation is {}".format(black_evaluation))
                break
            if game.goingTo_Win("Black")[0] == True and game.goingTo_Win("Black")[1] == "X":
                print("Black wins")
                print("number of white evaluation is {}".format(white_evaluation))
                print("number of black evaluation is {}".format(black_evaluation + 1))
                break
            if game.goingTo_Draw():
                print("Draw")
                print("number of white evaluation is {}".format(white_evaluation))
                print("number of black evaluation is {}".format(black_evaluation))
                break
            player = "Black"
            continue
        if player == "Black":
            node = tree_black_depth3(game)
            paths = bf_pathfinder_help(node)
            new_board = select_pathEval2(paths, "Black")[1].Board
            game = new_board
            black_evaluation += len(paths)
            if game.is_win()[0] == True and game.is_win()[1] == "":
                print("Black wins")
                print("number of white evaluation is {}".format(white_evaluation))
                print("number of black evaluation is {}".format(black_evaluation))
                break
            if game.goingTo_Win("White")[0] == True and game.goingTo_Win("White")[1] == "O":
                print("White wins")
                print("number of white evaluation is {}".format(white_evaluation + 1))
                print("number of black evaluation is {}".format(black_evaluation))
                break
            if game.goingTo_Draw():
                print("Draw")
                print("number of white evaluation is {}".format(white_evaluation))
                print("number of black evaluation is {}".format(black_evaluation))
                break
            player = "White"
            continue


# experiment alpha solver with depth 3 with evaluation 1 vs  alpha solver with depth 3 with evaluation 2
def alpha3Eval1_alpha3Eval2(initial_board):
    game = Board(initial_board)
    player = "White"
    white_evaluation = 0
    black_evaluation = 0
    draw_counter = 0

    while True:
        if player == "White":
            alpha_beta = alpha_beta_solver_eval1(game, 3, -math.inf, math.inf, "White")
            node = tree_white_depth3(game)
            paths = minimax_pathfinder_help(node, alpha_beta,1)
            results = select_pathEval1(paths, "White")
            if len(results) > 1:
                new_board = results[1].Board
            else:
                draw_counter +=1
                if draw_counter < 7:
                    new_board = results[0].Board
                else:
                    print("Draw")
                    print("number of white evaluation is {}".format(white_evaluation))
                    print("number of black evaluation is {}".format(black_evaluation))
                    break
            game = new_board
            white_evaluation += len(paths)
            if game.is_win()[0] == True and game.is_win()[1] == "O":
                print("White wins")
                print("number of white evaluation is {}".format(white_evaluation))
                print("number of black evaluation is {}".format(black_evaluation + 1))
                break
            if game.goingTo_Win("Black")[0] == True and game.goingTo_Win("Black")[1] == "X":
                print("Black wins")
                print("number of white evaluation is {}".format(white_evaluation))
                print("number of black evaluation is {}".format(black_evaluation))
                break
            if game.goingTo_Draw():
                print("Draw")
                print("number of white evaluation is {}".format(white_evaluation))
                print("number of black evaluation is {}".format(black_evaluation))
                break
            player = "Black"
            continue
        if player == "Black":
            alpha_beta = alpha_beta_solver_eval2(game, 3, -math.inf, math.inf, "Black")
            node = tree_black_depth3(game)
            paths = minimax_pathfinder_help(node, alpha_beta, 2)
            results = select_pathEval2(paths, "Black")
            if len(results) > 1:
                new_board = results[1].Board
            else:
                draw_counter +=1
                if draw_counter < 7:
                    new_board = results[0].Board
                else:
                    print("Draw")
                    print("number of white evaluation is {}".format(white_evaluation))
                    print("number of black evaluation is {}".format(black_evaluation))
                    break
            game = new_board
            black_evaluation += len(paths)
            if game.is_win()[0] == True and game.is_win()[1] == "":
                print("Black wins")
                print("number of white evaluation is {}".format(white_evaluation))
                print("number of black evaluation is {}".format(black_evaluation))
                break
            if game.goingTo_Win("White")[0] == True and game.goingTo_Win("White")[1] == "O":
                print("White wins")
                print("number of white evaluation is {}".format(white_evaluation + 1))
                print("number of black evaluation is {}".format(black_evaluation))
                break
            if game.goingTo_Draw():
                print("Draw")
                print("number of white evaluation is {}".format(white_evaluation))
                print("number of black evaluation is {}".format(black_evaluation))
                break
            player = "White"
            continue

# experiment brute force with depth 3 with evaluation vs the same
def bf3eval0_33(initial_board):
    game = Board(initial_board)
    player = "White"
    white_evaluation = 0
    black_evaluation = 0
    while True:
        if player == "White":
            node = tree_white_depth3(game)
            paths = bf_pathfinder_help(node)
            new_board = select_pathEval0(paths)[1].Board
            game = new_board
            white_evaluation += len(paths)
            if game.is_win()[0] == True and game.is_win()[1] == "O":
                print("White wins")
                print("number of white evaluation is {}".format(white_evaluation))
                print("number of black evaluation is {}".format(black_evaluation))
                break
            if game.goingTo_Win("Black")[0] == True and game.goingTo_Win("Black")[1] == "X":
                print("Black wins")
                print("number of white evaluation is {}".format(white_evaluation))
                print("number of black evaluation is {}".format(black_evaluation + 1))
                break
            if game.goingTo_Draw():
                print("Draw")
                print("number of white evaluation is {}".format(white_evaluation))
                print("number of black evaluation is {}".format(black_evaluation))
                break
            player = "Black"
            continue
        if player == "Black":
            node = tree_black_depth3(game)
            paths = bf_pathfinder_help(node)
            new_board = select_pathEval0(paths)[1].Board
            game = new_board
            black_evaluation += len(paths)
            if game.is_win()[0] == True and game.is_win()[1] == "":
                print("Black wins")
                print("number of white evaluation is {}".format(white_evaluation))
                print("number of black evaluation is {}".format(black_evaluation))
                break
            if game.goingTo_Win("White")[0] == True and game.goingTo_Win("White")[1] == "O":
                print("White wins")
                print("number of white evaluation is {}".format(white_evaluation + 1))
                print("number of black evaluation is {}".format(black_evaluation))
                break
            if game.goingTo_Draw():
                print("Draw")
                print("number of white evaluation is {}".format(white_evaluation))
                print("number of black evaluation is {}".format(black_evaluation))
                break
            player = "White"
            continue


# extra experiment brute force with depth 1 with evluation 2
# vs brute force with depth 3 with evluation 2
def bf1Eval2_bf3Eval2(initial_board):
    game = Board(initial_board)
    player = "White"
    white_evaluation = 0
    black_evaluation = 0
    while True:
        if player == "White":
            node = tree_white_depth1(game)
            paths = bf_pathfinder_help(node)
            new_board = select_pathEval2(paths, "White")[1].Board
            game = new_board
            white_evaluation += len(paths)
            if game.is_win()[0] == True and game.is_win()[1] == "O":
                print("White wins")
                print("number of white evaluation is {}".format(white_evaluation))
                print("number of black evaluation is {}".format(black_evaluation))
                break
            if game.goingTo_Win("Black")[0] == True and game.goingTo_Win("Black")[1] == "X":
                print("Black wins")
                print("number of white evaluation is {}".format(white_evaluation))
                print("number of black evaluation is {}".format(black_evaluation + 1))
                break
            if game.goingTo_Draw():
                print("Draw")
                print("number of white evaluation is {}".format(white_evaluation))
                print("number of black evaluation is {}".format(black_evaluation))
                break
            player = "Black"
            continue
        if player == "Black":
            node = tree_black_depth3(game)
            paths = bf_pathfinder_help(node)
            new_board = select_pathEval2(paths, "Black")[1].Board
            game = new_board
            black_evaluation += len(paths)
            if game.is_win()[0] == True and game.is_win()[1] == "":
                print("Black wins")
                print("number of white evaluation is {}".format(white_evaluation))
                print("number of black evaluation is {}".format(black_evaluation))
                break
            if game.goingTo_Win("White")[0] == True and game.goingTo_Win("White")[1] == "O":
                print("White wins")
                print("number of white evaluation is {}".format(white_evaluation + 1))
                print("number of black evaluation is {}".format(black_evaluation))
                break
            if game.goingTo_Draw():
                print("Draw")
                print("number of white evaluation is {}".format(white_evaluation))
                print("number of black evaluation is {}".format(black_evaluation))
                break
            player = "White"
            continue