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
