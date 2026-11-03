import numpy as np
def solve_jacobi(A: np.ndarray, b: np.ndarray, n: int) -> list:
	A, b = np.array(A, dtype=float), np.array(b, dtype=float)
	x = np.zeros(len(b))
	for _ in range(n):
		x_new = np.zeros_like(x)
		for i in range(len(b)):
			s = np.dot(A[i], x) - A[i, i] * x[i]
			x_new[i] = (b[i] - s) / A[i, i]
		x = np.round(x_new, 4)
	return x.tolist()