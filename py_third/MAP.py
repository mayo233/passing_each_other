# -*- coding: utf-8 -*-
import variable

# ブロック作成を行う関数
def make_brock():
    for i in range(50):
        for j in range(50):

            if (i == 0 and j == 49):  # 赤色　ゴール地点とスタート地点
                fill(250, 20, 0)
                rect(j * 10, i * 10, 10, 10)

            elif ((i == 8 and j == 7) or (i == 8 and j == 31)):  # 中間地点
                # println(j)
                fill(055, 255, 0)
                rect(j * 10, i * 10, 10, 10)

            elif (i == 49 and j == 0):  # スタートとゴール地点
                fill(0, 0, 255)
                rect(j * 10, i * 10, 10, 10)

            elif variable.brock[i][j] == 0:
                fill(255, 255, 255)  # 白いブロックにする
                rect(j * 10, i * 10, 10, 10)

            elif variable.brock[i][j] == 1:
                fill(0, 0, 0)  # 黒いブロックにする
                if variable.pre != 0:
                    fill(255, 255, 255)
                    
                    # if variable.delete ==False:
                    #      break_x =variable.pre
                    #      variable.delete =True
                   
                    rect(24 *10, 70, 10, 10)   #240,70
                else:
                    rect(j * 10, i * 10, 10, 10)
