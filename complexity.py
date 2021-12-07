# Math 55 Discrete Final Project
# Graph Complexity
# Eli Pregerson, William Yik and Georgia Klein

import numpy as np

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

def matrix_complexity(adj_list):
    adj_matrix = np.array(adj_list).reshape((len(adj_list), len(adj_list)))
    # recursion?

    return adj_matrix


def main():
    adj_list = [[0, 1, 0], [1, 0, 1], [0, 1, 1]]
    matrix_complexity(adj_list)

main()

