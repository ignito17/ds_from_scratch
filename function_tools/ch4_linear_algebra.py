# Linear algebra is the branch of mathematics that deals with vector spaces.
# Abstractly, vectors are objects that can be added together (to form new vectors) and that
# can be multiplied by scalars (i.e., numbers), also to form new vectors.

# Abstractly, vectors are objects that can be added together (to form new vectors) and that
# can be multiplied by scalars (i.e., numbers), also to form new vectors.
# Concretely (for us), vectors are points in some finite-dimensional space. Although you
# might not think of your data as vectors, they are a good way to represent numeric data.
# For example, if you have the heights, weights, and ages of a large number of people, you
# can treat your data as three-dimensional vectors (height, weight, age). If you’re
# teaching a class with four exams, you can treat student grades as four-dimensional vectors
# (exam1, exam2, exam3, exam4).
# The simplest from-scratch approach is to represent vectors as lists of numbers. A list of
# three numbers corresponds to a vector in three-dimensional space, and vice versa:

# The simplest from-scratch approach is to represent vectors as lists of numbers. A list of
# three numbers corresponds to a vector in three-dimensional space, and vice versa:

height_weight_age = [70,        # inches,
                        170,    # pounds,
                        40 ]    # years
grades = [95, # exam1
            80,                 # exam2
            75,                 # exam3
            62 ]                # exam4


# One problem with this approach is that we will want to perform arithmetic on vectors.
# Because Python lists aren’t vectors (and hence provide no facilities for vector arithmetic),
# we’ll need to build these arithmetic tools ourselves. So let’s start with that.
# To begin with, we’ll frequently need to add two vectors. Vectors add componentwise. This
# means that if two vectors v and w are the same length, their sum is just the vector whose
# first element is v[0] + w[0], whose second element is v[1] + w[1], and so on. (If they’re
# not the same length, then we’re not allowed to add them.)

# We can easily implement this by zip-ing the vectors together and using a list
# comprehension to add the corresponding elements:

def vector_add(v, w):
    """adds corresponding elements"""
    return [v_i + w_i
            for v_i, w_i in zip(v, w)]

def vector_subtract(v, w):
    """subtracts corresponding elements"""
    return [v_i - w_i
            for v_i, w_i in zip(v, w)]

def vector_sum(vectors):
    """sums all corresponding elements"""
    result = vectors[0]                         # start with the first vector
    for vector in vectors[1:]:                  # then loop over the others
        result = vector_add(result, vector)     # and add them to the result
    return result


# If you think about it, we are just reduce-ing the list of vectors using vector_add, which
# means we can rewrite this more briefly using higher-order functions:

from functools import partial,reduce
def vector_sum(vectors):
    return reduce(vector_add, vectors)

# or even:
vector_sum = partial(reduce, vector_add)

# We’ll also need to be able to multiply a vector by a scalar, which we do simply by
# multiplying each element of the vector by that number:
def scalar_multiply(c, v):
    """c is a number, v is a vector"""
    return [c * v_i for v_i in v]

# This allows us to compute the componentwise means of a list of (same-sized) vectors:
def vector_mean(vectors):
    """compute the vector whose ith element is the mean of the
    ith elements of the input vectors"""
    n = len(vectors)
    return scalar_multiply(1/n, vector_sum(vectors))

# A less obvious tool is the dot product. The dot product of two vectors is the sum of their
# componentwise products:
def dot(v, w):
    """v_1 * w_1 + ... + v_n * w_n"""
    return sum(v_i * w_i
                for v_i, w_i in zip(v, w))
# The dot product measures how far the vector v extends in the w direction. For example, if
# w = [1, 0] then dot(v, w) is just the first component of v. Another way of saying this is
# that it’s the length of the vector you’d get if you projected v onto w


# Using this, it’s easy to compute a vector’s sum of squares:
def sum_of_squares(v):
    """v_1 * v_1 + ... + v_n * v_n"""
    return dot(v, v)

# Which we can use to compute its magnitude (or length):
import math
def magnitude(v):
    return math.sqrt(sum_of_squares(v))             # math.sqrt is square root function


# We now have all the pieces we need to compute the distance between two vectors, defined

def squared_distance(v, w):
    """(v_1 - w_1) ** 2 + ... + (v_n - w_n) ** 2"""
    return sum_of_squares(vector_subtract(v, w))

def distance(v, w):
    return math.sqrt(squared_distance(v, w))


# Which is possibly clearer if we write it as (the equivalent):
def distance(v, w):
    return magnitude(vector_subtract(v, w))


# Matrix
# A matrix is a two-dimensional collection of numbers. We will represent matrices as lists
# of lists, with each inner list having the same size and representing a row of the matrix. If
# A is a matrix, then A[i][j] is the element in the ith row and the jth column.

A = [[1, 2, 3],     # A has 2 rows and 3 columns
    [4, 5, 6]]
B = [[1, 2],        # B has 3 rows and 2 columns
    [3, 4],
    [5, 6]]

# Given this list-of-lists representation, the matrix A has len(A) rows and len(A[0])
# columns, which we consider its shape:
def shape(A):
    num_rows = len(A)
    num_cols = len(A[0]) if A else 0 # number of elements in first row
    return num_rows, num_cols


# If a matrix has n rows and k columns, we will refer to it as a matrix. We can (and
# sometimes will) think of each row of a matrix as a vector of length k, and each
# column as a vector of length n:
def get_row(A, i):
    return A[i]                 # A[i] is already the ith row
def get_column(A, j):
    return [A_i[j]              # jth element of row A_i
            for A_i in A]       # for each row A_i


# We’ll also want to be able to create a matrix given its shape and a function for generating
# its elements. We can do this using a nested list comprehension:
def make_matrix(num_rows, num_cols, entry_fn):
    """returns a num_rows x num_cols matrix
    whose (i,j)th entry is entry_fn(i, j)"""
    return [[entry_fn(i, j)                 # given i, create a list
    for j in range(num_cols)]               # [entry_fn(i, 0), ... ]
    for i in range(num_rows)]               # create one list for each i

def is_diagonal(i, j):
    """1's on the 'diagonal', 0's everywhere else"""
    return 1 if i == j else 0

make_matrix(3,3,is_diagonal)


# Matrices will be important to us for several reasons.
# First, we can use a matrix to represent a data set consisting of multiple vectors, simply by
# considering each vector as a row of the matrix.

# heights, weights, and ages of 1,000 people you could put them in a matrix:
data = [[70, 170, 40],
        [65, 120, 26],
        [77, 250, 19],
        # ....
        ]

# Second, as we’ll see later, we can use an matrix to represent a linear function that
# maps k-dimensional vectors to n-dimensional vectors.

# Third, matrices can be used to represent binary relationships. In Chapter 1, we represented
# the edges of a network as a collection of pairs (i, j). An alternative representation would
# be to create a matrix A such that A[i][j] is 1 if nodes i and j are connected and 0
# otherwise.
# Recall that before we had:
friendships = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
                (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

# We could also represent this as:
# user 0 1 2 3 4 5 6 7 8 9
#
friendships = [[0, 1, 1, 0, 0, 0, 0, 0, 0, 0],              # user 0
                [1, 0, 1, 1, 0, 0, 0, 0, 0, 0],             # user 1
                [1, 1, 0, 1, 0, 0, 0, 0, 0, 0],             # user 2
                [0, 1, 1, 0, 1, 0, 0, 0, 0, 0],             # user 3
                [0, 0, 0, 1, 0, 1, 0, 0, 0, 0],             # user 4
                [0, 0, 0, 0, 1, 0, 1, 1, 0, 0],             # user 5
                [0, 0, 0, 0, 0, 1, 0, 0, 1, 0],             # user 6
                [0, 0, 0, 0, 0, 1, 0, 0, 1, 0],             # user 7
                [0, 0, 0, 0, 0, 0, 1, 1, 0, 1],             # user 8
                [0, 0, 0, 0, 0, 0, 0, 0, 1, 0]]             # user 9

friendships[0][2] == 1                                      # True, 0 and 2 are friends
friendships[0][8] == 1                                      # False, 0 and 8 are not friends

# Similarly, to find the connections a node has, you only need to inspect the column (or the
# row) corresponding to that node:

# Similarly, to find the connections a node has, you only need to inspect the column (or the
# row) corresponding to that node:
friends_of_five = [i                                                # only need
                    for i, is_friend in enumerate(friendships[5])   # to look at
                    if is_friend]                                   # one row
