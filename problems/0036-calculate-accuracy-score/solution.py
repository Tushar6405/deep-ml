import numpy as np

def accuracy_score(y_true, y_pred):
	# Your code here
	return float(np.mean(np.array(y_true) == np.array(y_pred)))