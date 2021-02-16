import math
from typing import List, Tuple, Callable

Vector = List[float]
Matrix = List[List[float]]


def add(v: Vector, w: Vector) -> Vector:
    """Adds two vectors together using the principles of vector addition. Returns the sum
    of both vectors. Checks if both vectors have the same length.

    Arguments:
        v {Vector} -- a vector of floats of length n
        w {Vector} -- another vector of floats of the same length n

    Returns:
        Vector -- sum of the input vectors
    """
    assert len(v) == len(w), 'both vectors must have the same length'

    return [v_item + w_item for v_item, w_item in zip(v, w)]


def subtract(v: Vector, w: Vector) -> Vector:
    """Subtracts two vectors together using the principles of vector subtraction. Returns the
    sum result of the subtraction. Checks if both vectors have the same length.

    Arguments:
        v {Vector} -- a vector of floats of length n
        w {Vector} -- another vector of floats of the same length n

    Returns:
        Vector -- result of the subtraction of the input vectors
    """
    assert len(v) == len(w), 'both vectors must have the same length'

    return [v_item - w_item for v_item, w_item in zip(v, w)]


def vector_sum(vectors: List[Vector]) -> Vector:
    """Adds a list of vectors componentwise. In other words, for each nth element of each vector,
    add those together to be the nth element of a result vector.

    Arguments:
        vectors {List[Vector]} -- a list of vectors of the same length

    Returns:
        Vector -- a vector whose elements are the sum of the input vectors' elements
    """
    assert vectors, 'no vectors provided'

    num_elements = len(vectors[0])
    assert all(
        len(v) == num_elements for v in vectors), 'vectors must be the same length'

    return [sum(vec[i] for vec in vectors) for i in range(num_elements)]


def scalar_multiply(s: float, v: Vector) -> Vector:
    """Multiplies every element of vector {v} by a scalar {s}, then returns the resulting vector.

    Arguments:
        s {float} -- float to mutiply a vector's elements by
        v {Vector} -- vector of any length

    Returns:
        Vector -- the vector containing the product of the scalar multiplication
    """
    return [s * v_item for v_item in v]


def vector_mean(vectors: List[Vector]) -> Vector:
    """Calculates the elementwise mean of the values in a list of same-sized vectors.

    Arguments:
        vectors {List[Vector]} -- [description]

    Returns:
        Vector -- [description]
    """
    n = len(vectors)

    return scalar_multiply(1/n, vector_sum(vectors))


def dot(v: Vector, w: Vector) -> float:
    """Computes the sum of the componentwise products of two vectors. Returns the dot product.

    Arguments:
        v {Vector} -- a vector of floats of length n
        w {Vector} -- another vector of floats of the same length n

    Returns:
        float -- the dot product of the input vectors
    """
    assert len(v) == len(w), 'vectors must be the same length'

    return sum(v_item * w_item for v_item, w_item in zip(v, w))


def sum_of_squares(v: Vector) -> float:
    """Computes the sum of the squares of all the elements of {v}

    Arguments:
        v {Vector} -- a vector of any length

    Returns:
        float -- the sum of the square of every element of vector {v}
    """
    return dot(v, v)


def magnitude(v: Vector) -> float:
    """Returns the magnitude (or length) of a vector {v}

    Arguments:
        v {Vector} -- a vector of any length

    Returns:
        float -- the magnitude of vector {v}
    """
    return math.sqrt(sum_of_squares(v))


def distance(v: Vector, w: Vector) -> float:
    """Computes the distance between two vectors

    Arguments:
        v {Vector} -- a vector of any length
        w {Vector} -- a vector of the same length of {v}

    Returns:
        float -- the distance between vectors {v} and {w}
    """
    return magnitude(subtract(v, w))


def shape(A: Matrix) -> Tuple[int, int]:
    """Returns the shape of a matrix in function of its rows and columns

    Arguments:
        A {Matrix} -- a matrix of any length

    Returns:
        Tuple[int, int] -- the shape of the matrix as (n_rows, n_cols)
    """
    num_rows = len(A)
    num_cols = len(A[0]) if A else 0

    return num_rows, num_cols


def get_row(A: Matrix, i: int) -> Vector:
    """Returns the i-th row of a matrix as a vector

    Arguments:
        A {Matrix} -- a matrix of any length
        i {int} -- the row to be returned as a vector

    Returns:
        Vector -- the {i}-th row of matrix {A} as a vector
    """
    return A[i]


def get_column(A: Matrix, j: int) -> Vector:
    """Returns the j-th column of a matrix as a vector

    Arguments:
        A {Matrix} -- a matrix of any length
        j {int} -- the column to be returned as a vector

    Returns:
        Vector -- the {j}-th column of matrix {A} as a vector
    """
    return [A_i[j] for A_i in A]


def make_matrix(num_rows: int, num_cols: int, entry_fn: Callable[[int, int], float]) -> Matrix:
    """Creates a matrix of shape {num_rows} x {num_cols} whose (i, j)-entry is {entry_fn}(i, j)

    Arguments:
        num_rows {int} -- number of rows for the resulting matrix
        num_cols {int} -- number of columns for the resulting matrix
        entry_fn {Callable[[int, int], float]} -- a function to define the values of the matrix

    Returns:
        Matrix -- a {num_rows} x {num_cols} with {entry_fn}(i, j) elements for each (i, j)
    """
    return [[entry_fn(i, j)
             for j in range(num_cols)]
            for i in range(num_rows)]


def identity_matrix(n: int) -> Matrix:
    """Constructs and returns a {n} x {n} identity matrix (a matrix with 1s on the diagonals and 0s elsewhere)

    Arguments:
        n {int} -- number of rows and columns for the resulting matrix

    Returns:
        Matrix -- a {n} x {n} identity matrix
    """
    return make_matrix(n, n, lambda i, j: 1 if i == j else 0)


if __name__ == '__main__':
    # Vector operations
    assert add([1, 2, 3], [4, 5, 6]) == [5, 7, 9]
    assert subtract([5, 7, 9], [4, 5, 6]) == [1, 2, 3]
    assert vector_sum([[1, 2], [3, 4], [5, 6], [7, 8]]) == [16, 20]
    assert scalar_multiply(2, [1, 2, 3]) == [2, 4, 6]
    assert vector_mean([[1, 2], [3, 4], [5, 6]]) == [3, 4]
    assert dot([1, 2, 3], [4, 5, 6]) == 32
    assert sum_of_squares([1, 2, 3]) == 14
    assert magnitude([3, 4]) == 5
    assert distance([2, 3, 4, 2], [1, -2, 1, 3]) == 6

    # Matrices
    assert shape([[1, 2, 3], [4, 5, 6]]) == (2, 3)
    assert get_row([[1, 2, 3], [4, 5, 6]], 0) == [1, 2, 3]
    assert get_column([[1, 2, 3], [4, 5, 6]], 0) == [1, 4]
    assert identity_matrix(5) == [[1, 0, 0, 0, 0],
                                  [0, 1, 0, 0, 0],
                                  [0, 0, 1, 0, 0],
                                  [0, 0, 0, 1, 0],
                                  [0, 0, 0, 0, 1]]
