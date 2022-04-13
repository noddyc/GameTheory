import random
import math
"""
file: game_board.py
implementation for game_board
Author: Jian He
"""
# structure for game board
class Board:
    def __init__(self, board):
        self.board = board

    def count_chess(self):
        O_num = 0
        X_num = 0
        for i in self.board:
            for j in i:
                if j == "O":
                    O_num +=1
                if j == "X":
                    X_num +=1
        return [O_num, X_num]

# check if a game is in won status
    def is_win(self):
        chess_count = self.count_chess()
        if chess_count[1] == 0 and chess_count[0] > 0:
            return [True, "O"]
        if chess_count[0] == 0 and chess_count[1] > 0:
            return [True, "X"]
        return [False, "E"]

# check if a game is going to win within next move
    def goingTo_Win(self, player):
        chess_count = self.count_chess()
        if chess_count[1] == 1:
            if player == "White":
                temp = self.get_successor("White")
                for i in temp:
                    if Board(i).is_win():
                        return [True, "O"]
        if chess_count[0] == 1:
            if player == "Black":
                temp = self.get_successor("White")
                for i in temp:
                    if Board(i).is_win():
                        return [True, "X"]
        return [False, "E"]

# check if a game is going to draw
    def goingTo_Draw(self):
        chess_count = self.count_chess()
        if (chess_count[0] == 2 and chess_count[1] == 2):
            return True
        else:
            return False

# calculation of evaluation 1
    def eval1(self):
        temp = self.count_chess()
        return temp[0]-temp[1]

    # calculation of evaluation 2
    def eval2(self):
        Oedge = 0
        Xedge = 0
        Ocenter = 0
        Xcenter = 0
        for row in range(0, len(self.board)):
            for item in range(0, len(self.board[row])):
                if row == 0 or row == len(self.board)-1 or item == 0 or item == len(self.board[row])-1:
                    if self.board[row][item] == "O":
                        Oedge +=1
                    if self.board[row][item] == "X":
                        Xedge +=1
                else:
                    if self.board[row][item] == "O":
                        Ocenter +=1
                    if self.board[row][item] == "X":
                        Xcenter +=1
        return round(0.7*(Ocenter)+0.3*(Oedge) - (0.7*(Xcenter)+0.3*(Xedge)),2)

# calculate all possible successor moves
    def get_successor(self, player):
        Successors = []
        eat1=[]
        eat2=[]
        simple_move_original=[]
        simple_move =[]
        different_directions = [[0,-1],[0,1],[-1,0],[1,0]]
        same_directions = [[0,-1],[0,1],[-1,0],[1,0],[-1,-1],[-1,1],[1,-1],[1,1]]
        if player == "White":
            for row in range(0, len(self.board)):
                for item in range(0, len(self.board[row])):
                    if self.board[row][item] == "O":
                        if row%2 == item%2:
                            for direction in same_directions:
                                x = row + direction[0]
                                y = item + direction[1]
                                if x in range(0, len(self.board)) and y in range(0, len(self.board[row])):
                                    if self.board[x][y] == "E":
                                        eat1_temp = self.eat1(row,item,direction,player)
                                        if eat1_temp !=[]:
                                            eat1.append(eat1_temp)
                                            Board_temp = [r[:] for r in self.board]
                                            Board_temp[row][item] = "E"
                                            Board_temp[x][y] = "O"
                                            for i in eat1_temp:
                                                Board_temp[i[0]][i[1]] = "E"
                                            Successors.append(Board_temp)
                                        eat2_temp = self.eat2(row,item,direction,player)
                                        if eat2_temp !=[]:
                                            eat2.append(eat2_temp)
                                            Board_temp = [r[:] for r in self.board]
                                            Board_temp[row][item] = "E"
                                            Board_temp[x][y] = "O"
                                            for i in eat2_temp:
                                                Board_temp[i[0]][i[1]] = "E"
                                            Successors.append(Board_temp)
                                        simple_move.append([x,y])
                                        simple_move_original.append([row, item])
                        else:
                            for direction in different_directions:
                                x = row + direction[0]
                                y = item + direction[1]
                                if x in range(0, len(self.board)) and y in range(0, len(self.board[row])):
                                    if self.board[x][y] == "E":
                                        eat1_temp = self.eat1(row,item,direction,player)
                                        if eat1_temp !=[]:
                                            eat1.append(eat1_temp)
                                            Board_temp = [r[:] for r in self.board]
                                            Board_temp[row][item] = "E"
                                            Board_temp[x][y] = "O"
                                            for i in eat1_temp:
                                                Board_temp[i[0]][i[1]] = "E"
                                            Successors.append(Board_temp)
                                        eat2_temp = self.eat2(row,item,direction,player)
                                        if eat2_temp !=[]:
                                            eat2.append(eat2_temp)
                                            Board_temp = [r[:] for r in self.board]
                                            Board_temp[row][item] = "E"
                                            Board_temp[x][y] = "O"
                                            for i in eat2_temp:
                                                Board_temp[i[0]][i[1]] = "E"
                                            Successors.append(Board_temp)
                                        simple_move.append([x,y])
                                        simple_move_original.append([row,item])
            if eat1 == [] and eat2 == []:
                for i in range(0, len(simple_move)):
                    Board_temp = [r[:] for r in self.board]
                    Board_temp[simple_move_original[i][0]][simple_move_original[i][1]] = "E"
                    Board_temp[simple_move[i][0]][simple_move[i][1]] = "O"
                    Successors.append(Board_temp)
        if player == "Black":
            for row in range(0, len(self.board)):
                for item in range(0, len(self.board[row])):
                    if self.board[row][item] == "X":
                        if row % 2 == item % 2:
                            for direction in same_directions:
                                x = row + direction[0]
                                y = item + direction[1]
                                if x in range(0, len(self.board)) and y in range(0, len(self.board[row])):
                                    if self.board[x][y] == "E":
                                        eat1_temp = self.eat1(row, item, direction, player)
                                        if eat1_temp != []:
                                            eat1.append(eat1_temp)
                                            Board_temp = [r[:] for r in self.board]
                                            Board_temp[row][item] = "E"
                                            Board_temp[x][y] = "X"
                                            for i in eat1_temp:
                                                Board_temp[i[0]][i[1]] = "E"
                                            Successors.append(Board_temp)
                                        eat2_temp = self.eat2(row, item, direction, player)
                                        if eat2_temp != []:
                                            eat2.append(eat2_temp)
                                            Board_temp = [r[:] for r in self.board]
                                            Board_temp[row][item] = "E"
                                            Board_temp[x][y] = "X"
                                            for i in eat2_temp:
                                                Board_temp[i[0]][i[1]] = "E"
                                            Successors.append(Board_temp)
                                        if eat1 == [] and eat2 == []:
                                            simple_move.append([x, y])
                                            simple_move_original.append([row, item])
                        else:
                            for direction in different_directions:
                                x = row + direction[0]
                                y = item + direction[1]
                                if x in range(0, len(self.board)) and y in range(0, len(self.board[row])):
                                    if self.board[x][y] == "E":
                                        eat1_temp = self.eat1(row, item, direction, player)
                                        if eat1_temp != []:
                                            eat1.append(eat1_temp)
                                            Board_temp = [r[:] for r in self.board]
                                            Board_temp[row][item] = "E"
                                            Board_temp[x][y] = "X"
                                            for i in eat1_temp:
                                                Board_temp[i[0]][i[1]] = "E"
                                            Successors.append(Board_temp)
                                        eat2_temp = self.eat2(row, item, direction, player)
                                        if eat2_temp != []:
                                            eat2.append(eat2_temp)
                                            Board_temp = [r[:] for r in self.board]
                                            Board_temp[row][item] = "E"
                                            Board_temp[x][y] = "X"
                                            for i in eat2_temp:
                                                Board_temp[i[0]][i[1]] = "E"
                                            Successors.append(Board_temp)
                                        if eat1 == [] and eat2 == []:
                                            simple_move.append([x, y])
                                            simple_move_original.append([row, item])
            if eat1 == [] and eat2 == []:
                for i in range(0, len(simple_move)):
                    Board_temp = [r[:] for r in self.board]
                    Board_temp[simple_move_original[i][0]][simple_move_original[i][1]] = "E"
                    Board_temp[simple_move[i][0]][simple_move[i][1]] = "X"
                    Successors.append(Board_temp)
        return Successors

# successors of retreat capture
    def eat1(self, row, item, direction, player):
        if player == "White":
            white_list = []
            succesor_list = []
            new_x = row + (-direction[0])
            new_y = item + (-direction[1])
            if new_x in range(0, len(self.board)) \
                    and new_y in range(0, len(self.board[row]))\
                    and self.board[new_x][new_y] == "X":
                count = 1
                while True:
                    taken_x = row + (-count * direction[0])
                    taken_y = item + (-count * direction[1])
                    if taken_x in range(0, len(self.board)) \
                            and taken_y in range(0, len(self.board[row])) \
                            and self.board[taken_x][taken_y] == "X":
                        white_list.append([taken_x, taken_y])
                        count += 1
                    else:
                        break
            return white_list
        if player == "Black":
            black_list = []
            new_x = row + (-direction[0])
            new_y = item + (-direction[1])
            if new_x in range(0, len(self.board)) \
                    and new_y in range(0, len(self.board[row]))\
                    and self.board[new_x][new_y] == "O":
                count = 1
                while True:
                    taken_x = row + (-count * direction[0])
                    taken_y = item + (-count * direction[1])
                    if taken_x in range(0, len(self.board)) \
                            and taken_y in range(0, len(self.board[row])) \
                            and self.board[taken_x][taken_y] == "O":
                        black_list.append([taken_x, taken_y])
                        count += 1
                    else:
                        break
            return black_list

# successors of approach capture
    def eat2(self, row, item, direction, player):
        if player == "White":
            white_list = []
            new_x = row + (2*direction[0])
            new_y = item + (2*direction[1])
            if new_x in range(0, len(self.board)) \
                    and new_y in range(0, len(self.board[row])) \
                    and self.board[new_x][new_y] == "X":
                count = 2
                while True:
                    taken_x = row + (count * direction[0])
                    taken_y = item + (count * direction[1])
                    if taken_x in range(0, len(self.board)) \
                            and taken_y in range(0, len(self.board[row])) \
                            and self.board[taken_x][taken_y] == "X":
                        white_list.append([taken_x, taken_y])
                        count += 1
                    else:
                        break
            return white_list
        if player == "Black":
            black_list = []
            new_x = row + (2*direction[0])
            new_y = item + (2*direction[1])
            if new_x in range(0, len(self.board)) \
                    and new_y in range(0, len(self.board[row])) \
                    and self.board[new_x][new_y] == "O":
                count = 2
                while True:
                    taken_x = row + (count * direction[0])
                    taken_y = item + (count * direction[1])
                    if taken_x in range(0, len(self.board)) \
                            and taken_y in range(0, len(self.board[row])) \
                            and self.board[taken_x][taken_y] == "O":
                        black_list.append([taken_x, taken_y])
                        count += 1
                    else:
                        break
            return black_list

# random solver
def random_solver(Board, player):
    Results = Board.get_successor(player)
    Random_pick = random.choice(range(0,len(Results)))
    return Results[Random_pick]

# minimax solver with depth
def minimax_solver(state, depth, player):
    if depth == 0 or state.is_win()[0] == True:
        return state.eval1()
    if player == "White":
        maxEval = -math.inf
        succesors = state.get_successor("White")
        for i in succesors:
            b = Board(i)
            eval = minimax_solver(b, depth-1, "Black")
            maxEval = max(maxEval, eval)
        return maxEval
    else:
        minEval = math.inf
        succesors = state.get_successor("Black")
        for i in succesors:
            b = Board(i)
            eval = minimax_solver(b, depth-1, "White")
            minEval = min(minEval, eval)
        return minEval

# alpha beta solver without depth
def alpha_beta_solver_nodepth(state,alpha,beta, player):
    if state.is_win()[0]==True:
        return state.eval1()
    if player == "White":
        maxEval = -math.inf
        succesors = state.get_successor("White")
        for i in succesors:
            b = Board(i)
            eval = alpha_beta_solver_eval1(b, alpha, beta, "Black")
            maxEval = max(maxEval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return maxEval
    else:
        minEval = math.inf
        succesors = state.get_successor("Black")
        for i in succesors:
            b = Board(i)
            eval = alpha_beta_solver_eval1(b, alpha, beta,"White")
            minEval = min(minEval, eval)
            beta = min(beta,eval)
            if beta <= alpha:
                break
        return minEval

# alpha beta solver with depth using evaluation 1
def alpha_beta_solver_eval1(state, depth, alpha,beta, player):
    if depth == 0 or state.is_win()[0]==True:
        return state.eval1()
    if player == "White":
        maxEval = -math.inf
        succesors = state.get_successor("White")
        for i in succesors:
            b = Board(i)
            eval = alpha_beta_solver_eval1(b, depth-1, alpha, beta, "Black")
            maxEval = max(maxEval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return maxEval
    else:
        minEval = math.inf
        succesors = state.get_successor("Black")
        for i in succesors:
            b = Board(i)
            eval = alpha_beta_solver_eval1(b, depth-1, alpha, beta,"White")
            minEval = min(minEval, eval)
            beta = min(beta,eval)
            if beta <= alpha:
                break
        return minEval

# alpha beta solver with depth using evaluation 2
def alpha_beta_solver_eval2(state,depth, alpha,beta, player):
    if depth == 0 or state.is_win()[0]==True:
        return state.eval2()
    if player == "White":
        maxEval = -math.inf
        succesors = state.get_successor("White")
        for i in succesors:
            b = Board(i)
            eval = alpha_beta_solver_eval2(b, depth-1, alpha, beta, "Black")
            maxEval = max(maxEval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return maxEval
    else:
        minEval = math.inf
        succesors = state.get_successor("Black")
        for i in succesors:
            b = Board(i)
            eval = alpha_beta_solver_eval2(b, depth-1, alpha, beta,"White")
            minEval = min(minEval, eval)
            beta = min(beta,eval)
            if beta <= alpha:
                break
        return minEval


