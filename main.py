import numpy as np


def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def find_smallest_prime(matrix):
    n = matrix.shape[0]
    min_prime = None
    min_prime_positions = []

    for i in range(n):
        for j in range(i + 1, n):
            if is_prime(matrix[i, j]):
                if min_prime is None or matrix[i, j] < min_prime:
                    min_prime = matrix[i, j]
                    min_prime_positions = [(i, j)]
                elif matrix[i, j] == min_prime:
                    min_prime_positions.append((i, j))

    return min_prime, min_prime_positions


def delete_rows_columns(matrix, positions):
    rows_to_delete = {pos[0] for pos in positions}
    cols_to_delete = {pos[1] for pos in positions}

    new_matrix = np.delete(matrix, list(rows_to_delete), axis=0)
    new_matrix = np.delete(new_matrix, list(cols_to_delete), axis=1)

    return new_matrix


# Приклад використання
matrix = np.array([
    [10, 6, 17, 4],
    [5, 6, 6, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
])

min_prime, positions = find_smallest_prime(matrix)

indices_correct = [(i+1, j+1) for i, j in positions]

if min_prime is not None:
    print(f"Найменше просте число: {min_prime}")
    print(f"Індекси елементів зі значенням {min_prime}: {indices_correct}")
    new_matrix = delete_rows_columns(matrix, positions)
    print("Матриця після видалення рядків і стовпців:")
    print(new_matrix)
else:
    print("таких нема!")
