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


# def plus_matrix(matrix_a, matrix_b):
#     result = []
#     for i in range(len(matrix_a)):
#         row = []
#         for j in range(len(matrix_a[0])):
#             row.append(matrix_a[i][j] + matrix_b[i][j])
#         result.append(row)
#     return result
#
# def subtract_matrix(matrix_a, matrix_b):
#     result = []
#     for i in range(len(matrix_a)):
#         row = []
#         for j in range(len(matrix_a[0])):
#             row.append(matrix_a[i][j] - matrix_b[i][j])
#         result.append(row)
#     return result
#
# def multiply_matrix(matrix_a, matrix_b):
#     result = []
#     for i in range(len(matrix_a)):
#         row = []
#         for j in range(len(matrix_b[0])):
#             sum = 0
#             for k in range(len(matrix_b)):
#                 sum += matrix_a[i][k] * matrix_b[k][j]
#             row.append(sum)
#         result.append(row)
#     return result
#
# A = [[7, 2, 0],
#     [-7, -2, 1],
#     [1, 1, 0]]
#
# B = [[0, 2, 3],
#     [1, 0, -2],
#     [3, 1, 1]]
#
# A2=multiply_matrix(A,A)
# B2=multiply_matrix(B,B)
# A2subB2=subtract_matrix(A2,B2)
# AplusB=plus_matrix(A,B)
# result = multiply_matrix(A2subB2,AplusB)
#
# for row in result:
#     print(row)


# def create_chessboard_matrix(n):
#     chessboard = np.zeros((n, n), dtype=int)
#     chessboard[1::2, ::2] = 1
#     chessboard[::2, 1::2] = 1
#     return chessboard
#
# print(create_chessboard_matrix(5))


# def create_chessboard_matrix(n):
#     chessboard = [[0] * n for _ in range(n)]
#     for i in range(n):
#         for j in range(n):
#             if (i + j) % 2 == 1:
#                 chessboard[i][j] = 1
#     return chessboard
#
#
# for row in  create_chessboard_matrix(5):
#     print(row)

# def create_array_with_ones(n):
#     array = np.zeros((n, n), dtype=int)
#     array[:, ::2] = 1
#     return array
#
# print(create_array_with_ones(5))
#
# def create_array_with_ones(n):
#     array = [[1 if i % 2 == 0 else 0 for i in range(n)] for _ in range(n)]
#     return array
#
# for row in create_array_with_ones(5):
#     print(row)


# def count_zeros_nonzeros(array):
#     zeros_count = np.count_nonzero(array == 0)
#     nonzeros_count = np.count_nonzero(array != 0)
#     return zeros_count, nonzeros_count
#
#
# # Зчитуємо масив з клавіатури
# try:
#     input_array = np.array(list(map(int, input("Введіть масив елементів через пробіл: ").split())))
#
#     zeros, nonzeros = count_zeros_nonzeros(input_array)
#
#     print(f"Кількість нульових елементів: {zeros}")
#     print(f"Кількість ненульових елементів: {nonzeros}")
#
# except ValueError:
#     print("Некоректний ввід. Будь ласка, введіть числа через пробіл.")


# def count_zeros_nonzeros(array):
#     zeros_count = sum(1 for element in array if element == 0)
#     nonzeros_count = sum(1 for element in array if element != 0)
#     return zeros_count, nonzeros_count
#
# try:
#     input_array = list(map(int, input("Введіть масив елементів через пробіл: ").split()))
#
#     zeros, nonzeros = count_zeros_nonzeros(input_array)
#
#     print(f"Кількість нульових елементів: {zeros}")
#     print(f"Кількість ненульових елементів: {nonzeros}")
#
# except ValueError:
#     print("Некоректний ввід. Будь ласка, введіть числа через пробіл.")


# def create_array_from_n_to_zero(n):
#     return np.arange(n, -1, -1)
#
# print(create_array_from_n_to_zero(5))

# def create_array_from_n_to_zero_iterative(n):
#     result_array = []
#     for i in range(n, -1, -1):
#         result_array.append(i)
#     return result_array
#
#
# print(create_array_from_n_to_zero_iterative(10))

# def create_array_with_frame(n):
#     array = np.zeros((n, n), dtype=int)
#
#     array[1:-1, 1:-1] = 1
#     return array
#
# print(create_array_with_frame(10))

# def create_array_with_frame_iterative(n):
#     array = [[0] * n for _ in range(n)]
#
#     for i in range(1, n - 1):
#         for j in range(1, n - 1):
#             array[i][j] = 1
#
#     return array
#
# for row in create_array_with_frame_iterative(5):
#      print(row)


# def create_chessboard_array(size):
#     chessboard = np.tile([[0, 1], [1, 0]], (size // 2, size // 2))
#     return chessboard[:size, :size]
#
# print(create_chessboard_array(8))


# def create_chessboard_array_iterative(size):
#     chessboard = []
#     for i in range(size):
#         row = []
#         for j in range(size):
#             value = 0 if (i + j) % 2 == 0 else 1
#             row.append(value)
#         chessboard.append(row)
#     return chessboard
#
#
# for row in create_chessboard_array_iterative(8):
#       print(row)

# def fill_matrix(n):
#     matrix = np.zeros((n, n), dtype=int)
#     matrix[0::2, :] = 1
#     return matrix
#
#
# print(fill_matrix(10))

# def fill_matrix_iterative(n):
#     matrix = [[0] * n for _ in range(n)]
#
#     for i in range(n):
#         for j in range(n):
#             if i % 2 == 0:
#                 matrix[i][j] = 1
#
#     return matrix
#
#
# for row in fill_matrix_iterative(8):
#       print(row)


# def generate_uniform_vector(n):
#     vector = np.linspace(0, 1, n, endpoint=False)
#     return np.round(vector, 3)
#
# print(generate_uniform_vector(10))


# def generate_uniform_vector_iterative(n):
#     interval_start = 0.01
#     interval_end = 1
#     step = (interval_end - interval_start) / n
#
#     vector = []
#     value = interval_start
#
#     for _ in range(n):
#         vector.append(round(value, 3))
#         value += step
#
#     return vector
#
#
# print(generate_uniform_vector_iterative(10))