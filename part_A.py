"""
TECH2 mandatory assignment - Part A

Write the implementation of part A of the exercise below.
"""
from math import sqrt

def std_loops(x):
    """
    Compute standard deviation of x using loops.

    Parameters
    ----------
    x: Sequence of numbers

    Returns
    -------
    sd : float
        Standard deviation of the list of numbers.
    """
    sum1 = 0
    sum2 = 0
    length = 0
    
    for i in x:
        sum1 = sum1 + i         #Summing up the values
        sum2 = sum2 + i ** 2    #Summing up the values squared
        length = length + 1     #Counting the number of values
        
    mean = sum1 / length        #Calculating the mean
    
    S = sum2 / length           #Calcultating the mean of squares
    
    var = S - mean ** 2         #Calculating the variance
    
    sd = sqrt(var)              #Calculating the standard deviation
    
    return sd
       
num_lst = [1, 2, 3, 4, 5]       #Defining the list of numbers the program goes through
std_dev = std_loops(num_lst)
print(f'The standard deviation, using method 1, is {std_dev:.2f}')


import numpy as np  

def std_builtin(x):
    """
    Compute standard deviation of x using the built-in functions sum()
    and len().

    Parameters
    ----------
    x: Sequence of numbers

    Returns
    -------
    sd : float
        Standard deviation of the list of numbers.
    """
    sum1 = sum(x)                   #Summing the values
    x_squared = np.array(x) ** 2    #Squaring the values, by using an array
    sum2 = np.sum(x_squared)        #Summing the values squared
    
    mean = sum1 / len(x)            #Calculating the mean
    
    S = sum2 / len(x)               #Calculating the mean of squares
    
    var = S - mean ** 2             #Calculating the variance
    
    sd = sqrt(var)                  #Calculating the standard deviation
    
    return sd
       
num_lst = [1, 2, 3, 4, 5]           #Defining the list of numbers the program goes through
std_dev = std_builtin(num_lst)
print(f'The standard deviation, using method 2, is {std_dev:.2f}')

    
print(f'The standard deviation, using method 3, is {np.std(num_lst):.2f}')

    