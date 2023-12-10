from collections import deque

def is_valid(x, y):
    return 0 <= x < 8 and 0 <= y < 8

def knight_moves(start, end):
    directions = [(-2, -1), (-2, 1), (-1, -2), (-1, 2),
                  (1, -2), (1, 2), (2, -1), (2, 1)]  # 骑士的八个可能移动方向

    queue = deque([(start, 0)])
    visited = set([start])

    while queue:
        current, distance = queue.popleft()

        if current == end:
            return distance

        x, y = current
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            neighbor = (nx, ny)

            if is_valid(nx, ny) and neighbor not in visited:
                queue.append((neighbor, distance + 1))
                visited.add(neighbor)

    # 如果无法找到路径，返回-1表示失败
    return -1

# 例如，从(0, 0)到(7, 7)的最短路径长度
for i in range(0, 64):
    for j in range(0, 64):   
        if i != j:
            start_point = (i//8, i%8)
            end_point = (j//8, j%8)
            result = knight_moves(start_point, end_point)
            print("x: ", i," y: ", j, "step: ", result)


#if result != -1:
#    print(f"从{start_point}到{end_point}的最短路径长度是: {result}")
#else:
#    print(f"无法找到从{start_point}到{end_point}的路径")
