import numpy as np


matrix = np.array([[2,3],[7,11]])
vector = np.array([[5],[13]])

print(f'A = {matrix}')

determiant = np.linalg.det(matrix)

print(f'det(A) = {determiant}')
inverse = np.linalg.inv(matrix)
print(f'A^-1 = {inverse}')

solution = np.matmul(inverse, vector)
print(f'x = {solution}')

fast_solution = np.linalg.solve(matrix, vector)
print(f' = {fast_solution}')