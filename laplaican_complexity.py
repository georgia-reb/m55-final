# Math 55 Discrete Final Project
# Graph Complexity
# Eli Pregerson, William Yik and Georgia Klein

import numpy as np
import scipy as sp
import scipy.sparse
import scipy.linalg
import math
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.csgraph.laplacian.html

def is_connected(laplacian):
    laplacian_null_space = sp.linalg.null_space(laplacian)
    shape = np.shape(laplacian_null_space)
    # TODO test shape situtation more

    # Theorem: If the original matrix is connected, the null space of it's
    # laplacian matrix is 1-dimensional.
    return shape[1] == 1

def num_cuts(matrix, i, j): # expects a laplacian matrix 
    # Not currently working...
    if not is_connected(matrix):
        return 0
    # Failure, got to the upper triangular matrix and did not successfully
    # disconnect the graph.
    if i == len(matrix) - 2:
        print(matrix)
        return math.inf
    
    # leaveAlone is recursion with making no cuts
    if j < len(matrix) - 1: # If not at the end of the row, continue down the row
        leaveAlone = num_cuts(matrix, i, j + 1)
    else:
        # If at the end of the row, reset to the next row (keep in mind that we
        # are doing the upper triangular matrix).
        leaveAlone = num_cuts(matrix, i + 1, i + 2)
    
    # If there is a 0 at the current location, no cuts should be made
    if matrix[i][j] == 0:
        return leaveAlone
    else:
        # Cut the edge associated at the current value [i, j] in the matrix.
        matrix[i][j] = 0
        matrix[j][i] = 0
        matrix[i][i] = matrix[i][i] - 1
        matrix[j][j] = matrix[j][j] - 1
        # Recurse on the matrix with the current edge removed.
        cut = 1 + num_cuts(matrix, 0, 1)
        return min(leaveAlone, cut)

def matrix_complexity(adj_list):
    matrix = np.array(adj_list).reshape((len(adj_list), len(adj_list)))
    laplacian = sp.sparse.csgraph.laplacian(matrix)
    return num_cuts(laplacian, 0, 1)

def main():
    #adj_list = [[0, 1, 1], [1, 0, 1], [1, 1, 0]]
    adj_list = [[0, 1, 1, 1], [1, 0, 1, 1], [1, 1, 0, 1], [1, 1, 1, 0]]
    #adj_list = [[0, 1, 1, 1, 1], [1, 0, 1, 1, 1], [1, 1, 0, 1, 1], [1, 1, 1, 0, 1], [1, 1, 1, 1, 0]]
    print(matrix_complexity(adj_list))

main()
