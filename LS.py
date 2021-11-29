import LA
import QR

"""
This assignment is due by 11:59pm on 11/19/2021. 

For this assignment you will be writing a python script named LS.py which will
contain several functions. All functions must satisfy the same requirements as in HW03. 

You will import the LA.py and QR.py scripts from the previous homeworks. You must make use of those
functions to implement the functions below. Failure to do this will result in an
earned grade of 0.

For all functions below, matrices will be stored as lists of lists where each
component list represents a column of the matrix. Use of any other
representation will result in an earned grade of 0.

The functions you will need to write are

1) Write a function which takes as it's argument a vector stored as a list, and
a matrix, and returns the least squares solution, calculated by using QR
factorization.
"""

#Problem 1
def least_Squares(matrix_A: list[list[complex]], vector_A: list[complex]) -> list[complex]:
    """Finds the Least Squares of our input matrix and vector
            First set the variable Q_R to be the Q and R of matrix_A. We get Q and R from teh stable_Gram_Schmidt
            function from QR.py. Then seperate the Q and R by storing Q into variable Q and R into variable R. Then
            set variable con_trans_Q to store the conjugate transpose of Q using teh con_Transpose function from
            QR.py. Then create result variable which stores multiplication of con_trans_Q which is a matrix and
            vector_A. This is achieved by using the matrix_vector_Multi function from LA.py.

            Args:
                matrix_A: A matrix stored as a list of list with complex and\or normal numbers.
                vector_A: A vector stored as a list of complex and\or normal numbers.
            Returns:
                result: The least squares of the input variables stored as a list.
        """
    Q_R: list[list[list[complex]]] = QR.stable_Gram_Schmidt(matrix_A)
    Q: list[list[complex]] = Q_R[0]
    R: list[list[complex]] = Q_R[1]
    con_trans_Q: list[list[complex]] = QR.con_Transpose(Q)
    result: list[complex] = LA.matrix_vector_Multi(con_trans_Q,vector_A)
    return result
