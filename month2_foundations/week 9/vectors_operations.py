def add_vectors(v1, v2):
    if len(v1) != len(v2):
        return "Vectors must be the same length."

    result = []

    for i in range(len(v1)):
        result.append(v1[i] + v2[i])

    return result

def scalar_multiply(vector, scalar):
    if not isinstance(scalar, (int, float)):
        return "Scalar must be a number."

    result = []

    for i in range(len(vector)):
        result.append(vector[i] * scalar)

    return result

def print_matrix(matrix):
    for row in matrix:
        print(row)

def add_vectors(v1, v2):
    if len(v1) != len(v2):
        return "Vectors must be the same length."

    result = []

    for i in range(len(v1)):
        result.append(v1[i] + v2[i])

    return result


def scalar_multiply(vector, scalar):
    if not isinstance(scalar, (int, float)):
        return "Scalar must be a number."

    result = []

    for i in range(len(vector)):
        result.append(vector[i] * scalar)

    return result


def print_matrix(matrix):
    for row in matrix:
        print(row)


def add_vectors(v1, v2):
    if len(v1) != len(v2):
        return "Vectors must be the same length."

    result = []

    for i in range(len(v1)):
        result.append(v1[i] + v2[i])

    return result

def subtract_vectors(v1, v2):
    if len(v1) != len(v2):
        return "Vectors must be of the same length."
    result = []
    for i in range(len(v1)):
        result.append(v1[i] - v2[i])
    return result

def scalar_multiply(vector, scalar):
    if not isinstance(scalar, (int, float)):
        return "Scalar must be a number."

    result = []

    for i in range(len(vector)):
        result.append(vector[i] * scalar)

    return result


def print_matrix(matrix):
    for row in matrix:
        print(row)


print("=== VECTOR ADDITION ===")
print("Example 1:", add_vectors([2, 3], [4, 5]))
print("Example 2:", add_vectors([1, 2, 3], [4, 5, 6]))
print("Example 3:", add_vectors([10, 20], [30, 40]))
print("Error Case:", add_vectors([1, 2], [3, 4, 5]))

print()

print("=== VECTOR SUBTRACTION ===")
print("Example 1:", subtract_vectors([5, 7], [2, 3]))
print("Error Case:", subtract_vectors([1, 2], [3, 4, 5]))

print()

print("=== SCALAR MULTIPLICATION ===")
print("Example 1:", scalar_multiply([2, 4], 3))
print("Example 2:", scalar_multiply([1, 2, 6], -0.5))
print("Example 3:", scalar_multiply([5, 10], 2))
print("Error Case:", scalar_multiply([1, 2], "no number here"))

print()

print("=== MATRIX DISPLAY ===")
matrix = [
    [10, 20, 30],
    [40, 50, 60]
]

print_matrix(matrix)

def matrix_size(matrix):
    return len(matrix), len(matrix[0])

print("Matrix size:", matrix_size(matrix)) # Output: (2, 3) = 2 rows and 3 columns
