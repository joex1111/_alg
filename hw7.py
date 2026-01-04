from collections import deque

def is_valid(state):
    human, wolf, sheep, cabbage = state
    # 如果羊跟狼在一起，且人不在場 -> 不合法
    if wolf == sheep and human != wolf:
        return False
    # 如果羊跟菜在一起，且人不在場 -> 不合法
    if sheep == cabbage and human != sheep:
        return False
    return True

def solve_river_puzzle():
    # 狀態表示：(人, 狼, 羊, 菜)，0 代表左岸，1 代表右岸
    start_state = (0, 0, 0, 0)
    goal_state = (1, 1, 1, 1)
    
    # queue 存放 (當前狀態, 之前的路徑)
    queue = deque([(start_state, [])])
    visited = {start_state}
    
    names = ["人", "狼", "羊", "菜"]
    
    while queue:
        current_state, path = queue.popleft()
        
        if current_state == goal_state:
            return path + [current_state]
        
        h, w, s, c = current_state
        
        # 找出所有可能的下一個動作（人一定要移動，並選擇帶 0 或 1 個物品）
        possible_moves = []
        # 情境 1: 人自己過河
        possible_moves.append((1-h, w, s, c))
        # 情境 2: 人帶狼
        if h == w: possible_moves.append((1-h, 1-w, s, c))
        # 情境 3: 人帶羊
        if h == s: possible_moves.append((1-h, w, 1-s, c))
        # 情境 4: 人帶菜
        if h == c: possible_moves.append((1-h, w, s, 1-c))
        
        for move in possible_moves:
            if move not in visited and is_valid(move):
                visited.add(move)
                queue.append((move, path + [current_state]))

    return None

def print_solution(path):
    if not path:
        print("找不到解。")
        return
    
    items = ["人", "狼", "羊", "菜"]
    for i, state in enumerate(path):
        left = [items[j] for j in range(4) if state[j] == 0]
        right = [items[j] for j in range(4) if state[j] == 1]
        print(f"步驟 {i}: 左岸:{left} | ---河--- | 右岸:{right}")

# 執行程式
solution_path = solve_river_puzzle()
print_solution(solution_path)
