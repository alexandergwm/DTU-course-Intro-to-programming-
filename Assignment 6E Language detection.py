### Assignment 6E Language detection

import numpy as np
import os

import pandas

"""
This script is used to compute the squared error between the frequencies in the text and the frequencies in the language
"""
def computeLanguageError(freq):
    """
    This function takes as input a vector of frequencies of occurrences of letters in a text
    :param freq:  A vector of size 26 containing the frequency of the letters a-z in a text
    :return: A vector of length 15 containing the squared error between the input vector and each of 15 languages in the CSV file
    """
    letter_frequencies = pandas.read_csv('letter_frequencies.csv')
    letters = np.array(letter_frequencies.Letter)

    # For each language to extract the frequencies of word
    # Get the number of languages of the CSV file
    num = np.size(letter_frequencies) / len(letter_frequencies)
    num = int(num) - 1
    languages = np.zeros([num,len(letter_frequencies)])
    # print(languages)
    for i in range(num):  # Traversing all the languages
        languages[i] = letter_frequencies.iloc[:,i+1]
    # The matrix stored languages is got

    # Calculate the squared error
    sum = np.zeros(num)
    for j in range(num):
        for i in range(len(letter_frequencies)):
            SE = (freq[i] - languages[j,i])**2
            sum[j] = sum[j] + SE
    return sum


