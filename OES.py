import numpy as np
X = np.array([ [0,0,1],[0,1,1],[1,0,1],[1,1,1] ])
Y = np.array([[0,1,1,0]]).T
ALPHA,HIDDEN_dim = (0.5,4)
sin_0 = 2*np.random.random((3,HIDDEN_dim)) - 1
sin_1 = 2*np.random.random((HIDDEN_dim,1)) - 1
for a in range(1):
    level_0 = 1/(1+np.exp(-(np.dot(X,sin_0))))
    level_1 = 1/(1+np.exp(-(np.dot(level_0,sin_1))))
    for b in range(60000):
        level_1_delta = (level_1 - Y)*(level_1*(1-level_1))
        level_0_delta = level_1_delta.dot(sin_1.T) * (level_0 * (1-level_0))
    sin_1 -= (ALPHA * level_0.T.dot(level_1_delta))
    sin_0 -= (ALPHA * X.T.dot(level_0_delta))
    
print(level_1)
