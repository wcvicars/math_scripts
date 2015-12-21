from __future__ import division
from math import sqrt, acos, radians
import numpy as np

class Vector(object):
    
    def __init__(self, values):
        self.values = values
    
    def magnitude(self):
        return sqrt(sum([value**2 for value in self.values]))
    
    def angle(self, other, degrees = False):
        angle = acos(self*other/(self.magnitude()*other.magnitude()))
        if degrees:
            return radians(angle)
        return angle
    
    def scalar_mult(self, scalar):
        prod_vec = [scalar*self.values[i] for i in range(len(self.values))]
        return Vector(prod_vec)
    
    def __add__(self, other):
        assert(len(self.values) == len(other.values))
        sum_vec = [self.values[i] + other.values[i] for i in range(len(self.values))]
        return Vector(sum_vec)
    
    def __sub__(self, other):
        assert(len(self.values) == len(other.values))
        diff_vec = [self.values[i] - other.values[i] for i in range(len(self.values))]
        return Vector(diff_vec)
    
    def __mul__(self, other):
        return sum([self.values[i] * other.values[i] for i in range(len(self.values))])
    
    def __str__(self):
        value_string = ''
        for value in self.values:
            value_string += str(value) + ' '
        return '[ ' + value_string + ']'

class Matrix(object):
    
    def __init__(self, values):
        self.values = values
        self.dimension = len(self.values)
    
    def __add__(self, other):
        return_mat = [[0 for v in self.values[0]] for d in range(self.dimension)]
        for i in range(self.dimension):
            for j in range(len(self.values[0])):
                return_mat[i][j] = self.values[i][j] + other.values[i][j]
        return return_mat
    
    def scalar_mult(self, alpha):
        return_mat = [[0 for v in self.values[0]] for d in range(self.dimension)]
        for i in range(self.dimension):
            for j in range(len(self.values[0])):
                return_mat[i][j] *= alpha
        return Matrix(return_mat)
    
    def matrix_vector_mult(self, vec):
        assert len(vec.values) == self.dimension
        return_vec = []
        for i in range(self.dimension):
            to_append = 0
            for j in range(len(vec.values)):
                to_append += self.values[j][i] * vec.values[j]
            return_vec.append(to_append)
        return Vector(return_vec)
    
    def transpose(self):
        return_mat = []
        for i in range(len(self.values[0])): 
            new = []
            for j in range(self.dimension):
                new.append(self.values[j][i])
            return_mat.append(new)
        return Matrix(return_mat)
        
    def set_to_identity(self):
        return_mat = [[0 for v in self.values[0]] for d in range(self.dimension)]
        for i in range(self.dimension):
            for j in range(len(self.values[0])):
                if i == j:
                    return_mat[i][j] = 1
                else:
                    return_mat[i][j] = 0
        return Matrix(return_mat)
    
    def set_to_lower_triangular(self, case = 'lower'):
        return_mat = [[0 for v in self.values[0]] for d in range(self.dimension)]
        for i in range(self.dimension):
            for j in range(len(self.values[0])):
                if i > j:
                    return_mat[i][j] = self.values[i][j]
                elif i == j:
                    if case == 'lower':
                        return_mat[i][j] = self.values[i][j]
                    elif case == 'strict':
                        return_mat[i][j] = 0
                    elif case == 'unit':
                        return_mat[i][j] = 1 
        return Matrix(return_mat)
    
    def set_to_upper_triangular(self, case = 'upper'):
        return_mat = [[0 for v in self.values[0]] for d in range(self.dimension)]
        for i in range(self.dimension):
            for j in range(len(self.values[0])):
                if i < j:
                    return_mat[i][j] = self.values[i][j]
                elif i == j:
                    if case == 'upper':
                        return_mat[i][j] = self.values[i][j]
                    elif case == 'strict':
                        return_mat[i][j] = 0
                    elif case == 'unit':
                        return_mat[i][j] = 1
        return Matrix(return_mat)
        
        
A = Matrix([[-1, 0, 2, 1], [2, -1, 1, 2], [3, 1, -1, 3]])
print A.transpose()

t = Matrix([[-1, 2, 4]])
print t.transpose()


A = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print A.set_to_identity()

# [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

A = np.matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print np.eye(len(A))

# [[ 1.  0.  0.]
#  [ 0.  1.  0.]
#  [ 0.  0.  1.]]

A = Matrix([[3, 0, 0], [0, -1, 0], [0, 0, 2]])
x = Vector(([2, 1, -2]))
print A.matrix_vector_mult(x)

# [ 6 -1 -4 ]

A = Matrix([[3, 8, 2], [-9, -1, 4], [7, 2, 2]])
print np.matrix(A.set_to_lower_triangular(case = 'strict').values)

# [[ 0  0  0]
#  [-9  0  0]
#  [ 7  2  0]]

print np.tril(np.matrix(A.values), -1) # numpy tril and triu methods

B = Matrix([[3, 8, 2], [-9, -1, 4], [7, 2, 2]])
print np.matrix(B.set_to_upper_triangular(case = 'upper').values)

print np.triu(np.matrix(B.values))

A = Matrix([[-1, 0, 2, 1], [2, -1, 1, 2], [3, 1, -1, 3]])
x = Matrix([[-1, 2, 4]])

print np.matrix(A.transpose().values)

# [[-1  2  3]
#  [ 0 -1  1]
#  [ 2  1 -1]
#  [ 1  2  3]]

print np.matrix(x.transpose().values)

# [[-1]
#  [ 2]
#  [ 4]]


'''
The nice thing about symmetric matrices is that only approximately half of the 
entries need to be stored. Often, only the lower triangular or only the upper 
triangular part of a symmetric matrix is stored.
'''

A = Matrix([[3, 0, 0], [0, -1, 0], [0, 0, 2]])
B = Matrix([[3, 8, 2], [-9, -1, 4], [7, 2, 2]])