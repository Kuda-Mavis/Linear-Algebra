def dot_product(v1, v2):
    return sum(x * y for x, y in zip(v1, v2))

def scalar_multiply(scalar, vector):
    return [scalar * x for x in vector]

def subtract_vectors(v1, v2):
    return [x - y for x, y in zip(v1, v2)]

def normalize_vector(vector):
    magnitude = (sum(x ** 2 for x in vector)) ** 0.5
    return [x / magnitude for x in vector]

def transpose(matrix):
    return [[row[i] for row in matrix] for i in range(len(matrix[0]))]

def qr_decomposition(matrix):
    m = len(matrix)
    n = len(matrix[0])
    q = []
    r = [[0] * n for _ in range(n)]

    for j in range(n):
        v = matrix[j]
        for i in range(j):
            r[i][j] = dot_product(q[i], matrix[j])
            v = subtract_vectors(v, scalar_multiply(r[i][j], q[i]))
        r[j][j] = (sum(x ** 2 for x in v)) ** 0.5
        q.append(normalize_vector(v))

    return q, r

def print_matrix(matrix):
    for row in matrix:
        print(row)

def main():
    m = int(input("Enter the number of rows (m): "))
    n = int(input("Enter the number of columns (n): "))

    matrix = []
    print(f"Enter the {m * n} entries of the matrix:")
    for _ in range(m):
        row = [float(input()) for _ in range(n)]
        matrix.append(row)

    q, r = qr_decomposition(matrix)

    print("\nQ matrix:")
    print_matrix(q)

    print("\nR matrix:")
    print_matrix(r)

if __name__ == "__main__":
    main()

