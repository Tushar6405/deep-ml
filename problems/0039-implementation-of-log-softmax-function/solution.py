import numpy as np

def log_softmax(scores: list) -> np.ndarray:
	# Your code here
	s = np.array(scores, dtype=float)
	s = s - np.max(s)
	result = s - np.log(np.sum(np.exp(s)))
	return np.round(result, 4).tolist()