# 初始化10x10的空棋盘
board = [['.' for _ in range(10)] for _ in range(10)]

# 打印棋盘
for row in board:
    print(' '.join(row))
print()

# 游戏主循环
game_over = False
player_turn = 1

while not game_over:
    # 轮到玩家输入
    print(f"玩家 {player_turn} 的回合")
    valid_move = False

    # 循环以确保输入合法
    while not valid_move:
        try:
            x, y = map(int, input("请输入要下子的坐标 (格式: x y): ").split())
            if 0 <= x < 10 and 0 <= y < 10 and board[x][y] == '.':
                valid_move = True
            else:
                print("输入无效！请确保输入在范围内且该位置为空。")
        except ValueError:
            print("输入无效！请输入两个数字，表示坐标。")

    # 更新棋盘
    board[x][y] = 'X' if player_turn == 1 else 'O'

    # 打印更新后的棋盘
    for row in board:
        print(' '.join(row))
    print()

    # 检查是否形成了长度为3的连续标记链条
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, 1), (-1, 1), (1, -1)]
    chain_detected = False

    for dx, dy in directions:
        count = 1
        nx, ny = x + dx, y + dy
        # 正向检查
        while 0 <= nx < 10 and 0 <= ny < 10 and board[nx][ny] != '.':
            count += 1
            nx += dx
            ny += dy

        # 反向检查
        nx, ny = x - dx, y - dy
        while 0 <= nx < 10 and 0 <= ny < 10 and board[nx][ny] != '.':
            count += 1
            nx -= dx
            ny -= dy

        if count >= 3:
            chain_detected = True
            break

    # 如果检测到长度为3的链条，游戏结束
    if chain_detected:
        print(f"玩家 {player_turn} 形成了长度为3的链条，游戏结束！玩家 {player_turn} 输。")
        game_over = True
    else:
        # 切换玩家
        player_turn = 2 if player_turn == 1 else 1