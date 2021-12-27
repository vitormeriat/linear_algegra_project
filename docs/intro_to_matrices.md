# Introduction to Matrices

Linear algebra consists of the methods to solve the system of linear equations and their applications to tackle real-world problems. This system of equations is expressed in a regular fashion to create an array or a ‘matrix’ of elements. These matrices allow us to perform different operations on them and make it easy to solve the system of equations.

In this article, we will understand what is a matrix and how to represent a system of linear equations in the form of a matrix. We will also go through various matrix creation routines in Python using the NumPy library.

## What is a Matrix

A matrix is an ordered rectangular array of numbers (real or complex), which has m rows (horizontal set of elements) and n columns (vertical set of elements). In general, rows and columns are called lines. The order of a matrix is represented as *m x n* (pronounced *m* by *n*).

Elements of the matrix are enclosed in *[ ]* or *( )*. For example:

$$
\begin{aligned}
 A =
 \begin{bmatrix}
 5 & 3 & 58 \\
 -4 & 23 & 11 \\
 34 & 2 & -67
 \end{bmatrix}
 \end{aligned}
$$

## Representing System of Linear Equations with Matrices

Let’s now see how we can represent a system of linear equations in the form of a matrix. The equations contain the variable with coefficients and a constant term.

<div align="center" style="width: 100%;">
    <img src="https://cdn-didfa.nitrocdn.com/wkIKMMXDQqRqsyTthNODBhOAXRBgWPrw/assets/static/optimized/rev-4d0b72f/wp-content/uploads/2020/05/equations.svg">
    <h4 style="font-family: courier; font-size: .8em;">System of Equations to Matrix</h4>
</div>

$$
\begin{aligned}
 2x + 5y &= 16\\
 4x + 3y &= 8
 \end{aligned}
$$

These equations are represented with an **augmented matrix**, where the first equation forms the first row and the second equation forms the second row.

The first column represents the x coefficients and the second column represents the y coefficients. The constants in the equations are entered in the third column.

The augmented matrix formed from the above system of equations, say A, is:

$$
\begin{aligned}
 A =
 \begin{bmatrix}
 2 & 5 & 16 \\
 4 & 3 & 8
 \end{bmatrix}
 \end{aligned}
$$

If a term is missing in the equation, it means that the coefficient of that variable is 0.

$$
\begin{aligned}
 8y – 3z &= 19\\
 2x + z &= -5\\
 7x + 4y + 6z &= 28\\
 \Downarrow\\
 0x + 8y – 3z &= 19\\
 2x + 0y + z &= -5\\
 7x + 4y + 6z &= 28\\
 \end{aligned}
$$

If the constant terms are on the left side of the equal sign or variable terms are on the right side of the equal sign, we have to rearrange the equations to bring them to the standard form before representing them in the augmented matrix.

Also, make sure that the sequence of the variable terms is uniform.

$$
\begin{aligned}
 3 – 5x + 7z &= 12y\\
 4x + y – 11 &= -9z\\
 6y + 8x &= 0\\
 \Downarrow\\
 – 5x -12y + 7z &= -3\\
 4x + y + 9z &= 11\\
 8x + 6y + 0z &= 0\\
 \end{aligned}
$$

$$
\begin{aligned}
 \Rightarrow C =
 \begin{bmatrix}
 -5 & -12 & 7 & -3 \\
 4 & 1 & 9 & 11 \\
 8 & 6 & 0 & 0
 \end{bmatrix}
 \end{aligned}
$$

## Representation of Matrix Elements

Consider the matrix $A$ with 2 rows and 4 columns. An individual element of the matrix is represented as $a_{ij}$, where $i$ is the row number and $j$ is the column number. The entire $2 \times 4$ matrix can be represented as:

$$
\begin{aligned}
 A_{2\times4} =
 \begin{bmatrix}
 a_{11} & a_{12} & a_{13} & a_{14} \\
 a_{21} & a_{22} & a_{23} & a_{24}
 \end{bmatrix}
 \end{aligned}
$$

## Creating Matrices in Python using NumPy

Link to notebook...
