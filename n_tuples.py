from __future__ import annotations
from typing import List, Optional

Array = List[float]


class NTuple:
    """
    An n-tuple is just a finite ordered sequence of elements of size n.
    """

    def __init__(self) -> None:
        """Since this is the baseclass, it cannot be instantiated.

        Raises:
            NotImplementedError: error to indicate the baseclass
        """
        raise NotImplementedError


class Vector(NTuple):
    """
    A vector is, concretely, a collection of points in a finite n-dimensional space.
    """

    def __init__(self, items: Array = []) -> None:
        """Initializes the Vector instance with a list of floats or an empty list as its values

        Arguments:
            items {Array} -- the initial values that compose a particular vector (default: {[]})
        """
        self.items = items
        self.length = len(items)

    def __repr__(self) -> str:
        """Defines a formal string representation for a Vector

        Returns:
            str -- a formal representation of the Vector object
        """
        return f'Vector({self.items})'

    def __str__(self) -> str:
        """Produces a beautyfied string representation of a Vector for visualization purposes. This is cheating but
        it works, since we are using to our advantage the fact that the Vector's items are just a list of floats.

        Returns:
            str -- a beautyfied representation of the Vector object
        """
        return str(self.items)

    def __len__(self) -> int:
        """Computates and returns the length of the vector

        Returns:
            int -- number of elements (length) of the vector
        """
        return self.length

    def add(self, other: Vector, inplace: bool = False) -> Optional[Vector]:
        """Adds two vectors of the same length together using the principles of vector addition.

        Arguments:
            other {Vector} -- the vector to be added with {self}

        Keyword Arguments:
            inplace {bool} -- whether or not the addition should mutate {self} (default: {False})

        Returns:
            Optional[Vector] -- either a vector if {inplace == False} or None
        """
        assert isinstance(other, Vector), 'item to be added must be a Vector'
        assert len(self) == len(other), 'vectors should be the same length'

        sum_of_elements = [self_item + other_item for self_item, other_item in
                           zip(self.items, other.items)]

        if inplace:
            self.items = sum_of_elements
            return None

        return Vector(sum_of_elements)

    def __add__(self, other: Vector) -> Optional[Vector]:
        """Defines how a Vector object behaves with the '+' operator. Utilizes the Vector add()
        method.

        Arguments:
            other {Vector} -- the Vector object to be added with {self}

        Returns:
            Vector -- the resulting Vector from the sum of {self} and {other}
        """
        return self.add(other)

    def subtract(self, other: Vector, inplace: bool = False) -> Optional[Vector]:
        """Subtracts the elements of two vectors of the same length using the principles
        of vector subtraction.

        Arguments:
            other {Vector} -- the vector to be subtracted from {self}

        Keyword Arguments:
            inplace {bool} -- whether or not the subtraction should mutate {self} (default: {False})

        Returns:
            Optional[Vector] -- either a vector if {inplace == False} or None
        """
        assert isinstance(
            other, Vector), 'item to be subtracted must be a Vector'
        assert len(self) == len(other), 'vectors should be the same length'

        sub_of_elements = [self_item - other_item for self_item, other_item in
                           zip(self.items, other.items)]

        if inplace:
            self.items = sub_of_elements
            return None

        return Vector(sub_of_elements)

    def __sub__(self, other: Vector) -> Optional[Vector]:
        """Defines how a Vector object behaves with the '-' operator. Utilizes the Vector subtract()
        method.

        Arguments:
            other {Vector} -- the Vector object to be subtracted from {self}

        Returns:
            Vector -- the resulting Vector from the subtraction of {self} and {other}
        """
        return self.subtract(other)

    def vector_sum(self, vectors: List[Vector], inplace: bool = False) -> Optional[Vector]:
        """Adds the elements of {self} to those of a list of Vectors, elementwise.

        Arguments:
            vectors {List[Vector]} -- a list of Vectors of the same length as {self}

        Keyword Arguments:
            inplace {bool} -- whether or not to mutate {self} (default: {False})

        Returns:
            Optional[Vector] -- either a vector if {inplace == False} or None
        """
        assert vectors, 'no vectors provided'

        vectors.append(self)

        num_elements = len(vectors[0])
        assert all(
            len(v) == num_elements for v in vectors), 'vectors must be the same length'

        sum_of_all = [sum(vec.items[i] for vec in vectors)
                      for i in range(num_elements)]

        if inplace:
            self.items = sum_of_all
            return None

        return Vector(sum_of_all)


if __name__ == '__main__':
    # Initalize two test vectors
    test_v = Vector([1, 2, 3])
    test_w = Vector([4, 5, 6])

    # Test the length property
    assert test_v.length == test_w.length == 3
    assert len(test_v) == len(test_w) == 3

    # Create a variable to hold the vector addition of {test_v} and {test_w}
    test_add = test_v.add(test_w)
    # Check that the + operator works alright
    test_add_op = test_v + test_w

    # Check that {test_add} and {test_add_op} are Vectors with value [5, 7, 9]
    assert test_add is not None and isinstance(
        test_add, Vector) and test_add.items == [5, 7, 9]

    assert test_add_op is not None and isinstance(
        test_add_op, Vector) and test_add_op.items == [5, 7, 9]

    # Check that vector addition returns None when done inplace
    assert test_v.add(test_w, inplace=True) is None

    # Check that {test_v} is now mutated after vector addition. It should now be [5, 7, 9]
    assert test_v.items == [5, 7, 9]
