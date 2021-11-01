"""
This assignment is due by 11:59pm on 10/29/2021.

For this assignment you will be writing a python script named QR.py which will
contain several functions. All functions must satisfy the same requirements as in HW03.

You will import the LA.py script from HW03 and HW04. You must make use of those
functions to implement the functions below. Failure to do this will result in an
earned grade of 0.

For all functions below, matrices will be stored as lists of lists where each
component list represents a column of the matrix. Use of any other
representation will result in an earned grade of 0.

The functions you will need to add are

1) A function which implements the unstable version of Gram-Schmidt for reduced QR
factorization. It will
take as it's argument a matrix and will return a list of two matrices. The first
will be Q and the second will be R from the QR factorization described in the
algorithm.

2) A function which implements the stable version of Gram-Schmidt for reduced QR
factorization.It will take as it's argument a matrix and will return a list of
two matrices. The first will be Q and the second will be R from the QR factorization
described in the algorithm.

"""

import LA

#Problem 1
def unstable_Gram_Schmidt(matrix_A):
    Q = []
    V = [[0,0,0],[0,0,0]]
    R = [[0,0],[0,0]]
    r = 0
    scal = 0

    for column in range(len(matrix_A)):
        V[column] = matrix_A[column]
        for row in range(0, column):
            r = LA.inner_product_Result(Q[row], V[column])
            R[column][row] = r.real
            scal = LA.scalar_vector_Multi(Q[row], -R[column][row])
            V[column] = LA.add_vectors(V[column], scal)
        R[column][column] = LA.p_Norm((V[column]))
        Q.append(LA.scalar_vector_Multi((V[column]), (1 / R[column][column])))
    return [Q,R]
print("Problem 1")
print(unstable_Gram_Schmidt([[1,0,1],[2,1,0]]))

#Problem 2

def stable_Gram_Schmidt(matrix_A):
    Q = []
    V = []
    R = [[0, 0], [0, 0]]
    r = 0
    scal = 0
    for element in matrix_A:
        V.append(element)
    for column in range(len(matrix_A)):
        R[column][column] = LA.p_Norm((V[column]))
        Q.append(LA.scalar_vector_Multi((V[column]), (1 / R[column][column])))
        for row in range(column+1, len(matrix_A)):
            print(row)
            print(column)
            r = LA.inner_product_Result(Q[row], V[column])
            R[row][column] = r.real
            scal = LA.scalar_vector_Multi(Q[row], -R[column][row])
            V[column] = LA.add_vectors(V[column], scal)
    return [Q,R]

print("Problem 2")
print(stable_Gram_Schmidt([[1,0,1],[2,1,0]]))