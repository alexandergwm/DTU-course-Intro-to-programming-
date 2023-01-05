### Assignment 6C Moving average
import numpy as np
"""
This script is used to take a signal vector as input and compute the five-sample weighted moving average of the signal
it smoothes the signal by n-sample symmetric weighted moving average  i.e. weighted average of the surrounding
Input: y input signal (vector)
Output: ysmooth Five-sample moving average smoothing of input signal (vector)
"""
def movingAvg(y):
    N = len(y)  # get the length of input array
    # Build the matrix by shifting the array
    # initial a matrix with dimensions[len(y),5]
    matrix = np.zeros((5,len(y)))
    # print(matrix[0,:])
    # build a new zero matrix to store all the array including shifting and origin
    y1 = np.zeros(len(y)+4)
    y1[2:len(y)+2] = y
    # print(y1)
    # value i is from (-2,2),i.e. the distance of shifting,‘-’ is left shift，‘+' is right shift
    for i,j in zip(range(-2,3,1),range(4,-1,-1)):
           # the shifted versiion of the signal
           matrix[i+2,:] = y1[j:j+len(y)]
           # the scaled version of the signal
           if i <= 0:
               matrix[i+2,:] = (3+i) * matrix[i+2,:]
           else:
               matrix[i+2,:] = (3-i) * matrix[i+2,:]
           # compute the mean of each column
    sum_column = np.sum(matrix,axis = 0)
    ysmooth = sum_column/9
    return ysmooth


