def riemann_n_dim(f, bounds, steps):
    """
    f: 待積分函數，接受一個 list 作為參數
    bounds: 積分範圍，格式為 [(x1_min, x1_max), (x2_min, x2_max), ...]
    steps: 每一維度切割的份數
    """
    n = len(bounds)
    # 計算每一維度的步長 (delta)
    deltas = [(b - a) / steps for a, b in bounds]
    unit_volume = 1
    for d in deltas:
        unit_volume *= d

    def compute_recursive(dimension, current_point):
        if dimension == n:
            # 遞迴終點：已經確定了所有維度的座標，計算函數值
            return f(current_point)
        
        total_sum = 0.0
        a, b = bounds[dimension]
        d = deltas[dimension]
        
        # 在該維度進行遍歷 (取區塊中點作為採樣點)
        for i in range(steps):
            coord = a + (i + 0.5) * d
            current_point.append(coord)
            total_sum += compute_recursive(dimension + 1, current_point)
            current_point.pop() # 回溯 (Backtracking)
            
        return total_sum

    return compute_recursive(0, []) * unit_volume
