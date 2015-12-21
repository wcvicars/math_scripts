# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 06:53:28 2015

@author: wcvicars
"""

from __future__ import division

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import math
import sympy
from scipy.integrate import quad

x, y, z = sympy.symbols('x y z')

class Calc:

    def __init__(self, function):
        self.function = function

    def get(self):
        return self.function

    def D1(self):
        return sympy.simplify(sympy.diff(self.function))

    def D2(self):
        return sympy.simplify(sympy.diff(sympy.diff(self.function)))
    
    def indefInt(self):
        return sympy.simplify(sympy.integrate(self.function, x))
    
    def defInt(self, (a, b)):
        return sympy.simplify(sympy.integrate(self.function, (x, a, b)))
    
    def average(self, (start, stop)):
        return (1.0/(stop - start))*self.defInt((start, stop))

    def evaluate(self, val, D):
        
        if D == -1:
            return sympy.integrate(self.function).subs(x, val)
        if D == 0:
            return self.function.subs(x, val)
        elif D == 1:
            try:
                return sympy.diff(self.function).subs(x, val)
            except(ValueError):
                print "The first derivative cannot be evaluated: f' = {0}".format(sympy.diff(self.function))
        elif D == 2:
            try:
                return sympy.diff(sympy.diff(self.function).subs(x, val))
            except(ValueError):
                print "The second derivative cannot be evaluated: f' = {0}".\
                    format(sympy.diff(sympy.diff(self.function)))
    
    def solve(self, D, val = 0):
        if D == 0:
            return sympy.solve(sympy.Eq(val, self.function))
        elif D == 1:
            return sympy.solve(sympy.Eq(val, sympy.diff(self.function)))
        elif D == 2:
            return sympy.solve(sympy.Eq(val, sympy.diff(sympy.diff(self.function))))

    def plotFunction(self, D, (start, stop)):
        seq = np.arange(start, stop, 0.01)
        vals = []
        if D == -1:
            fun = sympy.lambdify(x, sympy.integrate(self.function))
        elif D == 0:
            fun = sympy.lambdify(x, self.function)
        elif D == 1:
            fun = sympy.lambdify(x, sympy.diff(self.function))
        elif D == 2:
            fun = sympy.lambdify(x, sympy.diff(sympy.diff(self.function)))
        for i in seq:
            try:
                vals.append(fun(i))
            except:
                vals.append('NaN')
        plt.plot(seq, vals, 'blue')
    
    def rectangles(self, n, (start, stop), approx = 'midpoint'):
        
        self.plotFunction(0, (start, stop))
        step = (stop - start) / n
        seq = np.arange(start, stop, step)
        nodes = []
        
        def rectPlot(nodeList):
            xvals = []
            yvals = []
            for node in nodeList:
               xvals.append(node[0])
               yvals.append(node[1])
            xvals.append(nodeList[0][0])
            yvals.append(nodeList[0][1])
            plt.plot(xvals, yvals, 'red')
        
        if approx == 'leftHand':
            for i in range(n):
                node1 = (seq[i], self.evaluate(seq[i], 0))
                node2 = (seq[i] + step, self.evaluate(seq[i], 0))
                node3 = (seq[i] + step, 0)
                node4 = (seq[i], 0)
                nodeList = [node1, node2, node3, node4]
                nodes.append(nodeList)
                rectPlot(nodeList)        
        elif approx == 'rightHand':
            for i in range(n):
                node1 = (seq[i], self.evaluate(seq[i] + step, 0))
                node2 = (seq[i] + step, self.evaluate(seq[i] + step, 0))
                node3 = (seq[i] + step, 0)
                node4 = (seq[i], 0)
                nodeList = [node1, node2, node3, node4]
                nodes.append(nodeList)
                rectPlot(nodeList)
        elif approx == 'trapezoid':
            for i in range(n):
                node1 = (seq[i], self.evaluate(seq[i], 0))
                node2 = (seq[i] + step, self.evaluate(seq[i] + step, 0))
                node3 = (seq[i] + step, 0)
                node4 = (seq[i], 0)
                nodeList = [node1, node2, node3, node4]
                nodes.append(nodeList)
                rectPlot(nodeList)
        elif approx == 'midpoint':
            for i in range(n):
                node1 = (seq[i], self.evaluate(seq[i] + step/2, 0))
                node2 = (seq[i] + step, self.evaluate(seq[i] + step/2, 0))
                node3 = (seq[i] + step, 0)
                node4 = (seq[i], 0)
                nodeList = [node1, node2, node3, node4]
                nodes.append(nodeList)
                rectPlot(nodeList)
        else:
            print 'Please enter one of the following approximation methods: "leftHand", "rightHand", "trapezoid" or "midpoint". Default is "midpoint".'
        
        total = 0
        if approx == 'trapezoid':
            for node in nodes:
                total += (node[1][0] - node[0][0]) * 0.5*(node[0][1] + node[1][1])
        else:
            for node in nodes:
                total += (node[1][0] - node[0][0]) * node[0][1]
        
        return total
    
    def arcLength(self, (a, b)):
        fun = sympy.lambdify(x, sympy.sqrt(1 + self.D1()**2.0))
        return quad(fun, a, b)

    def rootsearch(self, (a, b), dx):
        fun = sympy.lambdify(x, self.function)
        x1 = a
        f1 = fun(x1)
        x2 = a + dx
        f2 = fun(x2)
 
        while f1*f2 > 0.0:
            if x1 >= b:
                return None, None
            x1 = x2
            f1 = f2
            x2 = x1 + dx
            f2 = fun(x2)
        
        return x1, x2

    def bisection(self, x1, x2, tol = 1.0E-9):
        fun = sympy.lambdify(x, self.function)
        f1 = fun(x1)
        if f1 == 0.0:
            return x1
        
        f2 = fun(x2)
        if f2 == 0.0:
            return x2
        
        if f1*f2 > 0.0:
            return 'The root is not bracketed within the specified interval'
        
        n = int(math.ceil(math.log(abs(x2 - x1) / tol) / math.log(2.0)))
        
        for i in range(n):
            x_mid = (x2 + x1) / 2.0
            f_mid = fun(x_mid)
            if f_mid == 0:
                return x_mid
            if f2*f_mid < 0.0:
                x1 = x_mid
                f1 = fun(x1)
            else:
                x2 = x_mid
                f2 = fun(x_mid)
            
        return (x1 + x2) / 2.0
                
    def findRoots(self, (a, b), dx):
        print 'The roots of the function are: '
        while 1:
            x1, x2 = self.rootsearch((a, b), dx)
            if x1 != None:
                a = x2
                root = self.bisection(x1, x2)
                if root != None:
                    print root
            else:
                print 'Done'
                break
        raw_input('Press return to exit')
            
    def newtonRhapson(self, (a, b), tol = 1.0E-9):
        fun = sympy.lamdify(x, self.function)
        d_fun = sympy.lambdify(x, sympy.diff(self.function))
        f_a = fun(a)
        if f_a == 0.0:
            return a
        f_b = fun(b)
        if f_b == 0.0:
            return b
        if f_a*f_b > 0.0:
            return 'The root is not bracketed within the specified interval'
        x_mid = (a + b) / 2.0
        for i in range(30):
            f_mid = fun(x_mid)
            if abs(f_mid) < tol:
                return x_mid
            if f_a*f_mid < 0.0:
                b = x_mid
            else:
                a = x_mid
            df_mid = d_fun(x_mid)
            try:
                dx = -f_mid / df_mid
            except ZeroDivisionError:
                dx = b - a

class Shape(object):
    
    def __init__ (self, nodes):
        self.nodes = nodes
    
    def getData(self):
        xvals = []
        yvals = []
        for i in self.nodes:
            xvals.append(i[0])
            yvals.append(i[1])
        xvals.append(self.nodes[0][0])
        yvals.append(self.nodes[0][1])
        return xvals, yvals
    
    def plotShape(self):
        for i in self.nodes:
            plt.plot(i[0], i[1], 'o')
        xvals, yvals = self.getData()
        plt.plot(xvals, yvals)
        plt.xlim(-10, 10)
        plt.xticks(range(-20, 20))
        plt.ylim(-20, 20)
        plt.yticks(range(-20,20))
        plt.axes()
        plt.grid(b = True, which = 'major')
        plt.grid(b = True, which = 'minor')
        plt.axhline(0, color = 'black')
        plt.axvline(0, color = 'black')
    
    def pyth(self, (a, b)):
        return (a**2 + b**2)**(1/2)
    
    def translate(self, trans):
        xvals = []
        yvals = []
        for i in self.nodes:
            xvals.append(i[0] + trans[0])
            yvals.append(i[1] + trans[1])
        #print xvals, yvals
        xvals.append(self.nodes[0][0] + trans[0])
        yvals.append(self.nodes[0][1] + trans[1])
        #print xvals, yvals
        plt.plot(xvals, yvals, linestyle = '--')
    
    def rotate(self, point, degrees):
        xvals = []
        yvals = []
        
        theta = math.radians(degrees)
        trans_matrix = np.array([[math.cos(theta), -math.sin(theta)], \
                                 [math.sin(theta), math.cos(theta)]])
        
        for i in range(len(self.nodes)):
            x_y = np.array(self.nodes[i])
            trans = np.dot(x_y, trans_matrix)
            xvals.append(trans[0])
            yvals.append(trans[1])
        
        xvals.append(xvals[0])
        yvals.append(yvals[0])
        
        plt.plot(xvals, yvals, linestyle = '--')
        
    def reflect(self, slope, c = 0):
        xvals = []
        yvals = []
        for i in range(len(self.nodes)):
            x = self.nodes[i][0]
            y = self.nodes[i][1]
            d = (x + (y - c)*slope)/(1 + slope**2)
            x_trans = 2*d - x
            y_trans = 2*d*slope - y + 2*c
            xvals.append(x_trans)
            yvals.append(y_trans)
        
        xvals.append(xvals[0])
        yvals.append(yvals[0])
        
        print xvals, yvals
        plt.plot(xvals, yvals, linestyle = '--')
    
    
        
    def dilate(self, point, scale_factor):
        xvals = []
        yvals = []
        for i in self.nodes:
            xmap = (i[0] - point[0])*scale_factor
            xvals.append(point[0] + xmap)
            ymap = (i[1] - point[1])*scale_factor
            yvals.append(point[1] + ymap)
        xvals.append(point[0] + ((self.nodes[0][0] - point[0])*scale_factor))
        yvals.append(point[1] + ((self.nodes[0][1] - point[1])*scale_factor))
        plt.plot(xvals, yvals, 'o')
        plt.plot(xvals, yvals, linestyle = '--')
    
            
    
        
         
