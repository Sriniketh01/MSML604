from scipy.optimize import linprog
import time

# Coefficients for the objective function (negative because linprog minimizes)
c = [-640, -440, -200, -480, -330, -150, -480, -330, -150, 0, 0, 0]

# Constraint matrix (A_ub * x <= b_ub)
A = [
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],   # x1 ≤ 25
    [1, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0],  # x1 - x10 ≤ 0
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],   # x2 ≤ 60
    [0, 1, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0],  # x2 - x10 ≤ 0
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],   # x3 ≤ 210
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, -1],  # x3 - x12 ≤ 0
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],   # x4 ≤ 12
    [0, 0, 0, 1, 0, 0, 0, 0, 0, -1, 0, 0],  # x4 - x10 ≤ 0
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],   # x5 ≤ 30
    [0, 0, 0, 0, 1, 0, 0, 0, 0, -1, 0, 0],  # x5 - x11 ≤ 0
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],   # x6 ≤ 130
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, -1],  # x6 - x12 ≤ 0
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],   # x7 ≤ 5
    [0, 0, 0, 0, 0, 0, 1, 0, 0, -1, 0, 0],  # x7 - x10 ≤ 0
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],   # x8 ≤ 9
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, -1, 0],  # x8 - x11 ≤ 0
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],   # x9 ≤ 150
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, -1],  # x9 - x12 ≤ 0
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1.5, 1], # 2x10 + 1.5x11 + x12 ≤ 190
]

# Constraint bounds
b = [25, 0, 60, 0, 210, 0, 12, 0, 30, 0, 130, 0, 5, 0, 9, 0, 150, 0, 190]

# Non-negative bounds
bounds = [(0, None)] * 12

# Revised simplex method
start_revised = time.time()
res_revised = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='revised simplex')
time_revised = time.time() - start_revised

# Simplex method
start_simplex = time.time()
res_simplex = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='simplex')
time_simplex = time.time() - start_simplex

# Results
results = {
    "Revised Simplex": {
        "Objective Value": -res_revised.fun,
        "Computation Time (s)": time_revised
    },
    "Simplex": {
        "Objective Value": -res_simplex.fun,
        "Computation Time (s)": time_simplex
    }
}

import pandas as pd
import ace_tools as tools; tools.display_dataframe_to_user(name="Method Comparison Results", dataframe=pd.DataFrame(results))
