"""
This assignment is due by 11:59pm on 11/05/2021. 

For this assignment you will be updating the python script QR.py from the
previous homework. As usual, all functions must satisfy the same requirements as in HW03. 

You will import the LA.py script from HW03 and HW04. You must make use of those
functions to implement the functions below. Failure to do this will result in an
earned grade of 0.

1) Remove the function which implemented unstable Gram-Schmidt. It is unstable
and we may use the stable version exclusively from this point forward. 

2) Write a function which takes as it's argument a list of vectors and returns
an orthonormal list of vectors which shares the same span. 
"""

import LA

#Problem 1
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

#Problem 2
def orthonormal_Conversion(matrix_A: list[list[complex]]) -> list[list[complex]]:
    """Finds the Orthonormal List of Vectors of our Input Matrix

            We set Q equal to our stable_Gram_Schmidt function. The stable_Gram_Schmidt function already finds
            the orthonormal list of vectors for our input matrix which is Q and in additon R. We just need Q so for the
            return we only want the first column in Q which is Q[0] which holds the list that we want.

            Args:
                matrix_A: A matrix stored as a list of list with complex and\or normal numbers.

            Returns:
                Q: Which is the Orthonormal list of vectors of our input matrix

        """
    Q: list[list[complex]] = stable_Gram_Schmidt(matrix_A)
    return Q[0]
