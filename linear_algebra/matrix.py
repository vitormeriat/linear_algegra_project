class Matrix:

    def __init__(self, dims, fill):

        self.rows = dims[0]
        self.cols = dims[1]

        self.A = [[fill] * self.cols for i in range(self.rows)]

    def __str__(self):
        m = len(self.A)  # Get the first dimension
        return ''.join(
            (
                '|'
                + ', '.join(map(lambda x: '{0:8.3f}'.format(x), self.A[i]))
                + '| \n'
            )
            for i in range(m)
        )

    def __add__(self, other):

        # Create a new matrix
        C = Matrix(dims=(self.rows, self.cols), fill=0)

        # Check if the other object is of type Matrix
        if isinstance(other, Matrix):
            # Add the corresponding element of 1 matrices to another
            for i in range(self.rows):
                for j in range(self.cols):
                    C.A[i][j] = self.A[i][j] + other.A[i][j]

        # If the other object is a scaler
        elif isinstance(other, (int, float)):
            # Add that constant to every element of A
            for i in range(self.rows):
                for j in range(self.cols):
                    C.A[i][j] = self.A[i][j] + other

        return C

    # Right addition can be done by calling left addition
    def __radd__(self, other):
        return self.__add__(other)

    # Pointwise multiplication
    def __mul__(self, other):

        C = Matrix(dims=(self.rows, self.cols), fill=0)
        if isinstance(other, Matrix):

            for i in range(self.rows):
                for j in range(self.cols):
                    C.A[i][j] = self.A[i][j] * other.A[i][j]

        # Scaler multiplication
        elif isinstance(other, (int, float)):

            for i in range(self.rows):
                for j in range(self.cols):
                    C.A[i][j] = self.A[i][j] * other

        return C

    # Point-wise multiplication is also commutative
    def __rmul__(self, other):

        return self.__mul__(other)

    # Matrix-matrix multiplication
    def __matmul__(self, other):

        if isinstance(other, Matrix):
            C = Matrix(dims=(self.rows, self.cols), fill=0)

            # Multiply the elements in the same row of the first matrix
            # to the elements in the same col of the second matrix
            for i in range(self.rows):
                for j in range(self.cols):
                    acc = sum(self.A[i][k] * other.A[k][j]
                              for k in range(self.rows))

                    C.A[i][j] = acc

        return C

    def __getitem__(self, key):
        if isinstance(key, tuple):
            i = key[0]
            j = key[1]
            return self.A[i][j]

    def __setitem__(self, key, value):
        if isinstance(key, tuple):
            i = key[0]
            j = key[1]
            self.A[i][j] = value


if __name__ == '__main__':

    A = Matrix(dims=(3, 3), fill=1)
    B = Matrix(dims=(3, 3), fill=2)
    C = 2*A
    A[0, 1] = 2
    print(A[0, 1])
