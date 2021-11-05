import QR

#Problem 1
def test_orthonormal_Conversion():
    matrix_A = [[1,2,3],[4,5,6]]
    matrix_B = [[10,27],[30,35]]
    assert QR.orthonormal_Conversion(matrix_A) == [[0.2672612419124244, 0.5345224838248488, 0.8017837257372732], [(0.8728715609439694+0j), (0.21821789023599208+0j), (-0.43643578047198506+0j)]]
    assert QR.orthonormal_Conversion(matrix_B) == [[0.34731435582359393, 0.9377487607237036], [(0.9377487607237038+0j), (-0.34731435582359366+0j)]]
#Problem 2
def test_stable_Gram_Schmidt():
    matrix_A = [[1,0,1],[2,1,0]]
    matrix_B = [[1, 2], [3, 4]]
    assert QR.stable_Gram_Schmidt(matrix_A) == [[[0.7071067811865475, 0.0, 0.7071067811865475], [(0.577350269189626+0j), (0.5773502691896258+0j), (-0.5773502691896257+0j)]], [[1.4142135623730951, 0], [(1.414213562373095+0j), (1.7320508075688772+0j)]]]
    assert QR.stable_Gram_Schmidt(matrix_B) == [[[0.4472135954999579, 0.8944271909999159], [(0.8944271909999162+0j), (-0.4472135954999574+0j)]], [[2.23606797749979, 0], [(4.919349550499537+0j), (0.8944271909999159+0j)]]]
