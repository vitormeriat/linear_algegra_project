# How to Build a Matrix Module from Scratch

---

## Motivation

Numpy is a useful library that enables you to create a matrix and perform matrix operations with ease. But what if you want to create a matrix class with features that are not included in the Numpy library? To be able to do that, we first should start with understanding how to build a matrix class that enables us to create a matrix that has basic functions of a matrix such as print, matrix addition, scalar, element-wise, or matrix multiplication, have access and set entries.

## Why Class?

Creating a class allows new instances of a type of object to be made. Each class instance can have different attributes and methods. Thus, using a class will enable us to create an instance that has attributes and multiple functions of a matrix. For example, if A = [[2,1],[2,3]], B = [[0,1],[2,1]], A + B should give us a matrix [[2,3],[4,4]].

`__method__` is a private method. Even though you cannot call the private method directly, these built-in methods in a class in Python will let the compiler know which one to access when you perform a specific function or operation. You just need to use the right method for your goal.

## Build a Matrix Class

I will start from what we want to create then find the way to create the class according to our goal. I recommend you to test your class as you add more methods to see if the class acts like what you want.

### Create and print a Matrix object

What we want to achieve with our class is below

```
        >>> A = Matrix(dims=(3,3), fill=1.0)
	>>> print( A )
	------------- output -------------
	|   1.000,    1.000,    1.000| 
	|   1.000,    1.000,    1.000| 
	|   1.000,    1.000,    1.000| 
	----------------------------------
```

Thus, we want to create a `Matrix` object with parameters that are `dims` and `fill`.

```python
class Matrix: 
 
  def __init__(self, dims, fill):    
     self.rows = dims[0]  
     self.cols = dims[1]   
     self.A = [[fill] * self.cols for i in range(self.rows)]
```

We use `__init__` as a constructor to initialize the attributes of our class (rows, cols, and matrix A). The rows and cols are assigned by the first and second dimensions of the matrix. Matrix A is created with `fill` as the values and `self.cols` and `self.rows` as the shape of the matrix.

We should also create a `__str__` method that enables us to print a readable format like above.

```python
    def __str__(self): 
        m = len(self.A) # Get the first dimension
        mtxStr = ''  mtxStr += '------------- output -------------\n'

        for i in range(m):
            mtxStr += ('|' + ', '.join( map(lambda x:'{0:8.3f}'.format(x), self.A[i])) + '| \n')  mtxStr += '----------------------------------'  return mtxStr
```

### Scaler and Matrix Addition

Goal:

Standard matrix-matrix addition

```
        >>> A = Matrix(dims=(3,3), fill=1.0)
	>>> B = Matrix(dims=(3,3), fill=2.0)
	>>> C = A + B
	>>> print( C )
	------------- output -------------
	|   3.000,    3.000,    3.000| 
	|   3.000,    3.000,    3.000| 
	|   3.000,    3.000,    3.000| 
	----------------------------------
```

Scaler-matrix addition (pointwise)

```
        >>>A = Matrix(dims=(3,3), fill=1.0)
	>>> C = A + 2.0
	>>> print( C )
	------------- output -------------
	|   3.000,    3.000,    3.000| 
	|   3.000,    3.000,    3.000| 
	|   3.000,    3.000,    3.000| 
	---------------------------------- 
```

We use `__add__` method to perform the right addition.

```python
    def __add__(self, other):
		#Create a new matrix
		C = Matrix( dims = (self.rows, self.cols), fill = 0)

		#Check if the other object is of type Matrix
		if isinstance (other, Matrix):
			#Add the corresponding element of 1 matrices to another
			for i in range(self.rows):
				for j in range(self.cols):
					C.A[i][j] = self.A[i][j] + other.A[i][j]

		#If the other object is a scaler
		elif isinstance (other, (int, float)):
			#Add that constant to every element of A
			for i in range(self.rows):
				for j in range(self.cols):
					C.A[i][j] = self.A[i][j] + other

		return C
```

Since addition is commutative, we also want to be able to add on the right-hand-side of the matrix. This could be easily done by calling the left addition.

```python
    def __radd__(self, other):
        return self.__add__(other)
```

## Pointwise Multiplication

Goal:

Matrix-Matrix Pointwise Multiplication

```
        >>> A = Matrix(dims=(3,3), fill=1.0)
	>>> B = Matrix(dims=(3,3), fill=2.0)
	>>> C = A * B
	>>> print( C )
	------------- output -------------
	|   2.000,    2.000,    2.000| 
	|   2.000,    2.000,    2.000| 
	|   2.000,    2.000,    2.000| 
	----------------------------------
```

Scaler-matrix Pointwise Multiplication

```
        >>> A = Matrix(dims=(3,3), fill=1.0)
	>>> C = 2.0 * A
	>>> C = A * 2.0
	>>> print( C )
	------------- output -------------
	|   2.000,    2.000,    2.000| 
	|   2.000,    2.000,    2.000| 
	|   2.000,    2.000,    2.000| 
	----------------------------------
```

Use `__mul__` method and `__rmul__` method to perform left and right point-wise

```python
	def __mul__(self, other): #pointwise multiplication

		C = Matrix( dims = (self.rows, self.cols), fill = 0)
		if isinstance(other, Matrix):

			for i in range(self.rows):
				for j in range(self.cols):
					C.A[i][j] = self.A[i][j] * other.A[i][j]

		#Scaler multiplication
		elif isinstance(other, (int, float)):

			for i in range(self.rows):
				for j in range(self.cols):
					C.A[i][j] = self.A[i][j] * other

		return C 

	#Point-wise multiplication is also commutative
	def __rmul__(self, other):

		return self.__mul__(other)
```

## Standard Matrix-Matrix Multiplication

Goal:

```
        >>> A = Matrix(dims=(3,3), fill=1.0)
	>>> B = Matrix(dims=(3,3), fill=2.0)
	>>> C = A @ B
	>>> print( C )
	------------- output -------------
	|   6.000,    6.000,    6.000| 
	|   6.000,    6.000,    6.000| 
	|   6.000,    6.000,    6.000| 
	----------------------------------
```

Matrix multiplication could be achieved by `__matmul__ `method that is specific for matrix multiplication.

```python
    def __matmul__(self, other): #matrix-matrix multiplication
		if isinstance(other, Matrix):
			C = Matrix( dims = (self.rows, self.cols), fill = 0)

			#Multiply the elements in the same row of the first matrix 
			#to the elements in the same col of the second matrix
			for i in range(self.rows):
				for j in range(self.cols):
					acc = 0

					for k in range(self.rows):
						acc += self.A[i][k] * other.A[k][j]

					C.A[i][j] = acc

		return C
```

## Have Access and Set Entries

Goal:

```
        >>> A = Matrix(dims=(3,3), fill=1.0)
	>>> A[i,j]
	>>> A[i,j] = 1.0
```

Use `__setitem__` method to set the value for the matrix indices and use`__getitem__` method to get value for the matrix indices.

```python
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
```
