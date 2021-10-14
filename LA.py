

"""
This homework is due on 10/15/2021 by 11:59pm. 


For this assignment you will be writing a python script to be named LA.py. In
this script you will need to write 6 functions. Every function must 

1) Have a doc string.

2) Have type annotations

3) Be tested using unit testing. 

Once you have finished writing LA.py you will upload it to the same github repo
you used for HW02. The functions you need to write are 

#0 A function which takes as it's arguments two vectors stored as
lists and returns their sum, also stored as a list.


#1 A function which takes as it's arguments a vector stored as a list and a
scalar, and returns the scalar vector multiplication stored as a list.


#2 A function which takes as it's arguments a matrix, stored as a list of lists
where each component list represents a column of the matrix(you cannot represent
the matrix as a list of rows!) and a scalar and returns their product, also
stored as a list of lists where each component list represents a column. You
must use the function from problem #1. Failure to use this function will result
in an earned grade of 0.

#3 A function which takes as it's arguments two matrices stored as lists of
lists where each component list represents a column vector, and returns their
sum stored in the same manner. You must use the function in problem #0 in your
method here. Failure to use the function from problem #0 will reuslt in an
earned grade of 0.

#4 A function which takes as it's argument a matrix (stored as a list of lists,
each component list representing a column vector), and a vector stored as a
list, and returns the matrix-vector product. This function must compute the
matrix-vector product by calculating the neccessary linear combination of the
input matrices columns. All other methods of matrix-vector multiplication are
strictly forbidden and their use will result in a grade of 0. For this function
you must use the functions written for problem #0 and problem #1. Failure to use
these functions will result in an earned grade of 0.

#5 A function which takes as it's arguments two matrices, each stored as a list
of lists where each component list represents a column vector, and returns their
product stored in the same manner. To earn any credit on this problem you must
use the function from problem #4 to implement the matrix-vector method of
matrix-matrix multiplication. Use of any other method will result in an earned
grade of 0.
"""


# Begin Example
# Problem #0

def add_vectors(vector_a: list[float],
                vector_b: list[float]) -> list[float]:
    """Adds the two input vectors.

    Creates a result vector stored as a list of 0's the same length as the input 
    then overwrites each element of the result vector with the corresponding
    element of the sum of the input vectors. Achieves this using a for loop over
    the indices of result. 

    Args:
        vector_a: A vector stored as a list.
        vector_b: A vector, the same length as vector_a, stored as a list.

    Returns:
       The sum of the input vectors stored as a list. 
    """ 
    result: list[float] = [0 for element in vector_a]
    for index in range(len(result)):
        result[index] = vector_a[index] + vector_b[index]
    return result

# End Example
# Note that you must add unit tests for problem 0!!!!!


# Problem #1
def scalar_vector_Multi(vector_A: list[float], scalar_A: float) -> list[float]:
    """Multiplies the input vector and scalar together.

    Creates a result vector stored as a list of 0's the same length as the
    input vector then overwrites each element of the result vector with the
    corresponding element of the multiplication of the input scalar and vector.
    Achieves this by using a for loop over the indices of result.
    Args:
        vector_A: A vector stored as a list.
        scalar_A: A scalar stored as a float number.
    Returns:
        The multiplication of the input vector and scalar stored as a list.
    """

    result: list[float] = []

    for i in range(len(vector_A)):
        result[i] = result.append(0)

    for i in range(len(vector_A)):
        result[i] = vector_A[i] * scalar_A

    return result


#Problem #2
def scalar_matrix_Multi(matrix_A: list[list[float]], scalar_A: float) -> list[list[float]]:
    """Multiplies the input matrix and scalar together.

    Overwrite each element in matrix_A with the corresponding element of the
    multiplication of the input matrix and scalar. Achieves this by using two for
    loops and calling the function scalar_vector_Multi inside the last loop and then
    putting the result into matrix_A.

    Args:
        matrix_A: A matrix stored as a list of lists.
        scalar_A: A scalar stored as a float number.

    Returns:
        The multiplication of the input matrix and scalar stored as a list of lists..
    """
    for column in range(len(matrix_A)):
        for row in range(len(matrix_A[0])):
            matrix_A[column][row] = (matrix_A[column][row] * scalar_A)

    return matrix_A

#Problem #3
def matrix_matrix_Add(matrix_A: list[list[float]], matrix_B: list[list[float]]) -> list[list[float]]:
    """Adds the two input matrices.

    Create two int variables max_number_A and max_number_B. Use a for loop
    for each max_number to calculate the number of elements in each matrix.
    Use a if-elif-else statement to check the dimensions and number of elements
    to see if the matrices can be added. Then we overwrite each element in matrix_A
    with the corresponding element of the sum of the input matrices. Achieves this
    by using two for loops over the indices of matrix_A.

    Args:
        matrix_A: A matrix stored as a list of lists.
        matrix_B: A matrix, the same size as matrix_A, stored as a list of lists.

    Returns:
        The sum of the input matrices stored as a list of lists.
    """
    max_number_A: int = 0
    max_number_B: int = 0

    for index in range(len(matrix_A)):
        max_number_A = max_number_A + len(matrix_A[index])
    for index in range(len(matrix_B)):
        max_number_B = max_number_B + len(matrix_B[index])

    if (len(matrix_A) != len(matrix_B)):
        matrix_A = "Error: Length of columns are not the same"

    elif (len(matrix_A[0]) != len(
            matrix_B[0])):  # Added print statement for when rows of both matrices are not the same.
        matrix_A = "Error: Length of rows are not the same"

    elif (max_number_A != max_number_B):
        matrix_A = "Error: Number of elements are not the same"  # Changed print statement from print("Error: Number of rows are not the same").

    else:
        for column in range(len(matrix_A)):
            for row in range(len(matrix_A[0])):
                matrix_A[column][row] = (matrix_A[column][row] + matrix_B[column][row])

    return matrix_A

#Problem #4
def matrix_vector_Multi(matrix_A: list[list[float]], vector_A: list[float]) -> list[float]:
    """Multiplies the input matrix and vector together.

    Creates a result matrix stored as a list of lists of 0's the same size as the
    input matrix. Creates a result vector stored as a list of 0's the same length
    as the input vector. Using a if statement to see if the columns of matrix_A
    are the same size as the rows in vector_A. Overwrite each column in matrix_A
    with the corresponding column of the multiplication of the matrix_A columns
    and vector_A elements. Achieves this by using a for loop and the function
    scalar_vector_Multi. Overwrite each column of result_matrix with the addition
    of result_matrix[i] and result_matrix[i+1] we achieved this by using a for loop
    and the function add_vectors. Overwrite result_vector with the last column in
    result_matrix.

    Args:
        matrix_A: A matrix stored as a list of lists.
        vector_A: A vector, the same column size as matrix_A, stored as a list.

    Returns:
        The multiplication of the input matrix and vector stored as a list.
    """
    result_Matrix: list[list[float]] = [([0] * (len(matrix_A[0]))) for i in range(len(matrix_A))]

    result_Vector: list[float] = []

    for index in range(len(vector_A)):
        result_Vector[index] = result_Vector.append(0)

    if (len(matrix_A) != len(vector_A)):  # Added a if statement to check if the columns from matrix_A are the same as the rows in vector_A.
        result_Vector = "Error: The dimensions are not compatible"

    else:
        for index in range(len(vector_A)):
            result_Matrix[index] = scalar_vector_Multi(matrix_A[index], vector_A[index])

        for index in range(len(result_Matrix) - 1):
            result_Matrix[index + 1] = add_vectors(result_Matrix[index], result_Matrix[(index + 1)])

        result_Vector = result_Matrix[len(result_Matrix) - 1]

    return result_Vector


#Problem #5
def matrix_matrix_Multi(matrix_A: list[list[float]], matrix_B: list[list[float]]) -> list[list[float]]:
    """Multiplies the input matrices together.

    Creates a result matrix stored as a list of list of 0's the same row length
    as the input matrix_A and the same column length as the input matrix_B. Uses
    if loop to see if the two input matrices are compatible. Overwrites each column
    in result_matrix with the corresponding column of the multiplication matrix_A
    and the columns in matrix_B. Achieves this by using a for loop and the function
    matrix_vector_Multi to overwrite the indices in result_matrix.

    Args:
        matrix_A: A matrix stored as a list of lists.
        matrix_B: A matrix, the same size as matrix_A, stored as a list of lists.

    Returns:
        The multiplication of the input matrices stored as a list of lists.

    """
    result_Matrix: list[list[float]] = [([0] * (len(matrix_A[0]))) for i in range(len(matrix_B))]

    if (len(matrix_A) != len(matrix_B[0])):
        result_Matrix = "Error: The dimensions are not compatible"

    else:
        for i in range(len(matrix_B)):
            result_Matrix[i] = matrix_vector_Multi(matrix_A, matrix_B[i])

    return result_Matrix