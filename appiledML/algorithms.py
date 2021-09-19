import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def hypothesis(X,theta):
    return np.dot(X,theta)

def computeCost(X,y,theta):
    m=len(y)
    # predictions=X.dot(theta)
    predictions = hypothesis(X,theta)
    predictions = np.sum(predictions,axis = 1)
    square_err=(predictions - y)**2
    return 1/(2*m) * np.sum(square_err)

def gradientdescent(X,y,theta,alpha,i):
    J = []  #cost function in each iterations
    k = 0
    m = len(y)
    alpha=float(alpha)
    while k < i:        
        pred = hypothesis(X,theta)
        pred = np.sum(pred, axis=1)
        for c in range(0, len(X.columns)):
            val = theta[c] - (alpha*(sum((pred-y)*X.iloc[:,c])/m))
            print(val)
            theta[c] = val
        j = computeCost(X, y, theta)
        print(j)
        J.append(j)
        k += 1
    return J, theta