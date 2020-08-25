import numpy as np


inputs =np.array([[-1,-1],[-1,1],[1,-1] ,[1,1]])

w1 =.5
w2 =.5
th = -.5


for input in inputs:
    sum = input[0]*w1 + input[1]*w2 + th
    if sum >= 0:
        print(" %d , %d, output %d" % (input[0],input[1], 1))
    else:
        print(" %d , %d, output %d" % (input[0], input[1], -1))




