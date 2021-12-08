# Math 55 Discrete Final Project
# Graph Complexity
# Eli Pregerson, William Yik and Georgia Klein

import numpy as np
import scipy as sp
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.csgraph.laplacian.html

# Input: adjacency matrix 2D list
# Convert matrix to a numpy matrix
# Helper function to compute the matrix to the k
    # np.linalg.matrix_power(matrix, power)
# Decide if a graph is connected

def is_connected(array):
    matrix_sum = np.zeros((len(array), len(array)))

    # The (i,j)th entry in an adjacency matrix to the power n represents the
    # number of walks of length n between the i and j vertices.
    # Here we compute matrix_sum, which is the sum of the adjacency matrix to
    # the power of all values between 1 and n.

    # TODO: why do we only compute only the lengths between 1 and n? How do we
    # know there won't be more paths of length n + m?
    for i in range(1, len(array) + 1):
        power_matrix = np.linalg.matrix_power(array, i)
        matrix_sum += power_matrix
    
    # If any element in matrix_sum is 0, there are no walks of any length
    # between two elements, meaning that the graph is disconnected.
    for row in matrix_sum:
        for elem in row:
            if elem == 0:
                return False
    
    return True

def matrix_complexity(matrix, i, j): # i row j column
    if not is_connected(matrix):
        return 0
    if j < len(matrix):
        leaveAlone = matrix_complexity(matrix, i, j + 1)
    else:
        leaveAlone = matrix_complexity(matrix, i + 1, i + 2)
    if matrix[][] == 0:
        return leaveAlone
    else:
        matrix[i][j] = 0
        matrix[j][i] = 0
        matrix[i][i] = matrix[i][i] - 1
        cut = 1 + matrix_complexity(matrix, i, j)
        return min(leaveAlone, cut)


def main():
    adj_list = [[0, 1, 0], [1, 0, 1], [0, 1, 1]]
    matrix_complexity(adj_list)

main()

