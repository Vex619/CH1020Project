# Problem 1: Piecewise linear interpolation

x = [0.2, 0.4, 0.6, 0.8, 1.0]
y = [0.17, 0.57, 1.1, 1.8, 2.5]

def piecewise_linear_interp(x_data, y_data, x0):
    # Find interval [x_i, x_{i+1}] that contains x0
    for i in range(len(x_data) - 1):
        x1, x2 = x_data[i], x_data[i+1]
        if x1 <= x0 <= x2:
            y1, y2 = y_data[i], y_data[i+1]
            # Linear interpolation formula [web:5]
            return y1 + (x0 - x1) * (y2 - y1) / (x2 - x1)
    raise ValueError("x0 is outside the data range")

print("y at x=0.3 =", piecewise_linear_interp(x, y, 0.3))
print("y at x=0.7 =", piecewise_linear_interp(x, y, 0.7))
# Problem 2: Linear least-squares fit (flowrate vs setting)

import numpy as np

setting = np.array([2.5, 2.5, 5, 5, 10, 10, 20, 20], dtype=float)
volume  = np.array([10, 10, 10, 10, 90, 90, 90, 90], dtype=float)
time_s  = np.array([12.4, 12.7, 6.3, 6.1, 27.2, 27.4, 13.7, 13.9], dtype=float)

flow = volume / time_s  # ml/s

# Fit y = m x + b using least squares [web:14]
A = np.vstack([setting, np.ones_like(setting)]).T
m, b = np.linalg.lstsq(A, flow, rcond=None)[0]

print("Flowrates (ml/s):", flow)
print(f"Best-fit line: flow = {m:.6f}*setting + {b:.6f}")

