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
def unstable_Gram_Schmidt(matrix_A: list[list[complex]]) -> list[list[complex]]:
    """Finds the Q & R for QR Factorization

        Creates four variables, Q which is a blank list, V which is a matrix the size of matrix_A, R which is a square
        matrix using the number of columns from matrix_A, and lastly vector_Hold which is a blank list. After variables
        are created it will then run a for loop which will run based off the number of columns in matrix_A. Inside that
        for loop we overwrite V[column] with matrix_A[column] and then run another for loop. This inner for loop will run
        from range 0 to what loop the outer for loop is on. The inner for loop will store the inner product of Q and V
        using our function inner_product_Result from our LA.py file into R. It will then store the scalar vector
        multiplication of Q and -R using the scalar_vector_Multi function from LA.py into vector_Hold. Then V will be
        overwritten with the addition of V and vector_Hold using the add_vectors function from LA.py. After that the
        inner for loop will end and it will then go back to the outer for loop which will then overwrite R with the
        P Norm of V using the p_Norm function from LA.py. It will then store the scalar vector multiplication of V and
        1/R into Q. After the outer for loop ends it will then return Q and R.

        Args:
            matrix_A: A matrix stored as a list of list with complex and\or normal numbers.

        Returns:
            The Q & R for QR factorization

    """

    Q: list[float] = []
    V: list[list[float]] = [([0] * (len(matrix_A[0]))) for i in range(len(matrix_A))]
    R: list[list[float]] = [([0] * (len(matrix_A))) for i in range(len(matrix_A))]
    vector_Hold: list[float] = []

    for Outer_For in range(len(matrix_A)):
        V[Outer_For] = matrix_A[Outer_For]
        for Inner_For in range(0, Outer_For):
            R[Outer_For][Inner_For] = LA.inner_product_Result(Q[Inner_For], V[Outer_For])
            vector_Hold = LA.scalar_vector_Multi(Q[Inner_For], -R[Outer_For][Inner_For])
            V[Outer_For] = LA.add_vectors(V[Outer_For], vector_Hold)
        R[Outer_For][Outer_For] = LA.p_Norm((V[Outer_For]))
        Q.append(LA.scalar_vector_Multi((V[Outer_For]), (1 / R[Outer_For][Outer_For])))
    return [Q,R]

#Problem 2

def stable_Gram_Schmidt(matrix_A: list[list[complex]]) -> list[list[complex]]:
    """Finds the Q & R for QR Factorization

            Creates four variables, Q which is a blank list, V which is a blank list, R which is a square
            matrix using the number of columns from matrix_A, and lastly vector_Hold which is a blank list. After
            variables are created we will run a for loop which will put all the element in matrix_A into our V variable.
            After that it will then run a for loop which will run based off the number of columns in matrix_A. Inside
            that for loop it will overwrite R with the P Norm of V using the p_Norm function from LA.py. It will then
            store the scalar vector multiplication of V and 1/R into Q. After this another for loop will then run. This
            inner for loop will run from range of what loop the outer for loop is on plus one to the length of matrix_A.
            The inner for loop will store the inner product of Q and V using our function inner_product_Result from our
            LA.py file into R. It will then store the scalar vector multiplication of Q and -R using the
            scalar_vector_Multi function from LA.py into vector_Hold. Then V will be overwritten with the addition of V
            and vector_Hold using the add_vectors function from LA.py. After the outer for loop ends it will then return
            Q and R.

            Args:
                matrix_A: A matrix stored as a list of list with complex and\or normal numbers.

            Returns:
                The Q & R for QR factorization

        """

    Q: list[complex] = []
    V: list[complex] = []
    R: list[list[float]] = [([0] * (len(matrix_A))) for i in range(len(matrix_A))]
    vector_Hold: list[float] = []

    for element in matrix_A:
        V.append(element)
    for Outer_For in range(len(matrix_A)):
        R[Outer_For][Outer_For] = LA.p_Norm((V[Outer_For]))
        Q.append(LA.scalar_vector_Multi((V[Outer_For]), (1 / R[Outer_For][Outer_For])))
        for Inner_For in range(Outer_For+1, len(matrix_A)):
            R[Inner_For][Outer_For] = LA.inner_product_Result(Q[Outer_For], V[Inner_For])
            vector_Hold = LA.scalar_vector_Multi(Q[Outer_For], -R[Inner_For][Outer_For])
            V[Inner_For] = LA.add_vectors(V[Inner_For], vector_Hold)
    return [Q,R]
