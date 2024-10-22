qipan = 10
caozuo = [['.' for _ in range(qipan)] for _ in range(qipan)]  # 初始化棋盘

for hang in caozuo:
    print(' '.join(hang))# .join表示的是叠次出现
print()

player = 1

while True:    # 游戏循环
    for hang in caozuo:  # 显示当前棋盘状态
        print(' '.join(hang))
    print()

    print(f"玩家 {player} 的回合:")

    try:  # 请求玩家输入坐标x y
        x, y = map(int, input("请输入坐标 (行 列): ").split())
    except ValueError:
        print("输入无效，请输入两个整数。")
        continue

    if not (0 <= x < qipan and 0 <= y < qipan and caozuo[x][y] == '.'):  # 检查输入是否合法
        print("无效的移动，位置超出范围或该格子已被占用，请重试。")
        continue

    if player == 1:  # 依据玩家标记棋盘
        caozuo[x][y] = 'X'
    else:
        caozuo[x][y] = 'O'

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, 1), (-1, 1), (1, -1)]
    gameover = False          # 检查是否形成3个连续的标记（任意标记，不分玩家）

    for dx, dy in directions:
        count = 1  # 包含当前标记

        # 向一个方向检查连续标记
        for i in range(1, 3):  # 只检查连续的2个格子，总共3个标记
            nx = x + i * dx
            ny = y + i * dy
            if 0 <= nx < qipan and 0 <= ny < qipan and caozuo[nx][ny] != '.' and caozuo[nx][ny] != '.':
                count += 1
            else:
                break

        # 反方向检查
        for i in range(1, 3):  # 反方向最多再查2个
            nx = x - i * dx
            ny = y - i * dy
            if (0 <= nx < qipan and
                    0 <= ny < qipan and
                    caozuo[nx][ny] != '.' and
                    caozuo[nx][ny] != '.'):
                count += 1
            else:
                break

        if count >= 3:  # 如果任意方向形成3个连续标记
            gameover = True
            break

    if gameover:
        for hang in caozuo:
            print(' '.join(hang))
        print(f"玩家 {player} 输了!")
        break

    if player == 1:           # 切换玩家
        player = 2
    else:
        player = 1