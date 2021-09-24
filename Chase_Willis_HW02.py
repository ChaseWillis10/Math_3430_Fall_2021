"""
For this homework assignment we will take our work from HW01 and use it to
prepare a python script which will implement our algoirthms as python functions. 

For Problems #0-5 from HW01, Do the following.



1) Write your answer from HW01 in a comment.

2) Below the comment write a function which implements the algorithm from your
comment. If you find that you need to change your algorithm for your python
code, you must edit your answer in the comment. 

3) Test each of your functions on at least 2 inputs. 

4) Upload your .py file to a github repo named "Math_3430_Fall_2021"

This assignment is due by 11:59pm 09/27/2021. Do NOT upload an updated version to github
after that date. 
"""


#Example:

#Problem 00

"""
-The Three Questions

Q1: What do we have?

A1: Two vectors stored as lists. Denoted by the names vector_a and vector_b. 

Q2: What do we want?

A2: Their sum stored as a list.

Q3: How will we get there?

A3: We will create an empty list of the appropriate size and store the sums of
the corresponding components of vector_a and vector_b. 

-PsuedoCode

def add_vectors(vector_a,vector_b):

Initialize a result vector of 0's which is the same size as vector_a. Call this
vector result.

# Set each element of result to be equal to the desired sum.
for index in range(length(result)):
  result[index] = vector_a[index] + vector_b[index]

Return the desired result.
"""

def add_vectors(vector_a,vector_b):
  result = [0 for element in vector_a]
  for index in range(len(result)):
    result[index] = vector_a[index] + vector_b[index]
  return result

test_vector_01 = [1, 2, 4]
test_vector_02 = [3, 1, 2]

# add_vectors(test_vector_01,test_vector_02) should output [4,3,6]
print('Test Output for add_vectors: ' + str(add_vectors(test_vector_01,test_vector_02)))
print('Should have been [4,3,6]')


#End Example


#Problem 01
'''

-The Three Questions

Q1: What do we have?

A1: We have a scalar and a vector stored as a list and both are saved into the computer.

Q2: What do we want?

A2: We want a new vector that has been multiply by the scalar number.

Q3: How will we get there?

A3: We will have a vector called vector_A of any sized and a Scalar called scalar_A. We will then move
    through vector_A and multiply each instance by scalar_A. We will then store the new numbers inside our result
    vector that we initialize at the beginning of the code.

-Pseudocode

def scalar_vector_Multi(vector_A, scalar_A):

# Initializing result as an empty list
result = []

# Add an element to result for each element of vector_a. Set that element to 0.
for element in vector_A:
  append 0 to result

#Going through each number in our matrix and multiply the number by scalar_A.
for index in range(length(vector_A)):
	result[index] = vector_A[index] * scalar_A

#Return the result
return result
'''
def scalar_vector_Multi(vector_A, scalar_A):
  result = []

  for i in range(len(vector_A)):
    result[i] = result.append(0)

  for i in range(len(vector_A)):
    result[i] = vector_A[i] * scalar_A

  return result

#Test Inputs

print("\nTest Inputs for Problem 01")
vector_A = [1,2,3]
scalar_A = 2
print("1st Test Output for scalar_vector_Multi:", scalar_vector_Multi(vector_A,scalar_A))
print("1st Test Should be: [2, 4, 6]")
vector_B = [2,4,6,8]
scalar_B = 10
print("2nd Test Output for scalar_vector_Multi:", scalar_vector_Multi(vector_B,scalar_B))
print("2nd Test Should be: [20, 40, 60, 80]")

#Problem 02
'''
-The Three Questions

Q1: What do we have?

A1: We have a scalar and a matrix stored as a list of list and both are saved into the computer.

Q2: What do we want?

A2: We want a new matrix that has been multiply by the scalar number.

Q3: How will we get there?

A3: We will have a matrix called matrix_A of any sized and a Scalar called scalar_A. We will then move
    through matrix_A and multiply each number by scalar_A. We will override our matrix_A with our new 
    numbers that we calculated.

- Psuedocode

def scalar_matrix_Multi(vector_A, scalar_A):

#Going through each number in our matrix and multiply the number by scalar_A.
#Using to for loops to find the placement of each number so that we can multiply
#each number by our scalar. We will override matrix_A with our new calculations.
for column in range(length(matrix_A)):
	for row in range(length(matrix_A[0]))
		matrix_A[column][row] = (matrix_A[column][row] * scalar_A)

#Return the new matrix_A
return matrix_A
'''


def scalar_matrix_Multi(matrix_A, scalar_A):

  for column in range(len(matrix_A)):
    for row in range(len(matrix_A[0])):
      matrix_A[column][row] = (matrix_A[column][row] * scalar_A)

  return matrix_A

#Test Inputs

print("\nTest Inputs for Problem 02")
matrix_A = [[1,2],[3,4]]
scalar_C = 10
print("1st Test Output for scalar_matrix_Multi:", scalar_matrix_Multi(matrix_A,scalar_C))
print("1st Test Should be: [[10, 20], [30, 40]]")
matrix_B = [[1,2,2,1],[2,3,3,2],[3,4,4,3]]
scalar_D = 5
print("2nd Test Output for scalar_matrix_Multi:", scalar_matrix_Multi(matrix_B,scalar_D))
print("2nd Test Should be: [[5, 10, 10, 5], [10, 15, 15, 10], [15, 20, 20, 15]]")

#Problem 03
'''
- The Three Questions

Q1: What do we have?

A1: We have two matrices of the same dimensions and both are stored in our computer.

Q2: What do we want?

A2: We want a new matrix that is the addition of our two input matrices

Q3: How will we get there?

#Has been modified to check for number of rows and number of variables.
A3: We will first check to see if the dimensions of our matrices are the same by calculating the number of columns
    and how many variables we have in each matrices. We will then check to see if the number of columns are the same and
    if they are we will then check to see if number of rows and number of elements are the same. If they are not we will return 
    why they did not work and if they are we will then continue on with our function. If the dimension are the same we will 
    then go through our matrices and take the numbers that are in the same place in both matrices and add them together. We 
    will do this until we have done each number and then we will override our first matrix with the new matrix that we calculated.

-Pseudocode

def matrix_matrix_Add(matrix_A, matrix_B):
	
#Max number of elements in our input matrices.
max_number_A = 0
max_number_B = 0

#calculate the number of elements in each matrix.
for index in range(length(matrix_A)):
	max_number_A = max_number_A + length(matrix_A[index])
	max_number_B = max_number_B + length(matrix_B[index])

#If statement to see if the number of columns are the same in each matrix if they are not will return Error message.	
if(length(matrix_A) != length(matrix_B)):
	print("Error length of columns are not the same")

#This part has been added#
#Elif statement to see if the number of rows are the same if not error message will be returned.
elif(len(matrix_A[0]) != len(matrix_B[0])): #Added print statement for when rows of both matrices are not the same.
    print("Error: Length of rows are not the same")

#Has been Modified#
#Elif statement to see if the number of elements are the same in each matrix if they are not will return Error message.
elif(max_number_A != max_number_B)
	print("Error length of row are not the same")

#If the matrices are the same dimension then we will do the adding calculations. We do this by running two for loops
#to find the placement of each number for both matrices and add them together.
else:
	for column in range(length(matrix_A)):
		for row in range(length(matrix_A[0])):
			matrix_A[column][row] = (matrix_A[column][row] + matrix_B[column][row])

#Return the new matrix_A
return matrix_A
'''

def matrix_matrix_Add(matrix_A, matrix_B):

  max_number_A = 0
  max_number_B = 0

  for index in range(len(matrix_A)):
    max_number_A = max_number_A + len(matrix_A[index])
  for index in range(len(matrix_B)):
    max_number_B = max_number_B + len(matrix_B[index])

  if (len(matrix_A) != len(matrix_B)):
    matrix_A = "Error: Length of columns are not the same"

  elif(len(matrix_A[0]) != len(matrix_B[0])): #Added print statement for when rows of both matrices are not the same.
    matrix_A = "Error: Length of rows are not the same"

  elif (max_number_A != max_number_B):
    matrix_A = "Error: Number of elements are not the same" #Changed print statement from print("Error: Number of rows are not the same").

  else:
    for column in range(len(matrix_A)):
      for row in range(len(matrix_A[0])):
        matrix_A[column][row] = (matrix_A[column][row] + matrix_B[column][row])

  return matrix_A

#Test Inputs

print("\nTest Inputs for Problem 03")
matrix_C = [[1,2,3],[4,5,6]]
matrix_D = [[1,2],[3,4]]
print("1st Test Output for matrix_matrix_Add:", matrix_matrix_Add(matrix_C,matrix_D))
print("1st Test Should be: Error: Length of rows are not the same")
matrix_E = [[1,2,3],[4,5,6],[7,8,9]]
matrix_F = [[1,1,1],[1,1,1],[1,1,1]]
print("2nd Test Output for matrix_matrix_Add:", matrix_matrix_Add(matrix_E,matrix_F))
print("2nd Test Should be: [[2, 3, 4], [5, 6, 7], [8, 9, 10]]")

#Problem 04
'''
-The Three Questions

Q1: What do we have?

A1: We have a matrix and a vector stored in our computer.

Q2: What do we want?

A2: We want a vector which is the multiplication of the input matrix and vector.

Q3: How will we get there?

#Has been modified to check the dimension for matrix_A and vector_A are compatible.
A3: We will create a result_matrix which will have the same dimension of matrix_A. We will also have a result_vector
    which will have the same dimension have vector_A. We will check the dimension of matrix_A and vector_A to see if they are
    compatible. We will then send each column vector in matrix_A and each number in vector_A into our problem 1 algorithm 
    scalar_vector_Multi. We will return the new vectors into our result_matrix. We will then send the send the first column 
    vector in result_matrix and the next column vector into our problem 0 algorithm add_Vector to be added together. This
    will happen until each column vector is add together. We will then take the last column in our result matrix and send it 
    to result_Vector which will then be return. 

-Pseudocode

def matrix_vector_Multi(matrix_A,vector_A):

#Initailing result matrix which has the same dimension has matrix_A and fill it with zeros.
result_Matrix = [([0] * (length(matrix_A[0]))) for i in range(length(matrix_A))]

#intitalize result vector
result_Vector = []

#Fill result vector with zeros and the dimesnion will be the same has vector_A
for index in range(length(vector_A)):
	result_Vector[index] = result_Vector.append(0)

#Added#
#if statement to check if the dimension of matrix_A and vector_A work.
if(len(matrix_A) != len(vector_A)): 
  result_Vector = "Error: The dimensions are not compatible"
  
#Modified#
else:
  #We will use our problem 1 algorithm scalar_vector_Multi to calculate our new matrix.
  for index in range(length(vector_A)):
          result_Matrix[index] = scalar_vector_Multi(matrix_A[index],vector_A[index])

  #We will use our problem 0 algorithm add_Vector to add all of our column vectors in result_Matrix
  #to get our column vector that we want to return.
  for index in range(length(result_Matrix)-1):
          result_Matrix[index+1] = add_Vector(result_Matrix[index],result_Matrix[(index+1)])

  #We now grab the last column vector in our result_matrix and store it in result_Vector
  result_Vector = result_Matrix[length(result_Matrix)-1]

#Return result_Vector
return result_Vector
'''


def matrix_vector_Multi(matrix_A, vector_A):

  result_Matrix = [([0] * (len(matrix_A[0]))) for i in range(len(matrix_A))]

  result_Vector = []

  for index in range(len(vector_A)):
    result_Vector[index] = result_Vector.append(0)

  if(len(matrix_A) != len(vector_A)): #Added a if statement to check if the columns from matrix_A are the same as the rows in vector_A.
    result_Vector = "Error: The dimensions are not compatible"

  else:
    for index in range(len(vector_A)):
      result_Matrix[index] = scalar_vector_Multi(matrix_A[index], vector_A[index])

    for index in range(len(result_Matrix) - 1):
      result_Matrix[index + 1] = add_vectors(result_Matrix[index], result_Matrix[(index + 1)])

    result_Vector = result_Matrix[len(result_Matrix) - 1]

  return result_Vector

#Test Inputs

print("\nTest Inputs for Problem 04")
matrix_G = [[1,2],[3,4]]
vector_C = [2,2]
print("1st Test Output for matrix_vector_Multi:", matrix_vector_Multi(matrix_G,vector_C))
print("1st Test Should be: [8, 12]")
matrix_H = [[1,2,3],[4,5,6],[7,8,9]]
vector_D = [2,4]
print("2nd Test Output for matrix_vector_Multi:", matrix_vector_Multi(matrix_H,vector_D))
print("2nd Test Should be: Error: The dimensions are not compatible")

#Problem 05
'''
-The Three Questions

Q1: What do we have?

A1: We have two matrices that are stored in our computer matrix_A and matrix_B.

Q2: What do we want?

A2: We want a new matrix that is the multiplication of our two input matrices

Q3: How will we get there?

#Has been modified to check if the dimension of the two matrices are compatible.
A3: We will create a result matrix that has the dimension of the number of columns in matrix_B and the number of rows from matrix_A.
    We will then create a for loop that will take matrix_A and each column vector in matrix_B and send them to our problem 4 algorithm
    matrix_vector_Multi(matrix_A,vector_A) where matrix_A will be matrix_A and matrix_B[i] = vector_A. We will then store the vector that we
    get from our matrix_vector_Multi algorithm in the corresponding column vector in our result matrix. We will also check to see if
    the dimension of the two matrices are the same.


def matrix_matrix_Multi(matrix_A,matrix_B):

#Intializing a new matrix that will have the dimension we desire.
result_Matrix = [([0] * (len(matrix_A[0]))) for i in range(len(matrix_B))]

#ADDED#
#If statement to check to see if the dimensions of the two matrices are compatible.
if(len(matrix_A) != len(matrix_B[0])):
    result_Matrix = "The dimensions are not compatible."

#MODIFIED - else statement added#
#For loop that will go through each column vector in matrix_B which will then be sent into problem 4 algorithm along
#with the entirety of matrix_A. We will the store the return we get from matrix_vector_Multi in the column vector of our
#result matrix.
else:
  for i in range(len(matrix_B)):
	  result_matrix[i] = matrix_vector_Multi(matrix_A,matrix_B[i])

#Return our result_Matrix.
return result_Matrix
'''

def matrix_matrix_Multi(matrix_A, matrix_B):

  result_Matrix = [([0] * (len(matrix_A[0]))) for i in range(len(matrix_B))]

  if(len(matrix_A) != len(matrix_B[0])):
    result_Matrix = "The dimensions are not compatible."

  else:
    for i in range(len(matrix_B)):
      result_Matrix[i] = matrix_vector_Multi(matrix_A, matrix_B[i])

  return result_Matrix

#Test Inputs

print("\nTest Inputs for Problem 05")
matrix_I = [[1,2],[3,4]]
matrix_J = [[2,2],[4,4]]
print("1st Test Output for matrix_matrix_Multi:", matrix_matrix_Multi(matrix_I,matrix_J))
print("1st Test Should be: [[8, 12], [16, 24]")
matrix_K = [[1,2,3],[4,5,6]]
matrix_L = [[2,4,6],[3,5,7]]
print("2nd Test Output for matrix_matrix_Multi:", matrix_matrix_Multi(matrix_K,matrix_L))
print("2nd Test Should be: Error: The dimensions are not compatible")
