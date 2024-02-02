import numpy as np
# Task 1
import numpy as np


# def generate_matrix():
#     m, n = map(int, input("Введіть m та n через пробіл: ").split())
#
#     matrix = np.zeros((n, m), dtype=int)
#
#     matrix[0, :] = np.arange(m)
#
#     print("Згенерована матриця:")
#     print(matrix)
#
#
# generate_matrix()


# def generate_matrix_iterator():
#     m, n = map(int, input("Введіть m та n через пробіл: ").split())
#
#     matrix = []
#
#     matrix.append(list(range(m)))
#
#     for _ in range(1, n):
#         matrix.append([0] * m)
#
#     print("Згенерована матриця:")
#     for row in matrix:
#         print(row)
#
#
# generate_matrix_iterator()


# def solve_system(matrix_A, vector_B):
#     det_A = np.linalg.det(matrix_A)
#
#     solution = []
#
#     for i in range(len(vector_B)):
#         temp_matrix = np.copy(matrix_A)
#
#         temp_matrix[:, i] = vector_B.copy()
#
#         det_temp = np.linalg.det(temp_matrix)
#
#         solution.append(det_temp / det_A)
#
#     return np.array(solution)
#
#
# def check_solution(matrix_A, vector_B, solution):
#     result = np.dot(matrix_A, solution)
#
#     print("Перевірка розв'язку:")
#     print("Матриця A * Розв'язок:")
#     print(result)
#     print("Вектор B:")
#     print(vector_B)
#
#
# def check_solution_inverse(matrix_A, vector_B, solution):
#     inverse_A = np.linalg.inv(matrix_A)
#     result_inverse = np.dot(inverse_A, vector_B)
#
#     print("Перевірка розв'язку за допомогою оберненої матриці:")
#     print("Обернена матриця A:")
#     print(inverse_A)
#     print("Обернена матриця A * Вектор B:")
#     print(result_inverse)
#
#
# def check_solution_numpy_solve(matrix_A, vector_B):
#     result_solve = np.linalg.solve(matrix_A, vector_B)
#
#     print("Перевірка розв'язку за допомогою numpy.linalg.solve():")
#     print("Розв'язок за допомогою solve():")
#     print(result_solve)
#
#
# def compare_solutions(solution1, solution2, solution3):
#     if np.allclose(solution1, solution2) and np.allclose(solution1, solution3):
#         print("Всі розв'язки ідентичні.")
#     else:
#         print("Розв'язки відрізняються.")
#
#
#
# def task_SLE():
#     try:
#         matrix_A = np.array([
#             [0, 1, -3, 4],
#             [1, 0, -2, 3],
#             [3, 2, 0, -5],
#             [4, 3, -5, 0]
#         ], dtype=np.float64)
#
#         vector_B = np.array([-5, -4, 12, 5], dtype=np.float64)
#
#
#         solution = solve_system(matrix_A, vector_B)
#
#         print("Розв'язок системи:")
#         print(solution)
#
#         check_solution(matrix_A, vector_B, solution)
#
#         check_solution_inverse(matrix_A, vector_B, solution)
#
#         check_solution_numpy_solve(matrix_A, vector_B)
#
#
#         compare_solutions(solution, check_solution_inverse(matrix_A, vector_B, solution),
#                           check_solution_numpy_solve(matrix_A, vector_B))
#
#     except Exception as e:
#         print(f"Помилка виконання: {str(e)}")
#
# task_SLE()

# def task_3_numpy():
#     A = np.array([[7, 2, 0],
#                    [-7, -2, 1],
#                    [1, 1, 0]])
#
#     B = np.array([[0, 2, 3],
#                    [1, 0, -2],
#                    [3, 1, 1]])
#
#     result = (A*A - B*B) * (A+B)
#
#     print(result)
#
# task_3_numpy()


def plus_matrix(matrix_a, matrix_b):
    result = []
    for i in range(len(matrix_a)):
        row = []
        for j in range(len(matrix_a[0])):
            row.append(matrix_a[i][j] + matrix_b[i][j])
        result.append(row)
    return result

def subtract_matrix(matrix_a, matrix_b):
    result = []
    for i in range(len(matrix_a)):
        row = []
        for j in range(len(matrix_a[0])):
            row.append(matrix_a[i][j] - matrix_b[i][j])
        result.append(row)
    return result

def multiply_matrix(matrix_a, matrix_b):
    result = []
    for i in range(len(matrix_a)):
        row = []
        for j in range(len(matrix_b[0])):
            sum = 0
            for k in range(len(matrix_b)):
                sum += matrix_a[i][k] * matrix_b[k][j]
            row.append(sum)
        result.append(row)
    return result

A = [[7, 2, 0],
    [-7, -2, 1],
    [1, 1, 0]]

B = [[0, 2, 3],
    [1, 0, -2],
    [3, 1, 1]]

A2=multiply_matrix(A,A)
B2=multiply_matrix(B,B)
A2subB2=subtract_matrix(A2,B2)
AplusB=plus_matrix(A,B)
result = multiply_matrix(A2subB2,AplusB)

for row in result:
    print(row)