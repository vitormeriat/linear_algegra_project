# How to Build a Matrix Module from Scratch

> If you have been importing Numpy for matrix operations but don’t know how the module is built, this article will show you how to build your own matrix module

## Motivation

Numpy is a useful library that enables you to create a matrix and perform matrix operations with ease. But what if you want to create a matrix class with features that are not included in the Numpy library? To be able to do that, we first should start with understanding how to build a matrix class that enables us to create a matrix that has basic functions of a matrix such as print, matrix addition, scalar, element-wise, or matrix multiplication, have access and set entries.

Tutorial here...

---

```
linear_algegra_project/
│
├── linear_algebra/
│   ├── __init__.py
│   ├── __main__.py
│   └── matrix.py
│
├── tests/
│   ├── __init__.py
│   └── test_linear_algebra.py
│
├── README.md
└── requirements.txt
```

Run tests...

```
python -m pytest tests
```



