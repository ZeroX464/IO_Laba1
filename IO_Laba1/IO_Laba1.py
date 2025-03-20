from scipy.optimize import linprog

c = [-5, -8, -8]

# Матрица ограничений целевой функции
A = [
    [0.02, 0, 0.04],       # Станки I типа
    [0.04, 0.03, 0.01],    # Станки II типа
    [1.0, 1.5, 2.0],       # Пряжа
    [0.03, 0.02, 0.025]    # Красители
]

# Вектор-столбец свободных членов
b = [200, 500, 15000, 450]

# Границы для переменных (x1, x2, x3)
x1_bounds = (1000, 5000)
x2_bounds = (2000, 9000)
x3_bounds = (2500, 4000)
bounds = [x1_bounds, x2_bounds, x3_bounds]

result = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs')

if result.success:
    print("Оптимальное количество ткани (x1, x2, x3):", result.x)
    x1, x2, x3 = result.x
    resource_usage = [
        A[0][0] * x1 + A[0][1] * x2 + A[0][2] * x3,
        A[1][0] * x1 + A[1][1] * x2 + A[1][2] * x3,
        A[2][0] * x1 + A[2][1] * x2 + A[2][2] * x3,
        A[3][0] * x1 + A[3][1] * x2 + A[3][2] * x3
    ]
    print("Расход ресурсов:")
    print(f"Станки I типа: {resource_usage[0]:.2f} станко-часов")
    print(f"Станки II типа: {resource_usage[1]:.2f} станко-часов")
    print(f"Пряжа: {resource_usage[2]:.2f} кг")
    print(f"Красители: {resource_usage[3]:.2f} кг")
    print("Максимальная общая стоимость:", -result.fun)
else:
    print("Решение не найдено")
