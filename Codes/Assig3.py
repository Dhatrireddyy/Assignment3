# CBSE Probability Grade 10
# Exercise 15.1 Q13

# Name: Velma Dhatri Reddy
# Roll number: AI21BTECH11030

""" Problem Statement
A die is thrown once. Find the probability of getting
(i) a prime number
(ii) a number lying between 2 and 6
(iii) an odd number
"""
#Create a PMF and CDF subplot for a single die roll

def line_gen(A,B):
    len =10
    dim = A.shape[0]
    x_AB = np.zeros((dim,len))
    lam_1 = np.linspace(0,1,len)
    for i in range(len):
        temp1 = A + lam_1[i]*(B-A)
        x_AB[:,i]= temp1.T
    return x_AB

#Function for batch usage of line_gen
def batch_plot(A, B):
    len = A.shape[0]
    for i in range(len):
        x_AB = line_gen(A[i, :], B[i, :])
        plt.plot(x_AB[0, :], x_AB[1, :], 'k-')

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import stem

#Arrays for PMF
X = np.array([1, 2, 3, 4, 5, 6])
Y = np.array([1/6, 1/6, 1/6, 1/6, 1/6, 1/6])
Z = np.cumsum(Y)

#Plotting the PMF
plt.subplot(1, 2, 1)
plt.xlabel('Value of X')
plt.ylabel('Probability Mass Function')
plt.xticks(X)
stem(X, Y, linefmt='k-', markerfmt='ko', basefmt='k-')

#Plotting the CDF
plt.subplot(1, 2, 2)
stem(X, Z, linefmt='k-', markerfmt='ko', basefmt='k-')
plt.xlabel('Value of X')
plt.ylabel('Cumulative Probability')
plt.xticks(X)
plt.grid()
plt.tight_layout() #Space the subplots properly
plt.savefig('/Users/dhatrireddy/Desktop/3_1')