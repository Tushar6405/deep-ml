import numpy as np

def shuffle_data(X, y, seed=None):
	# Your code here
	X, y = np.array(X), np.array(y)
	if seed is not None:
		np.random.seed(seed)
	idx = np.random.permutation(len(X))
	return X[idx], y[idx]