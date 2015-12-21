# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from __future__ import division
import math
from sympy import *
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

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
        for i in self.nodes:
            xdiff = point[0] - i[0]
            ydiff = point[1] - i[1]
            if degrees == 90:
                xvals.append(point[0] + ydiff)
                yvals.append(point[1] - xdiff)
            elif degrees == 180:
                xvals.append(point[0] + xdiff)
                yvals.append(point[1] + ydiff)
            elif degrees == 270:
                xvals.append(point[0] - ydiff)
                yvals.append(point[1] + xdiff)
            else:   
                xvals.append(point[0] - xdiff)
                yvals.append(point[1] - ydiff)
        if degrees == 90:
            xvals.append(point[0] + (point[1] - self.nodes[0][1]))
            yvals.append(point[1] - (point[0] - self.nodes[0][0]))
        elif degrees == 180:
            xvals.append(point[0] + (point[0] - self.nodes[0][0]))
            yvals.append(point[1] + (point[1] - self.nodes[0][1]))
        elif degrees == 270:
            xvals.append(point[0] - (point[1] - self.nodes[0][1]))
            yvals.append(point[1] + (point[0] - self.nodes[0][0]))
        else:   
            xvals.append(point[0] - (point[0] - self.nodes[0][0]))
            yvals.append(point[1] - (point[1] - self.nodes[0][1]))
        plt.plot(xvals, yvals, 'o')
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


        

        
        
    
    