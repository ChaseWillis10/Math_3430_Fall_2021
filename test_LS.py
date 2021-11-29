import LS
import pytest

def test_least_squares():
    matrix_A = [[3,4,0],[-6,-8,1]]
    vector_A = [-1,7,2]
    matrix_B = [[1,2,3],[4,5,6],[7,8,9]]
    vector_B = [1,2,3]
    assert LS.least_Squares(matrix_A, vector_A) == [(5+0j), (1.9999999999999991+0j)] #pytest.approx([(5+0j),(2+0j)], .001)
    assert LS.least_Squares(matrix_B, vector_B) == []
