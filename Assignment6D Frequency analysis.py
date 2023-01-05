## Assignment6D Frequency analysis
import string

import numpy as np
import os
"""
This script is used to take a text file as input and return a vector of size 26 with the frequency in percent of each
character a,b,...z. The frequency must be computed as the number of occurences divided by the total number of characters from
a to z that occur, multiplied by one hundred.
"""
def letterFrequency(filename):
    """
    :param filename: A string that is the filename of a plain text file in the current working directory
    :return: freq: A vector of length 26 containing the frequency of occurrence of each of the 26 letters from a to z
    """
    filein = open(filename,'r')  # Opens the file for reading
    lines = filein.readlines()  # Reads all lines into an array
    smalltxt = ''.join(lines)    ## covert the text to lower case only consider a to z
    smalltxt = smalltxt.lower()
    letters = [chr(i) for i in range(97,123)] # use ascll get 26 letters
    count = np.zeros(len(letters))
    total = 0
    for i in range(len(letters)):
        for j in range(len(smalltxt)):
            if letters[i] == smalltxt[j]:
                count[i] = count[i] + 1
                total = total+1  # count how many words the string have
    freq = count/total*100
    return freq

if __name__ == '__main__':
    print(letterFrequency('small_text.txt'))