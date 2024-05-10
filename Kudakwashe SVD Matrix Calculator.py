def dot_product(vector1, vector2):
    return sum(x * y for x, y in zip(vector1, vector2))

def matrix_transpose(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

def matrix_multiply(matrix1, matrix2):
    return [[sum(a * b for a, b in zip(row, col)) for col in zip(*matrix2)] for row in matrix1]

def eigen(matrix):
    # Basic eigenvalue decomposition method for 2x2 matrices
    a, b, c, d = matrix[0][0], matrix[0][1], matrix[1][0], matrix[1][1]
    trace = a + d
    det = a * d - b * c
    discriminant = (trace ** 2) - 4 * det

    if discriminant < 0:
        # Complex eigenvalues, not handled in this basic method
        raise ValueError("Complex eigenvalues not supported")
    else:
        eigenvalue1 = (trace + discriminant ** 0.5) / 2
        eigenvalue2 = (trace - discriminant ** 0.5) / 2

    eigenvector1 = [b, eigenvalue1 - a]
    eigenvector2 = [b, eigenvalue2 - a]

    # Ensure the first element of each eigenvector is positive
    if eigenvector1[0] < 0:
        eigenvector1 = [-eigenvector1[0], -eigenvector1[1]]
    if eigenvector2[0] < 0:
        eigenvector2 = [-eigenvector2[0], -eigenvector2[1]]

    return [eigenvalue1, eigenvalue2], [eigenvector1, eigenvector2[::-1]]  # Reverse the order of eigenvectors

def svd(A):
    m, n = len(A), len(A[0])
    
    # Step 1: Compute A^T * A
    ATA = matrix_multiply(matrix_transpose(A), A)
    
    # Step 2: Compute eigenvalues and eigenvectors of A^T * A
    eigenvalues, eigenvectors = eigen(ATA)
    
    # Step 3: Compute singular values
    singular_values = [eigenvalue ** 0.5 for eigenvalue in eigenvalues]
    
    # Step 4: Compute V matrix
    V = eigenvectors
    
    # Step 5: Compute U matrix
    U = matrix_multiply(A, eigenvectors)
    
    return U, singular_values, V

# Example usage
m = int(input("Enter the number of rows (m): "))
n = int(input("Enter the number of columns (n): "))

matrix = []
for _ in range(m):
    row = []
    for _ in range(n):
        row.append(float(input(f"Enter element {len(row)+1} of row {_+1}: ")))
    matrix.append(row)

U, singular_values, V = svd(matrix)

print("\nU matrix:")
for row in U:
    print(row)

print("\nSingular values:")
print(singular_values)

print("\nV matrix:")
for row in V:
    print(row)




