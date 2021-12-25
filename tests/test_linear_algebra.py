import unittest
from linear_algebra.matrix import Matrix

A = Matrix(dims=(3, 3), fill=1.0)
B = Matrix(dims=(3, 3), fill=2.0)


class Testclass(unittest.TestCase):

    def test_matrix_A(self):
        T = [[-10.0, 1.0, 1.0], [1.0, 1.0, 1.0], [1.0, 1.0, 1.0]]
        self.assertEqual(A.A, T, "Left add (Matrix-Matrix)")

    def test_matrix_B(self):
        T = [[2.0, 2.0, 2.0], [2.0, 2.0, 2.0], [2.0, 2.0, 2.0]]
        self.assertEqual(B.A, T, "Left add (Matrix-Matrix)")

    def test_left_add_matrix_matrix(self):
        C = A + B
        T = [[-8.0, 3.0, 3.0], [3.0, 3.0, 3.0], [3.0, 3.0, 3.0]]
        self.assertEqual(C.A, T, "Left add (Matrix-Matrix)")

    def test_left_add_matrix_scalar(self):
        C = A + 10.0
        T = [[0.0, 11.0, 11.0], [11.0, 11.0, 11.0], [11.0, 11.0, 11.0]]
        self.assertEqual(C.A, T, "Left add (Matrix-Scalar)")

    def test_right_add(self):
        C = 20.0 + A
        T = [[10.0, 21.0, 21.0], [21.0, 21.0, 21.0], [21.0, 21.0, 21.0]]
        self.assertEqual(C.A, T, "Right add:")

    def test_04(self):
        C = A @ B
        T = [[6.0, 6.0, 6.0], [6.0, 6.0, 6.0], [6.0, 6.0, 6.0]]
        self.assertEqual(C.A, T, "Standard multiplication (Matrix-Matrix):")

    def test_05(self):
        C = A * B
        T = [[2.0, 2.0, 2.0], [2.0, 2.0, 2.0], [2.0, 2.0, 2.0]]
        self.assertEqual(C.A, T, "Right add:")

    def test_06(self):
        C = A * 0.5
        T = [[0.5, 0.5, 0.5], [0.5, 0.5, 0.5], [0.5, 0.5, 0.5]]
        self.assertEqual(C.A, T, "Right add:")

    def test_07(self):
        C = 0.5 * A
        T = [[0.5, 0.5, 0.5], [0.5, 0.5, 0.5], [0.5, 0.5, 0.5]]
        self.assertEqual(C.A, T, "Right add:")

    def test_08(self):
        C = A[0, 0]
        self.assertEqual(C, 1.0, "Right add:")

    def test_09(self):
        C = A
        C[0, 0] = -10.0
        self.assertEqual(C[0, 0], -10.0, "Right add:")


if __name__ == '__main__':
    unittest.main()
