# -*- coding: utf-8 -*-
import sys
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage.filters import minimum_filter, maximum_filter

if __name__ == '__main__':

    # mat = [
    #     [1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
    #     [0, 1, 1, 1, 1, 1, 0, 1, 0, 1],
    #     [0, 0, 1, 0, 1, 1, 1, 0, 0, 1],
    #     [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
    #     [0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    #     [1, 0, 1, 1, 1, 0, 0, 1, 1, 0],
    #     [0, 0, 0, 0, 1, 0, 0, 1, 0, 1],
    #     [0, 1, 1, 1, 1, 1, 1, 1, 0, 0],
    #     [1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
    #     [0, 0, 1, 0, 0, 1, 1, 0, 0, 1]
    # ]

    maze=[
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]


    #########################
    # 前処理
    #########################
    #たてとよこ
    h, w = len(maze), len(maze[0])
    #コスト
    cost = np.zeros((h, w), dtype=int) + 999
    #コストが書き込まれて探索が終了したマス（bool）
    done = np.zeros((h, w), dtype=bool)
    #障害物（bool）
    barrier = np.zeros((h, w), dtype=bool)

    #プーリング用のフィルタ
    g = np.array([[0, 1, 0],
                [1, 1, 1],
                [0, 1, 0]])

    #mazeからスタート位置、ゴール位置、障害物位置を取得
    for i in range(h):
        maze[i] = list(maze[i])
        for j in range(w):
            if i==19 and j==0:
                start = (i, j)
                cost[i, j] = 0
                done[i, j] = True
            if i==4 and j==8:
                goal = (i, j)
            if maze[i][j] == 1:
                barrier[i, j] = True

    print('start\n{}'.format(start))
    print('goal\n{}'.format(goal))
    print('cost\n{}'.format(cost))
    print("cost_finished")
    print('done\n{}'.format(done))
    print('barrier\n{}'.format(barrier))
    
    #########################
    # 幅優先探索
    #########################
    count =0
    for i in range(1, 999):

        #次に進出するマスのbool
        #done_next = maximum_filter(done, footprint=g) * ~done
        done_next = maximum_filter(done, footprint=g) * ~done
        #print(i)
        count +=1
        # print(count)
        #print('done_next\n{}'.format(done_next))
        
        #次に進出するマスのcost
        cost_next = minimum_filter(cost, footprint=g) * done_next
        cost_next[done_next] += 1
        #print('cost_next\n{}'.format(cost_next))
        
        #costを更新
        cost[done_next] = cost_next[done_next]
        #ただし障害物のコストは999とする
        cost[barrier] = 999
        #print('cost\n{}'.format(cost))
        
        #探索終了マスを更新
        done[done_next] = done_next[done_next]
        #ただし障害物は探索終了としない
        done[barrier] = False
        #print('done\n{}'.format(done))
        
        #表示
        #show(i)
        
        #終了判定
        if done[goal[0], goal[1]] == True:
            break
    
    print(cost)
    #########################
    # ゴールから逆順でルート計算
    #########################
    point_now = goal
    cost_now = cost[goal[0], goal[1]]
    route = [goal]
    print('route\n{}'.format(route))
    while cost_now > 0:
        #上から来た場合
        try:
            if cost[point_now[0] - 1, point_now[1]] == cost_now - 1:
                #更新
                point_now = (point_now[0] - 1, point_now[1])
                cost_now = cost_now - 1
                #記録
                route.append(point_now)
        except: pass
        #下から来た場合
        try:
            if cost[point_now[0] + 1, point_now[1]] == cost_now - 1:
                #更新
                point_now = (point_now[0] + 1, point_now[1])
                cost_now = cost_now - 1
                #記録
                route.append(point_now)
        except: pass
        #左から来た場合    
        try:
            if cost[point_now[0], point_now[1] - 1] == cost_now - 1:
                #更新
                point_now = (point_now[0], point_now[1] - 1)
                cost_now = cost_now - 1
                #記録
                route.append(point_now)
        except: pass
        #右から来た場合
        try:
            if cost[point_now[0], point_now[1] + 1] == cost_now - 1:
                #更新
                point_now = (point_now[0], point_now[1] + 1)
                cost_now = cost_now - 1
                #記録
                route.append(point_now)
        except: pass

    # #ルートを逆順にする
    route = route[::-1]
    print('route\n{}'.format(route))
    # コスト配列の表示（numpyを使わないと見づらい）
    """
    
    print(cost[6][5])
    # 目的地に記入されたコスト
    print(cost[7][5])
    print(cost)
    
    # ゴールから逆順でルート計算
    #########################
    goal =(7,5)
    point_now = goal
    # print("point_now")
    # print(point_now)
    cost_now = cost[7][5]
    route = [goal]
    while cost_now >0:
        
        #上から来た場合
        try:
            if cost[point_now[0] - 1][point_now[1]] == cost_now - 1:
                print("up")
                #更新
                point_now = (point_now[0] - 1, point_now[1])
                cost_now = cost_now - 1
                #記録
                route.append(point_now)
        except: pass
        #下から来た場合
        try:
            if cost[point_now[0] + 1][point_now[1]] == cost_now - 1:
                #更新
                point_now = (point_now[0] + 1, point_now[1])
                print(point_now)
                print("down")
                cost_now = cost_now - 1
                #記録
                route.append(point_now)
        except: pass
        #左から来た場合    
        try:
            if cost[point_now[0]][point_now[1] - 1] == cost_now - 1:
                #更新
                # print(cost_now - 1)
                print("left")
                # print(cost[point_now[0]][point_now[1] - 1])
                point_now = (point_now[0], point_now[1] -1)
                print(point_now)
                cost_now = cost_now - 1
                #記録
                route.append(point_now)
        except: pass
        #右から来た場合
        try:
            if cost[point_now[0]][point_now[1] + 1] == cost_now - 1:
                #更新
                print("bbbb")
                point_now = (point_now[0] , point_now[1]+1)
                cost_now = cost_now - 1
                #記録
                route.append(point_now)
        except: pass

    #ルートを逆順にする
    route = route[::-1]
    print("route_fact")
    print('route\n{}'.format(route))
"""