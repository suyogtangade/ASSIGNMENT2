# -*- coding: utf-8 -*-
"""Untitled7.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fbIDAzy-M8lFha9KFMzg3ed57kYlYrbj
"""

import numpy as np
import matplotlib.pyplot as plt
import math 
from numpy import linalg as LNG

A = np.array([4,-7])
B = np.array([-1,5])
# Reading co-ordinates
A=np.array([4,-7])
B=np.array([-1,5])
P=np.linalg.norm(B-A)
print(P)


#Generate line points
def line_gen(A,B):
  len =10
  x_AB = np.zeros((2,len))
  lam_1 = np.linspace(0,1,len)
  for i in range(len):
    temp1 = A + lam_1[i]*(B-A)
    x_AB[:,i]= temp1.T
  return x_AB


def xang(A,B):
    theta = (B[1]-A[1])/(B[0]-A[0])
    arctan = np.arctan(theta)
    arctan *= (180/3.14)
    if arctan < 0:
        arctan = 180 + arctan
    return math.ceil(arctan)

x_AB = line_gen(A,B)
plt.plot(x_AB[0,:],x_AB[1,:],label="line")
print("Angle between line and x-axis",xang(A,B),"degree")

plt.plot(4,-7,'o')
plt.plot(-1,5,'o')

plt.xlabel('$x$')
plt.ylabel('$y$')

plt.text(4,-7,'A(4,-7)')
plt.text(-1,5,'B(-1,5)')



plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')

#if using termux
plt.savefig('distance.png')
#subprocess.run(shlex.split("termux-open ./line/figs/line_check_sol.pdf"))
#else
plt.show()

"""# New section"""

