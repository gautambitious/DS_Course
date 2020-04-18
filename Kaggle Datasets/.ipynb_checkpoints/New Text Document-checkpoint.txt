import numpy as np
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt

class CustomLogisticRegression:
    
    def __init__(self, lr=0.1, max_iters=20):
        self.lr=lr
        self.max_iters=max_iters
    
    def fit(self, X, y):
        X = np.hstack([np.ones((X.shape[0], 1)), X])
        self.theta_ = np.random.randn(X.shape[1], 1)
        
        for _ in range(self.max_iters):
            self.gradient_accend(X, y)
        self.intercept_ = self.theta_[0]
        self.coef_ = self.theta_[1:] 
    def gradient_accend(self,X,y):
        delta_theta = self.gradient(X,y)
        self.theta_+= delta_theta
    def gradient(self, X, y):
        yh = self.sigmoid(X)
        ya = y.reshape(-1,1)
        diff = (yh-ya)
        delta = np.dot(X.T, diff)/len(X)
        return -delta*self.lr
    def sigmoid(self, X):
        g = np.dot(X, self.theta_)
        return 1/(1+np.exp(-g))