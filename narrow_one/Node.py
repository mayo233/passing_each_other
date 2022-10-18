# -*- coding: utf-8 -*-

def astar(maze, start, goal):
    # たてとよこ
    h, w = len(maze), len(maze[0])
    # print(w)
    # コスト
    #cost = np.zeros((h, w), dtype=int) + 999
    cost = [[999] * 20 for i in range(20)]
    # print(cost)
    
    # print(cost)
    
    barrier = [[False] * 20 for i in range(20)]
    
    # mazeからスタート位置、ゴール位置、障害物位置を取得
    for i in range(h):
        maze[i] = list(maze[i])
        for j in range(w):
    
            if i == start[0] and j == start[1]:
                start = (i, j)
                cost[i][j] = 0
    
            if i == goal[0] and j == goal[1]:
                goal = (i, j)
    
            if maze[i][j] == 1:
                barrier[i][j] = True
    
    # print(cost)
    # 幅優先探索
    # 今注目するコストを0とする
    now_cost = 0
    
    # 無限ループ
    for n in range(1, 999):
    
        # もしゴールのコストに999以外が書き込まれていたら無限ループ終了
        if cost[goal[0]][goal[1]] != 999:
            break
    
        # 全マスを調べる
        # 今注目するコスト値が書かれたマスを見つけたら，その上下左右のコストが999であれば未探索なので
        # 今注目するコスト+1を書き込む
    
        for i in range(len(cost)):
            for j in range(len(cost)):
    
                if cost[i][j] == now_cost:
    
                    if i - 1 >= 0  and i-1 < len(cost):  # up
                        if cost[i - 1][j] == 999:
                            if barrier[i - 1][j] == True:
                                cost[i - 1][j] = 999
                            else:
                                cost[i - 1][j] = now_cost + 1
                            # print("up,True,change")
    
                    if i + 1 < len(cost) and i+1 >=0:  # down
                        if cost[i + 1][j] == 999:
                            if barrier[i + 1][j] == True:
                                cost[i + 1][j] = 999
                            else:
                                cost[i + 1][j] = now_cost + 1
                        # print("down,True,change")
    
                    if j - 1 >= 0  and j-1 < len(cost):  # left
                        if cost[i][j - 1] == 999:
                            if barrier[i][j - 1] == True:
                                cost[i][j - 1] = 999
                            else:
                                cost[i][j - 1] = now_cost + 1
                            # print("left,True,change")
    
                    if j + 1 < len(cost)  and j+1 >=0:  # right
                        if cost[i][j + 1] == 999:
                            if barrier[i][j + 1] == True:
                                cost[i][j + 1] = 999
                            else:
                                cost[i][j + 1] = now_cost + 1
        now_cost += 1
    
   # print(cost)
    
    # ゴールから逆順でルート計算
    #########################
    #goal =(7,5)
    point_now = goal
    # print("point_now")
    # print(point_now)
    cost_now = cost[goal[0]][goal[1]]
    route = [goal]
    while cost_now > 0:
    
        # 上から来た場合
        try:
            if point_now[0] -1 >=0  and point_now[1] >=0 :
                if cost[point_now[0] - 1][point_now[1]] == cost_now - 1:
                    # 更新
                    point_now = (point_now[0] - 1, point_now[1])
                    cost_now = cost_now - 1
                    # 記録
                    route.append(point_now)
                    #print(route)
        except:
            pass
        # 下から来た場合
        try:
            if point_now[0] +1 >=0  and point_now[1] >=0 :
                if cost[point_now[0] + 1][point_now[1]] == cost_now - 1:
                    # 更新
                    point_now = (point_now[0] + 1, point_now[1])
                    cost_now = cost_now - 1
                    # 記録
                    route.append(point_now)

        except:
            pass
        # 左から来た場合
        try:
            if point_now[0]>=0  and point_now[1] -1>=0 :
                if cost[point_now[0]][point_now[1] - 1] == cost_now - 1:
                    # 更新
                    # print(cost_now - 1)
                    # print(cost[point_now[0]][point_now[1] - 1])
                    point_now = (point_now[0], point_now[1] - 1)
                    #print(point_now)
                    cost_now = cost_now - 1
                    # 記録
                    route.append(point_now)
        except:
            pass
        # 右から来た場合
        try:
            if point_now[0]  >=0  and point_now[1] +1>=0 :
                if cost[point_now[0]][point_now[1] + 1] == cost_now - 1:
                    # 更新
                    point_now = (point_now[0], point_now[1] + 1)
                    cost_now = cost_now - 1
                    # 記録
                    route.append(point_now)

        except:
            pass
    
    # ルートを逆順にする
    route = route[::-1]
    # print("route_fact")
    # print(route)
    return route
    
