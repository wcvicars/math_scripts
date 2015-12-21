import math
import matplotlib.pyplot as plt
import numpy as np

class Vector(object):
    
    def __init__(self, values):
        self.values = values
    
    def getValues(self):
        return self.values
    
    def copy(self):
        return Vector(self.values)
    
    def scalar_mult(self, alpha):
        return Vector([self.values[i]*alpha for i in range(len(self.values))])
    
    def axpy(self, alpha, other):
        return (self.scalar_mult(alpha) + other)
    
    def magnitude(self):
        return math.sqrt(sum([self.values[i]**2 for i in range(len(self.values))]))
    
    def __add__(self, other):
        if len(self.values) != len(other.values):
            return 'Invalid operation'
        return Vector([self.values[i] + other.values[i] for i in range(len(self.values))])
    
    def __mul__(self, other):
        if len(self.values) != len(other.values):
            return 'Invalid operation'
        return sum([self.values[i]*other.values[i] for i in range(len(self.values))])
    
    def __str__(self):
        value_list = self.values
        value_string = ''
        for value in value_list:
            value_string += str(value) + ' '
        return '< ' + value_string + '>'

class Matrix(object):
    
    def __init__(self, values):
        self.values = values
        self.dimension = len(self.values)
    
    def getValues(self):
        return self.values
    
    def __add__(self, other):
        return_mat = [[0 for v in self.values[0]] for d in range(self.dimension)]
        for i in range(self.dimension):
            for j in range(len(self.values[0])):
                return_mat[i][j] = self.values[i][j] + other.values[i][j]
        return Matrix(return_mat)
    
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
                to_append += self.values[i][j] * vec.values[j]
            return_vec.append(to_append)
        return Vector(return_vec)
    
    def __mul__(self, other):
        assert len(self.values[0]) == other.dimension
        return_mat = [[] for d in range(self.dimension)]
        for row in range(self.dimension):
            row_vector = Vector(self.values[row])
            for column in range(len(other.values[0])):
                column_vector = Vector([other.values[i][column] for i in range(other.dimension)])
                return_mat[row].append(row_vector*column_vector)
        return Matrix(return_mat)
    
    def trace(self):
        assert self.dimension == len(self.values[0])
        trace = 0
        i = 0
        j = 0
        while i < self.dimension:
            trace += self.values[i][j]
            i += 1; j += 1
        return trace
    
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
        
class Shape(object):
    
    def __init__ (self, nodes):
        self.nodes = nodes
    
    def getData(self):
        xvals = [self.nodes[i][0] for i in range(len(self.nodes))]
        yvals = [self.nodes[i][1] for i in range(len(self.nodes))]
        xvals.append(self.nodes[0][0])
        yvals.append(self.nodes[0][1])
        return xvals, yvals
    
    def plotShape(self):
        for i in self.nodes:
            plt.plot(i[0], i[1], 'o')
        xvals, yvals = self.getData()
        plt.plot(xvals, yvals)
        plt.xlim(-10, 10); plt.xticks(range(-10, 10)); plt.ylim(-10, 10); plt.yticks(range(-10, 10))
        plt.axes()
        plt.grid(b = True, which = 'major'); plt.grid(b = True, which = 'minor')
        plt.axhline(0, color = 'black'); plt.axvline(0, color = 'black')
    
    def translate(self, trans):
        xvals, yvals = self.getData()
        xvals = [xvals[i] + trans[0] for i in range(len(xvals))]
        yvals = [yvals[i] + trans[1] for i in range(len(yvals))]
        return Shape([(xvals[i], yvals[i]) for i in range(len(xvals))]).plotShape()
    
    def rotate(self, point, degrees):
        xvals, yvals = self.getData()
 
        theta = math.radians(degrees)
        
        xdiff = [xvals[i] - point[0] for i in range(len(xvals))]
        ydiff = [yvals[i] - point[1] for i in range(len(yvals))]
        
        vectors = [Vector([x, y]) for x, y in zip(xdiff, ydiff)]
        
        trans_matrix = Matrix([[math.cos(theta), -math.sin(theta)], [math.sin(theta), math.cos(theta)]])
        
        trans_vectors = [trans_matrix.matrix_vector_mult(vec) for vec in vectors]
        
        return Shape([(point[0] + vec.getValues()[0], point[1] + vec.getValues()[1]) for vec in trans_vectors]).plotShape()
        
    def reflect(self, slope, c = 0):
        pass
        
    def dilate(self, point, scale_factor):
        pass