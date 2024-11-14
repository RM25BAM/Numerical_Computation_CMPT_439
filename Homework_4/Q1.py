import numpy as np
def determinant(matrix_val):# function parameter matrix
    det = np.linalg.det(matrix_val) # take it matrix and calculate the determinant with the numpy library
    #  https://www.geeksforgeeks.org/how-to-calculate-the-determinant-of-a-matrix-using-numpy/ (link for determinant)
    return det # return the determinant
def cramer(matrix):  # function parameter matrix
    n_shape = matrix.shape[0] # represents number of rows in matrix  
    if matrix.shape[1] != n_shape + 1: # number of column to check if its correct if not equal then no constant
        return "Not valid. The last column should be the constants." # error
    coefficient_matrix = matrix[:, :-1] # 
    constants = matrix[:, -1] #
    det = determinant(coefficient_matrix) # function of determinant matrix
    if det == 0: # if zero
        return "The system is singular (no solution)." # the system is singular so no solution 
    answer = [] # the list to input the det/ matrix 
    for i in range(n_shape): # for each n_shape iterate to compute the solution
        matrix_copy = np.array(coefficient_matrix, copy=True) # make copy of the matrix
        matrix_copy[:, i] = constants #  get the constants
        det_copy = determinant(matrix_copy) # copy the determination 
        answer.append(det_copy / det) # cramer
        variable_names = ['x', 'y', 'z'][:n_shape] # x y z for the naming the values solution for x y z so its not float32 output
        solution_str = ', '.join([f"{var} = {val:.6f}" for var, val in zip(variable_names, answer)]) # format for the printing output
    return solution_str # return the solution
    