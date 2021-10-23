
#Homework 3
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
    multiplication of the input matrix and scalar. Achieves this by using a for
    loop and the function scalar_vector_Multi to multiply each column in matrix_A
    to the input scalar and then overwrite the old column element with the newly
    calculated column elements for matrix_A.

    Args:
        matrix_A: A matrix stored as a list of lists.
        scalar_A: A scalar stored as a float number.

    Returns:
        The multiplication of the input matrix and scalar stored as a list of lists..
    """
    for column in range(len(matrix_A)):
        matrix_A[column] = scalar_vector_Multi(matrix_A[column], scalar_A)

    return matrix_A

#Problem #3
def matrix_matrix_Add(matrix_A: list[list[float]], matrix_B: list[list[float]]) -> list[list[float]]:
    """Adds the two input matrices.

    Create two int variables max_number_A and max_number_B. Use a for loop
    for each max_number to calculate the number of elements in each matrix.
    Use a if-elif-else statement to check the dimensions and number of elements
    to see if the matrices can be added. Then we overwrite each element in matrix_A
    with the corresponding element of the sum of the input matrices. Achieves this
    by using a for loop and the function add_vectors.

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
            matrix_B[0])):  
        matrix_A = "Error: Length of rows are not the same"

    elif (max_number_A != max_number_B):
        matrix_A = "Error: Number of elements are not the same"  

    else:
        for column in range(len(matrix_A)):
            matrix_A[column] = add_vectors(matrix_A[column], matrix_B[column]

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

    if (len(matrix_A) != len(vector_A)):  
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
                                           
                                           
# Homework 4
"""
This assignment is due by 11:59pm on 10/22/2021. 

For this assignment you will be adding functinos to the LA.py script from HW03.
All functions must satisfy the same requirements as in HW03. The functions you
will need to add are

#1) A function which takes a scalar as it's input and returns it's absolute
value. Note that this function must be able to take both real numbers and
complex numbers as input!!!

#2) A function which takes the as it's arguments

1) A vector stored as a list.

2) A float valued scalar, set to default as 2. 

and returns the p-norm of the input vector. Which p-norm must be determined using
the float valued scalar input. If no argument is given, it should default to
2. 

#3) A function which takes as it's argument a vector stored as a list and
returns the infinity norm of the input vector.

#4) A function which takes as it's arguments

1) A vector stored as a list.

2) An float valued scalar, set to default as 2.

3) A boolean value, set to default as False.

The function will return the p-norm of the input vector. If the boolean value is
given as True, the function will return the infinity norm of the input vector.
Otherwise it will return the p-norm of the vector corresponding to the float 
scalar argument. This function must use the functions from problem #2 and
problem #3 to earn credit. 

#5) A function which takes as it's arguments two vectors, stored as lists. This
function then returns the inner product of these vectors. Your function must be
able to handle complex numbers!
"""


# Problem #1
def abs(scalar_A: complex) -> float:
    """Find Absolute Value

        Create a result variable that is a float type. It will then convert our input scalar
        to a complex form. It will then take the real and the imaginary part of our scalar
        and square both then add them together. It will then store the value we just got into
        result then it will square root the result to get our absolute value. It then will
        return our result.

        Args:
            scalar_A: Is a scalar that is either normal or complex.

        Returns:
            The absolute value of our input value scalar_A.

        """
    result: float = 0
    scalar_A = complex(scalar_A)
    result = scalar_A.real ** 2 + scalar_A.imag ** 2
    result = result ** (1 / 2)

    return result


# Problem #2
def p_Norm(vector_A: list[float], p: int = 2) -> float:
    """Calculates the P-Norm

        Creates a result variable that is float type that is equal to zero. It will then
        take each element in our input vector and then raise it to the power of the absolute
        value of our input p. It finds the absolute value of p by calling the function abs()
        with p being the scalar for abs(). We will then add our element to the power of abs(p)
        with our result variable and then overwrite the result variable with the new calculation.
        It will continue to do this until it gets every element in our input vector. It achieves
        this by using a for loop which grabs each element in our input vector. It will then create
        a power variable which is a float type. The power variable will store the value we get
        from calling our abs() function from Problem #1 with p being the scalar for the abs()
        function. It will then overwrite result with the present result to the power of our power
        variable. It will then return result.

        Args:
            vector_A: A vector stored as a list of floats.
            p: A scalar stored as a int type with the default value of 2.

        Returns:
            The P-Norm of our input vector and input scalar.

        """
    result: float = 0
    for element in vector_A:
        result = result + element ** (abs(p))
    power: float = abs(1 / p)
    result = result ** (power)
    return result


# Problem #3
def inf_Norm(vector_A: list[float]) -> float:
    """Calculates the Infinity Norm

        Create two variables result and compare that both will be float types. It will then
        use a for loop to call each element in the input vector. It will then find the absolute
        value of each element from the input vector it will find the absolute value by send each
        element into the abs() function that we have created and store it into the compare variable.
        It will then use a if statement to see if compare is greater the result. If compare is greater
        then result it will then store the data in the compare variable to the result variable. If
        compare is less then result then result stays the same. It will run the for loop and if statements
        based of the number of elements in the input vector.

        Args:
            vector_A: A vector stored as a list of floats

        Returns:
            The infinity norm of our input vector

        """
    result: float = 0
    compare: float = 0
    for element in vector_A:
        compare = abs(element)
        if (compare > result):
            result = compare
    return result


# Problem #4
def p_inf_result(vector_A: list[float], p: int = 2, boolean: bool = False) -> float:
    """Finds the P-Norm or Infinity Norm

        Creates a result variable that is a float type. Then checks to see if our input
        boolean is True. If it is true then result will then be override with the
        infinity norm of our input vector by calling the inf_Norm() function. If the
        boolean variable is False then result will be override with P-norm of our
        vector input variable and p input variable. This is done by calling the
        p-Norm function. It will then return the result.

        Args:
            vector_A: A vector stored as a list of floats
            p: A scalar that is 2 by default.
            boolean: A boolean statement that is false by default.

        Returns:
            The multiplication of the input matrices stored as a list of lists.

        """
    result: float = 0
    if (boolean == True):
        result = inf_Norm(vector_A)
    else:
        result = p_Norm(vector_A, p)
    return result

# Problem 5
def inner_product_Result(vector_A, vector_B) -> complex:
    """Calculates the Inner Product of two vectors

        Creates a result variable that is a float type. Then runs a for loop that runs for
        the length of vector_A input. Each time the for loop is ran result will be override
        with result plus the multiplication of the elements in the two input vectors. We will
        make sure each element that is called from the input vectors are complex. After the for
        loop is over the result is returned.

        Args:
            vector_A: A vector stored as a list of complex and\or normal numbers.
            vector_B: A vector stored as a list of complex and\or normal numbers.

        Returns:
            The inner product of our two input vectors.

        """
    result: float = 0
    for element in range(len(vector_A)):
        result = result + (complex(vector_A[element]) * complex(vector_B[element]))
    return result
          
