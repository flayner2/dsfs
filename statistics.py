from typing import List
from collections import Counter


def mean(xs: List[float]) -> float:
    """Calculates the arithmetic mean of a list of values

    Arguments:
        xs {List[float]} -- a list of floats of any length

    Returns:
        float -- the mean of the values in {xs}
    """
    return sum(xs) / len(xs)


def _median_odd(xs: List[float]) -> float:
    """Returns the median for an odd length vector

    Arguments:
        xs {List[float]} -- a vector with an odd number of points

    Returns:
        float -- the median (middle value) of vector {xs}
    """
    return sorted(xs)[len(xs) // 2]


def _median_even(xs: List[float]) -> float:
    """Returns the median for an even length vector

    Arguments:
        xs {List[float]} -- a vector with an even number of points

    Returns:
        float -- the median (the mean of both middle values) of vector {xs}
    """
    sorted_xs = sorted(xs)
    hi_midpoint = len(xs) // 2

    return (sorted_xs[hi_midpoint - 1] + sorted_xs[hi_midpoint]) / 2


def median(v: List[float]) -> float:
    """Returns the middle-most value of a vector

    Arguments:
        v {List[float]} -- a vector of any length

    Returns:
        float -- the middle-most (median) value of vector {v}
    """
    return _median_even(v) if len(v) % 2 == 0 else _median_odd(v)


def quantile(xs: List[float], p: float) -> float:
    """Returns the {p}-th percentile value of a vector

    Arguments:
        xs {List[float]} -- a vector of any length
        p {float} -- a percentile value

    Returns:
        float -- the value at the {p}-th percentile of vector {xs}
    """
    p_index = int(p * len(xs))

    return sorted(xs)[p_index]


def mode(x: List[float]) -> List[float]:
    """Returns a list of the most common values of a vector

    Arguments:
        x {List[float]} -- a vector of any length

    Returns:
        List[float] -- a list containing the most common values (mode) of {x}
    """
    counts = Counter(x)
    max_count = max(counts.values())

    return [x_i for x_i, count in counts.items() if count == max_count]


if __name__ == '__main__':
    assert median([1, 10, 2, 9, 5]) == 5
    assert median([1, 9, 2, 10]) == (2 + 9) / 2

    quantile_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    assert quantile(quantile_list, 0.10) == 2
    assert quantile(quantile_list, 0.25) == 3
    assert quantile(quantile_list, 0.75) == 8
    assert quantile(quantile_list, 0.90) == 10
    print('hello!')
    mode_list = [1, 2, 3, 4, 4, 5, 6, 7, 8, 8, 9, 10]

    assert set(mode(mode_list)) == {4, 8}
