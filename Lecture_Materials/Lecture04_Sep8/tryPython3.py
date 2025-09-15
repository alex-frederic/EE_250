# Step 1: Importing the NumPy library
import numpy as np

print("Welcome to the NumPy tutorial!")

# Step 2: Creating arrays
print("\n--- Creating Arrays ---")
# Create a 1D array (vector)
vector = np.array([1, 2, 3, 4, 5])
print(f"1D Array (Vector): {vector}")

# Create a 2D array (matrix)
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(f"\n2D Array (Matrix):\n{matrix}")

# Create arrays with special functions
zeros = np.zeros((2, 3))  # 2x3 matrix filled with zeros
print(f"\nMatrix of Zeros:\n{zeros}")

ones = np.ones((3, 2))  # 3x2 matrix filled with ones
print(f"\nMatrix of Ones:\n{ones}")

identity = np.eye(3)  # 3x3 identity matrix
print(f"\nIdentity Matrix:\n{identity}")

# Step 3: Array Properties
print("\n--- Array Properties ---")
print(f"Shape of matrix: {matrix.shape}")
print(f"Size of matrix (total elements): {matrix.size}")
print(f"Data type of elements: {matrix.dtype}")

# Step 4: Basic Operations
print("\n--- Basic Operations ---")
# Add arrays
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(f"Array A: {a}")
print(f"Array B: {b}")
print(f"A + B: {a + b}")  # Element-wise addition
print(f"A * B: {a * b}")  # Element-wise multiplication

# Scalar operations
print(f"A * 2: {a * 2}")  # Multiply all elements by 2

# Dot product of two vectors
dot_product = np.dot(a, b)
print(f"Dot Product of A and B: {dot_product}")

# Step 5: Transpose
print("\n--- Transpose ---")
print(f"Original Matrix:\n{matrix}")
print(f"Transposed Matrix:\n{matrix.T}")

# Step 6: Indexing and Slicing
print("\n--- Indexing and Slicing ---")
print(f"Element at row 1, column 2: {matrix[0, 1]}")  # 1st row, 2nd column
print(f"First row: {matrix[0, :]}")  # All columns of the first row
print(f"First column: {matrix[:, 0]}")  # All rows of the first column
print(f"Sub-matrix (rows 1-2, cols 1-2):\n{matrix[0:2, 0:2]}")  # Top-left 2x2 sub-matrix

# Step 7: Reshaping
print("\n--- Reshaping ---")
reshaped = matrix.reshape(1, 9)  # Convert 3x3 to 1x9
print(f"Reshaped Matrix (1x9):\n{reshaped}")

# Step 8: Mathematical Functions
print("\n--- Mathematical Functions ---")
values = np.array([1, 2, 3, 4, 5])
print(f"Values: {values}")
print(f"Square root: {np.sqrt(values)}")
print(f"Exponential: {np.exp(values)}")
print(f"Logarithm: {np.log(values)}")

# Step 9: Random Numbers
print("\n--- Random Numbers ---")
random_array = np.random.rand(3, 3)  # 3x3 matrix of random numbers (0 to 1)
print(f"Random Array:\n{random_array}")

random_integers = np.random.randint(1, 10, size=(2, 3))  # Random integers between 1 and 9
print(f"Random Integers (2x3):\n{random_integers}")

# Step 10: Aggregation Functions
print("\n--- Aggregation Functions ---")
print(f"Matrix:\n{matrix}")
print(f"Sum of all elements: {matrix.sum()}")
print(f"Mean of all elements: {matrix.mean()}")
print(f"Maximum value: {matrix.max()}")
print(f"Minimum value: {matrix.min()}")

# Step 11: Boolean Indexing
print("\n--- Boolean Indexing ---")
print(f"Matrix:\n{matrix}")
print(f"Elements greater than 5:\n{matrix[matrix > 5]}")  # Filters elements greater than 5

# Step 12: Broadcasting
print("\n--- Broadcasting ---")
scalar = 10
print(f"Original Matrix:\n{matrix}")
print(f"Matrix + Scalar (10):\n{matrix + scalar}")  # Adds 10 to each element

# Final Message
print("\nThank you for following this NumPy tutorial!")
