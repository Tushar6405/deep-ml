def determinant_4x4(matrix: list[list[int|float]]) -> float:
	# Your recursive implementation here
	def det(m):
		n = len(m)
		if n == 1:
			return m[0][0]
		if n == 2:
			return m[0][0] * m[1][1] - m[0][1] * m[1][0]
		total = 0
		for j in range(n):
			minor = [row[:j] + row[j + 1:] for row in m[1:]]
			total += ((-1) ** j) * m[0][j] * det(minor)
		return total
	return det(matrix)