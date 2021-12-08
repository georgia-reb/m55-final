# Math 55 Discrete Final Project
# Graph Complexity
# Eli Pregerson, William Yik and Georgia Klein

import numpy as np
import scipy as sp
import scipy.sparse
import scipy.linalg
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.csgraph.laplacian.html

def is_connected(laplacian):
    laplacian_null_space = sp.linalg.null_space(laplacian)

    # Theorem: If the original matrix is connected, the null space of it's
    # laplacian matrix is 1-dimensional.
    return len(laplacian_null_space) == 1 and spanned_by_one

def num_cuts(matrix, i, j): # expects a laplacian matrix 
    # Not currently working...
    if not is_connected(matrix):
        return 0
    if j < len(matrix):
        leaveAlone = num_cuts(matrix, i, j + 1)
    else:
        leaveAlone = num_cuts(matrix, i + 1, i + 2)
    if matrix[i][j] == 0: # this was empty, is this supposed to be [i][j]?
        return leaveAlone
    else:
        matrix[i][j] = 0
        matrix[j][i] = 0
        matrix[i][i] = matrix[i][i] - 1
        cut = 1 + num_cuts(matrix, i, j)
        return min(leaveAlone, cut)

def matrix_complexity(adj_list):
    matrix = np.array(adj_list).reshape((len(adj_list), len(adj_list)))
    laplacian = sp.sparse.csgraph.laplacian(matrix)
    print(laplacian)
    return num_cuts(laplacian, 0, 1)

def main():
    adj_list = [[0, 1, 0], [1, 0, 1], [0, 1, 1]]
    print(matrix_complexity(adj_list))

main()