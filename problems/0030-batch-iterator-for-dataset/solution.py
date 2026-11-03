import numpy as np

def batch_iterator(X, y=None, batch_size=64):
	# Your code here
	X = np.array(X)
	batches = []
	for i in range(0, len(X), batch_size):
		if y is not None:
			batches.append([X[i:i + batch_size], np.array(y)[i:i + batch_size]])
		else:
			batches.append(X[i:i + batch_size])
	return batches