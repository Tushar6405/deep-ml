def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
	# Your code here
	n_f = len(vectors)
	n_o = len(vectors[0])
	means = [sum(v) / n_o for v in vectors]
	cov = [[0.0] * n_f for _ in range(n_f)]
	for i in range(n_f):
		for j in range(n_f):
			cov[i][j] = sum((vectors[i][k] - means[i]) * (vectors[j][k] - means[j]) for k in range(n_o)) / (n_o - 1)

	return cov
