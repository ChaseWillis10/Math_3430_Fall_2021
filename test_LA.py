import LA

#Problem 0
def test_add_vectors():
    vector_01 = [1, 1, 1]
    vector_02 = [2, 2, 2]
    vector_03 = [4, 2, 6]
    vector_04 = [2, 3, 4]
    assert LA.add_vectors(vector_01,vector_02) == [3,3,3]
    assert LA.add_vectors(vector_03,vector_04) == [6,5,10]

#Problem 1
def test_scalar_vector_Multi():
    vector_01 = [1, 2, 3]
    scalar_01 = 2
    vector_02 = [4, 5, 6]
    scalar_02 = 10
    assert LA.scalar_vector_Multi(vector_01,scalar_01) == [2,4,6]
    assert LA.scalar_vector_Multi(vector_02,scalar_02) == [40,50,60]

#Problem 2
def test_scalar_matrix_Multi():
    matrix_01 = [[1, 2], [3, 4]]
    scalar_01 = 10
    matrix_02 = [[1, 2, 2, 1], [2, 3, 3, 2], [3, 4, 4, 3]]
    scalar_02 = 5
    assert LA.scalar_matrix_Multi(matrix_01,scalar_01) == [[10, 20], [30, 40]]
    assert LA.scalar_matrix_Multi(matrix_02,scalar_02) == [[5, 10, 10, 5], [10, 15, 15, 10], [15, 20, 20, 15]]

#Problem 3
def test_matrix_matrix_Add():
    matrix_01 = [[1, 2, 3], [4, 5, 6]]
    matrix_02 = [[1, 2], [3, 4]]
    matrix_03 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    matrix_04 = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
    assert LA.matrix_matrix_Add(matrix_01,matrix_02) == "Error: Length of rows are not the same"
    assert LA.matrix_matrix_Add(matrix_03,matrix_04) == [[2, 3, 4], [5, 6, 7], [8, 9, 10]]

#Problem 4
def test_matrix_vector_Multi():
    matrix_01 = [[1, 2], [3, 4]]
    vector_01 = [2, 2]
    matrix_02 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    vector_02 = [2, 4]
    assert LA.matrix_vector_Multi(matrix_01,vector_01) == [8, 12]
    assert LA.matrix_vector_Multi(matrix_02,vector_02) == "Error: The dimensions are not compatible"

#Problem 5
def test_matrix_matrix_Multi():
    matrix_01 = [[1, 2], [3, 4]]
    matrix_02 = [[2, 2], [4, 4]]
    matrix_03 = [[1, 2, 3], [4, 5, 6]]
    matrix_04 = [[2, 4, 6], [3, 5, 7]]
    assert LA.matrix_matrix_Multi(matrix_01,matrix_02) == [[8, 12], [16, 24]]
    assert LA.matrix_matrix_Multi(matrix_03,matrix_04) == "Error: The dimensions are not compatible"

    
#Homework 4

#Problem 1
def test_abs():
    scalar_1 = -2-2j
    scalar_2 = -5
    assert LA.abs(scalar_1) == (8**(.5))
    assert LA.abs(scalar_2) == 5
    
#Problem 2
def test_p_Norm():
    vector_1 = [1,2,3]
    vector_2 = [2,4,6]
    p_1 = 3
    assert LA.p_Norm(vector_1, p_1) == (36**(1/3))
    assert LA.p_Norm(vector_2) == (56**(1/2))
    
#Problem 3
def test_inf_Norm():
    vector_1 = [1,-4,3,5,2]
    vector_2 = [-10, 2, 9]
    assert LA.inf_Norm(vector_1) == 5
    assert LA.inf_Norm(vector_2) == 10
    
#Problem 4
def test_p_inf_result():
    vector_1 = [1,2,5,4]
    vector_2 = [1,2,3]
    p_1 = 5
    boolean_1 = True
    assert LA.p_inf_result(vector_1, p_1, boolean_1) == 5
    assert LA.p_inf_result(vector_2) == (14**(.5))
    
#Problem 5
def test_inner_product_Result():
    vector_1 = [1,2,3]
    vector_2 = [1j,1+2j,2+3j]
    vector_3 = [2,4,6]
    vector_4 = [1,3,5]
    assert LA.inner_product_Result(vector_1,vector_2) == 8+14j
    assert LA.inner_product_Result(vector_3,vector_4) == 44
    
