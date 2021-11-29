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
def back_Sub(matrix_A: list[list[complex]], vector_B: list[complex]) -> list[complex]:
    """Calculates the back substitution of the input matrix and vector.
            First create a result variable that will be a empty list. Then result will be overwritten with the first
            solution in backsubstitution. Then we will create a for loop using a variable name current that will range
            from length of matrix_A - 2, -1, -1. Create a variable name temp and store vector_B[current} in the variable
            It will then start another for loop using a variable named index that will range from length fo result.
            Inside this for loop we will overwrite temp with temp - solution. Index for loop will end and it will then
            overwrite temp again with 1/ coefficient of the variable we are solving for. We will then append temp into
            result and then return result.
            Args:
                matrix_A: A matrix stored as a list of list with complex and\or normal numbers.
                vector_A: A vector stored as a list of complex and\or normal numbers.
            Returns:
                result: The least squares of the input variables stored as a list.
            """
    result: list = [vector_B[-1] * (1/(matrix_A[-1][-1]))]
    for current in range(len(matrix_A) - 2, -1, -1):
        temp: float = vector_B[current]
        for index in range(len(result)):
            temp -= matrix_A[len(matrix_A) - 1 - index][current] * result[index]
        temp *= 1/(matrix_A[current][current])
        result.append(temp)
    result = result[::-1]
    return result

#Problem 1
def least_Squares(matrix_A: list[list[complex]], vector_A: list[complex]) -> list[complex]:
    """Finds the Least Squares of our input matrix and vector
            First set the variable Q_R to be the Q and R of matrix_A. We get Q and R from teh stable_Gram_Schmidt
            function from QR.py. Then separate the Q and R by storing Q into variable Q and R into variable R. Then
            set variable con_trans_Q to store the conjugate transpose of Q using teh con_Transpose function from
            QR.py. Then create Multi variable which stores multiplication of con_trans_Q which is a matrix and
            vector_A. This is achieved by using the matrix_vector_Multi function from LA.py. Finally we will then
            create a result variable which will store the result of the back substitution of matrix_A and vector_A.
            We will get this result by using back_Sub function. It will then return the result.
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
    Multi: list[complex] = LA.matrix_vector_Multi(con_trans_Q,vector_A)
    result: list[complex] = back_Sub(R, Multi)
    return result
