#Homework 5 & 6
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

#Homework 7
"""
This assignment is due by 11:59pm on 11/12/2021. 
For this assignment you will be updating the python script QR.py from the
previous homework. As usual, all functions must satisfy the same requirements as in HW03. 
You will import the LA.py script from HW03 and HW04. You must make use of those
functions to implement the functions below. Failure to do this will result in an
earned grade of 0.
For all functions below, matrices will be stored as lists of lists where each
component list represents a column of the matrix. Use of any other
representation will result in an earned grade of 0.
1) Add a function which takes as it's argument a matrix and implements the
Householder Orthogonalization algorithm to calculate the QR
factorization, stored as a list of two matrices Q and R. 
"""

#Problem 1

def con_Transpose(matrix_A: list[list[complex]]) -> list[list[complex]]:
    """Finds the conjugate transpose of matrix_A
            We 
                matrix_A: A matrix stored as a list of list with complex and\or normal numbers.
            Returns:
                result: The conjugate transpose of matrix_A as a list of list with complex and\or normal numbers.
        """
    a: complex = 0
    result: list[list[float]] = [([0] * (len(matrix_A))) for i in range(len(matrix_A[0]))]
    for column in range(len(matrix_A)):
        for row in range(len(matrix_A[0])):
            a = matrix_A[column][row]
            a = a.real + (a.imag*-1j)
            result[row][column] = a
    return result

def matrix_Ident(matrix_A: list[list[complex]]) -> list[list[int]]:
    """Finds the matrix identity of matrix_A
            We 
                matrix_A: A matrix stored as a list of list with complex and\or normal numbers.
            Returns:
                result: The matrix identity stored as a list of list.
        """
    result: list[list[float]] = [([0] * (len(matrix_A))) for i in range(len(matrix_A[0]))]
    for element in range(len(matrix_A)):
        result[element][element] = 1
    return result

def dia_column(matrix_A: list[list[complex]], col_Num: int) -> list[complex]:
    """Finds the diagonal column of matrix_A
            We 
                matrix_A: A matrix stored as a list of list with complex and\or normal numbers.
                col_Num: a integer
            Returns:
                result: The diagonal column of matrix_A stored as a list of complex numbers.
        """
    result: list[float] = []
    for element in range((len(matrix_A[col_Num]))-col_Num):
        result[element] = result.append(0)
        result[element] = matrix_A[col_Num][element+col_Num]
    return result

def cal_V(e_vector: list[int], sub_X: list[complex]) -> list[complex]:
    """Finds the conjugate transpose of matrix_A
            We 
                matrix_A: A matrix stored as a list of list with complex and\or normal numbers.
            Returns:
                result: The conjugate transpose of matrix_A as a list of list with complex and\or normal numbers.
        """
    x_norm: complex = LA.p_Norm(sub_X)
    x_e_vector: list[float] = LA.scalar_vector_Multi(e_vector, x_norm)
    neg_sub_X: list[complex] = LA.scalar_vector_Multi(sub_X, -1)
    V = list[complex] = LA.add_vectors(x_e_vector, neg_sub_X)
    return [V]

def cal_F(V: list[complex]) -> list[list[complex]]:
    v_transpose: list[complex] = con_Transpose(V)
    v_Multi: list[list[complex]] = LA.matrix_matrix_Multi(V, v_transpose)
    Ident: list[list[int]] = matrix_Ident(v_Multi)
    v_Inner: complex = LA.inner_product_Result(V[0],V[0])
    scal_matrix: list[list[complex]] = LA.scalar_matrix_Multi(v_Multi, (2/v_Inner))
    neg_scal_matrix: list[list[complex]] = LA.scalar_matrix_Multi(scal_matrix, -1)
    F: list[list[complex]] = LA.matrix_matrix_Add(Ident, neg_scal_matrix)
    return F

def cal_Q(identity_matrix -> list[list[int]], F -> list[list[complex]], i -> int) -> list[list[complex]]:
    Q: list[list[float]] = [([0] * (len(identity_matrix))) for i in range(len(identity_matrix[0]))]
    for column in range(len(identity_matrix)):
        for row in range(len(identity_matrix[0])):
            Q[column][row] = identity_matrix[column][row]
    for column in range(len(Q) - i):
        for row in range(len(Q[0]) - i):
            Q[column + i][row + i] = F[column][row]
    return Q

def cal_final_Q(Q_List: list[list[list[complex]]], identity_matrix: list[list[int]], R: list[list[complex]]) -> list[list[complex]]:
    print(identity_matrix)
    Q: list[list[complex]] = identity_matrix
    Q[len(R)-1][len(R)-1] = R[len(R)-1][len(R)-1]
    Q_List.append(Q)
    print(Q_List)
    Q = Q_List[0]
    for index in range(len(Q_List) - 1):
        Q = LA.matrix_matrix_Multi(Q, Q_List[index + 1])
    Q = LA.matrix_matrix_Multi(Q, identity_matrix)
    return Q

def householder_Ortho(matrix_A: list[list[complex]]) -> list[list[complex]]:

    R: list[complex] = []
    Q_List: list[complex] = []
    identity_matrix : list[list[int]] = matrix_Ident(matrix_A)
    for element in matrix_A:
        R.append(element)
    for i in range(len(matrix_A)-1):
        identity_matrix = matrix_Ident(matrix_A)
        identity_column: list[int] = dia_column(identity_matrix, i)
        x: list[complex] = dia_column(R, i)
        V: list[complex] = cal_V(identity_column, x)
        F: list[list[complex]] = cal_F(V)
        Q: list[list[complex]] = cal_Q(identity_matrix, F, i)
        Q_List.append(Q)
        R = LA.matrix_matrix_Multi(Q,R)

    Q = cal_final_Q(Q_List, identity_matrix, R)
    return [Q,R]

print(householder_Ortho([[2,2,1],[-2,1,2],[1,3,1]]))
