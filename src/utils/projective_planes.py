from math import log2

import numpy as np


def is_prime(num):
    """Check if a number is prime.

    Params:
        num (float): The number to be checked.

    Returns:
        bool: 'True' if the number is prime, 'False' otherwise.
    """
    is_integer = isinstance(num, int) or (isinstance(num, float) and num.is_integer())

    if not is_integer or num <= 1:
        return False

    # Check for non-trivial factors
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def is_prime_power(num):
    """Check if a number is a prime power.

    Params:
        num (float): The number to be checked.

    Returns:
        bool: 'True' if the number is a prime power, 'False' otherwise.
    """
    is_integer = isinstance(num, int) or (isinstance(num, float) and num.is_integer())

    if not is_integer or num <= 1:
        return False

    # Compute the i-th root of num and check if it's prime
    for i in range(1, int(log2(num)) + 1):
        root = num ** (1/i)
        if root.is_integer() and is_prime(root):
            return True
    return False


def compute_incidence_matrix(order):
    """Compute the incidence matrix of a finite projective plane with specified order.

    Params:
        order (int): The order of the finite projective plane.

    Returns:
        np.ndarray: The computed incidence matrix.  Rows correspond to lines and columns correspond to points.

    Raises:
        ValueError: If the argument 'order' is not a prime power.

    Example:
        >>> compute_incidence_matrix(2)
        array([[ True,  True,  True, False, False, False, False],
               [ True, False, False,  True,  True, False, False],
               [ True, False, False, False, False,  True,  True],
               [False,  True, False,  True, False,  True, False],
               [False,  True, False, False,  True, False,  True],
               [False, False,  True,  True, False, False,  True],
               [False, False,  True, False,  True,  True, False]])
    """
    if not is_prime_power(order):
        raise ValueError("The 'order' argument must be a prime power.")

    # Number of points/lines of a finite projective plane of order n is given by n^2 + n + 1
    size = order**2 + order + 1

    # Preallocate incidence matrix, where rows correspond to lines and columns correspond to points
    incidence_matrix = np.zeros((size, size), dtype=bool)

    # Determine which points are on the first line
    which_line = 0
    which_pts = list(range(order + 1))
    incidence_matrix[which_line, which_pts] = True

    # Determine which points are on the next n lines
    for line in range(order):
        which_line += 1
        # The first n + 1 lines will all share point '0'
        which_pts = [0]
        start = (line + 1) * order + 1
        end = start + order
        which_pts.extend(list(range(start, end)))
        incidence_matrix[which_line, which_pts] = True

    # Determine which points are on the final n^2 lines
    for block in range(order):
        for line in range(order):
            which_line += 1
            which_pts = [block + 1]
            for pt in range(order):
                which_pts.append(order * (pt + 1) + ((block * pt + line) % order) + 1)
            incidence_matrix[which_line, which_pts] = True

    return incidence_matrix
