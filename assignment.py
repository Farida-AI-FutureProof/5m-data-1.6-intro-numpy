import numpy as np

print("✅ NumPy Demo Started\n")

# 1. Array creation
arr1 = np.array([10, 20, 30, 40, 50])
arr2 = np.arange(1, 11)   # 1 to 10
arr3 = np.linspace(0, 1, 5) # even spacing
print("arr1:", arr1)
print("arr2:", arr2)
print("arr3:", arr3, "\n")

# 2. Reshape & indexing
matrix = np.arange(1, 13).reshape(3, 4)
print("Matrix (3x4):\n", matrix)
print("Element [1, 2]:", matrix[1, 2])
print("Second row:", matrix[1, :])
print("Last column:", matrix[:, -1], "\n")

# 3. Vectorized operations
print("arr2 * 2 →", arr2 * 2)
print("arr2 ** 2 →", arr2 ** 2)
print("arr2 + 5 →", arr2 + 5, "\n")

# 4. Broadcasting
matrix2 = matrix + 10
print("Matrix + 10 →\n", matrix2, "\n")

# 5. Aggregations
print("Sum:", np.sum(matrix))
print("Mean:", np.mean(matrix))
print("Max:", np.max(matrix))
print("Min:", np.min(matrix))
print("Std Dev:", np.std(matrix), "\n")

# 6. Boolean filtering
even = arr2[arr2 % 2 == 0]
print("Even numbers from arr2:", even, "\n")

# 7. Random arrays & seed
np.random.seed(42)
rand = np.random.randint(1, 100, (3, 3))
print("Random Matrix:\n", rand)
print("Row means:", rand.mean(axis=1))
print("Column sums:", rand.sum(axis=0), "\n")

print("✅ NumPy Demo Completed")
