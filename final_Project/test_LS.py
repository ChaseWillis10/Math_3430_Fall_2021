import LS
import pytest

def test_least_squares():
    matrix_A = [[3,4,0],[-6,-8,1]]
    vector_A = [-1,7,2]
    matrix_B = [[5,-2,6,1],[2,4,5,3],[5,6,-3,-9]]
    vector_B = [3,4,5,1]
    assert LS.least_Squares(matrix_A, vector_A) == pytest.approx([(5+0j),(2+0j)])
    assert LS.least_Squares(matrix_B, vector_B) == pytest.approx([(0.161486449+0j),(0.844824548+0j),(0.159068918+0j)])
