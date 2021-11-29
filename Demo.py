import LA
import QR
import LS

"""
For your final project you will make a folder called "final_Project" in your
github repo. In this folder you will write 7 python scripts with the following
names.

LA.py
test_LA.py
QR.py
test_QR.py
LS.py
test_LS.py
Demo.py

For every function you write in your scripts they must

1) Use type annotations as discussed in class. 

2) Have a corresponidng doc string using the format discussed in class.

3) have a test in the corresponding pytest script. 

Note: In the work below, all matrices are stored as lists of lists, where each
component list represents a column of the matrix. You must use this
representation for matrices. Similarly, all vectors are stored as lists. 

Note: You are free to write additional functions in order to meet the
requirements specified below. 

In Demo.py you will not be writing any functions. Instead you will be
demonstrating the functionality of the library you've written. 

Begin by writin a print statement that introduces yourself and the library
you've written.

For each function in LA.py, QR.py, and LS.py 

1) Write a print statement which introduces the function and what it does. 

2) Write a print statement which introduces an example (I suggest reusing one of
your tests.) 

3) Write a print statement which prints the example. 

"""

#Final Project
print("Hello my name is Chase Willis and my major is in Mathematics. My library consist"
      " of three\n python files LA.py, QR.py and LS.py each going over different parts of"
      " linear algebra.\n")

print("LA.py contains 11 functions that perform basic linear algebra tasks.\n")

print("First function is add_vectors which adds two vectors together.")
print("Example, if a = [1,1,1] and b = [2,2,2], then add_vectors will return")
a = [1,1,1]
b = [2,2,2]
print(LA.add_vectors(a,b))
print("\n")

print("Second function is scalar_vector_Multi which calculates the product of a scalar and vector.")
print("Example, if a = [4,5,6] and b = 10, then scalar_vector_Multi will return")
a = [4,5,6]
b = 10
print(LA.scalar_vector_Multi(a,b))
print("\n")

print("Third function is scalar_matrix_Multi which calculates the product of a scalar and a matrix")
print("Example, if a = [[1,2],[3,4]] and b = 10, then scalar_matrix_Multi will return")
a = [[1,2],[3,4]]
b = 10
print(LA.scalar_matrix_Multi(a,b))
print("\n")

print("Fourth function is matrix_matrix_Add which adds two matrices together.")
print("Example, if a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] and b = [[1, 1, 1], [1, 1, 1], [1, 1, 1]], then \n"
      "matrix_matrix_Add will return")
a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
b = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
print(LA.matrix_matrix_Add(a,b))
print("\n")

print("Fifth function is matrix_vector_Multi which finds the product of a matrix and a vector.")
print("Example, if a = [[1, 2], [3, 4]] and b = [2, 2], then matrix_vector_Multi will return")
a = [[1, 2], [3, 4]]
b = [2, 2]
print(LA.matrix_vector_Multi(a,b))
print("\n")

print("Sixth function is matrix_matrix_Multi which finds the product of two matrices.")
print("Example, if a = [[1, 2], [3, 4]] and b = [[2, 2], [4, 4]], then matrix_matrix_Multi will return")
a = [[1, 2], [3, 4]]
b = [[2, 2], [4, 4]]
print(LA.matrix_matrix_Multi(a,b))
print("\n")

print("Seventh function is abs which finds the absolute value.")
print("Example, if a -2-2j, then abs will return")
a = -2-2j
print(LA.abs(a))
print("\n")

print("Eighth function is p_Norm which finds the p norm of a vector.")
print("Example, if a = [1,2,3] and b = 3, then p_Norm will return ")
a = [1,2,3]
b = 3
print(LA.p_Norm(a,b))
print("\n")

print("Ninth function is inf_Norm which finds the infinity norm of a vector.")
print("Example, if a = [1,-4,3,5,2], then inf_Norm will return")
a = [1,-4,3,5,2]
print(LA.inf_Norm(a))
print("\n")

print("Tenth function is p_inf_result which finds the p norm or infinity norm based off a given boolean.")
print("Example, if a = [1,2,5,4], b = 5, and c = True, then p_inf_result will return")
a = [1,2,5,4]
b = 5
c = True
print(LA.p_inf_result(a,b,c))
print("\n")

print("Eleventh function is inner_product_Result which calculates the inner product of two vectors. ")
print("Example, if a = [1,2,3] and b = [1j,1+2j,2+3j], then inner_product_Result will return.")
a = [1,2,3]
b = [1j,1+2j,2+3j]
print(LA.inner_product_Result(a,b))
print("\n")

print("QR.py contains 3 functions that perform QR calculations and orthonormal conversions.\n")

print("First function is stable_Gram_Schmidt which finds the QR matrices for a given matrix.")
print("Example, if a = [[1,0,1],[2,1,0]], then stable_Gram_Schmidt will return")
a =  [[1,0,1],[2,1,0]]
print(QR.stable_Gram_Schmidt(a))
print("\n")

print("Second function is orthonormal_Conversion which will calculate the orthonormal of a given matrix.")
print("Example, if a = [[1,2,3],[4,5,6]], then orthonormal_Conversion will return")
a = [[1,2,3],[4,5,6]]
print(QR.orthonormal_Conversion(a))
print("\n")

print("Third function is householder_Ortho which will find QR of a given matrix by householder method.")
print("Example, if a = [[2,2,1],[-2,1,2],[1,3,1]], then householder_Ortho will return")
a = [[2,2,1],[-2,1,2],[1,3,1]]
print(QR.householder_Ortho(a))
print("\n")

print("LS.py contains 1 function that calculates Least Squares\n")

print("First function is least_Squares which will find the least squares of the given matrix and vector.")
print("Example, if a = [[3,4,0],[-6,-8,1]] and b = [-1,7,2], then least_Squares will return")
a = [[3,4,0],[-6,-8,1]]
b = [-1,7,2]
print(LS.least_Squares(a,b))
