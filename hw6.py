import numpy as np
import matplotlib.pyplot as plt
import random

# 1. 產生模擬數據
np.random.seed(42)
X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1)

# --- 演算法實作 ---

# [1] 梯度下降法 (Gradient Descent)
def gradient_descent(X, y, lr=0.1, epochs=100):
    w, b = 0.0, 0.0
    m = len(y)
    for _ in range(epochs):
        y_pred = w * X + b
        dw = -(2/m) * np.sum(X * (y - y_pred))
        db = -(2/m) * np.sum(y - y_pred)
        w -= lr * dw
        b -= lr * db
    return w, b

# [2] 爬山演算法 (Hill Climbing)
def hill_climbing(X, y, epochs=1000, step=0.1):
    w, b = 0.0, 0.0
    def get_mse(w, b):
        return np.mean((y - (w * X + b))**2)
    
    curr_mse = get_mse(w, b)
    for _ in range(epochs):
        next_w = w + random.uniform(-step, step)
        next_b = b + random.uniform(-step, step)
        next_mse = get_mse(next_w, next_b)
        if next_mse < curr_mse:
            w, b, curr_mse = next_w, next_b, next_mse
    return w, b

# [3] 貪婪法概念 (簡化版：基於當前最優步徑更新)
def greedy_search(X, y, epochs=100, step=0.05):
    w, b = 0.0, 0.0
    def get_mse(w, b): return np.mean((y - (w * X + b))**2)
    
    for _ in range(epochs):
        # 貪婪地從四個方向選一個最好的
        candidates = [(w+step, b), (w-step, b), (w, b+step), (w, b-step)]
        best_w, best_b = w, b
        min_mse = get_mse(w, b)
        for nw, nb in candidates:
            mse = get_mse(nw, nb)
            if mse < min_mse:
                min_mse = mse
                best_w, best_b = nw, nb
        w, b = best_w, best_b
    return w, b

# [4] 改良法：動量梯度下降 (Momentum GD)
def momentum_gd(X, y, lr=0.1, momentum=0.9, epochs=100):
    w, b = 0.0, 0.0
    vw, vb = 0.0, 0.0
    m = len(y)
    for _ in range(epochs):
        y_pred = w * X + b
        dw = -(2/m) * np.sum(X * (y - y_pred))
        db = -(2/m) * np.sum(y - y_pred)
        vw = momentum * vw - lr * dw
        vb = momentum * vb - lr * db
        w += vw
        b += vb
    return w, b

# --- 執行與繪圖 ---

# 計算結果
res_gd = gradient_descent(X, y)
res_hc = hill_climbing(X, y)
res_gs = greedy_search(X, y)
res_mom = momentum_gd(X, y)

# 繪圖
plt.figure(figsize=(10, 6))
plt.scatter(X, y, color='gray', alpha=0.5, label='Data Points')
x_range = np.array([0, 2])

plt.plot(x_range, res_gd[0]*x_range + res_gd[1], 'r-', label='Gradient Descent')
plt.plot(x_range, res_hc[0]*x_range + res_hc[1], 'g--', label='Hill Climbing')
plt.plot(x_range, res_gs[0]*x_range + res_gs[1], 'b:', label='Greedy Search')
plt.plot(x_range, res_mom[0]*x_range + res_mom[1], 'y-.', label='Momentum GD')

plt.title('Linear Regression with Different Algorithms')
plt.legend()
plt.grid(True)
plt.show()

print(f"梯度下降: w={res_gd[0]:.2f}, b={res_gd[1]:.2f}")
print(f"爬山法:   w={res_hc[0]:.2f}, b={res_hc[1]:.2f}")
print(f"貪婪搜尋: w={res_gs[0]:.2f}, b={res_gs[1]:.2f}")
print(f"動量改良: w={res_mom[0]:.2f}, b={res_mom[1]:.2f}")
