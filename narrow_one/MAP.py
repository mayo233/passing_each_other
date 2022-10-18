# -*- coding: utf-8 -*-
import variable

# ブロック作成を行う関数
def make_brock(num1,num2,block_h_num):
    for i in range(20):
        for j in range(20):

            if (i == 0 and j == 19):  # 赤色　ゴール地点とスタート地点
                fill(250, 20, 0)
                rect(j * 10, i * 10, 10, 10)
                
            # agent1 task murasaki
            elif (i==block_h_num and j==num1):
                fill(167, 87, 168)
                rect(j * 10, i * 10, 10, 10)
                
            # agent2 task pink
            elif (i==block_h_num and j==num2):
                fill(234, 145, 152)
                rect(j * 10, i * 10, 10, 10)
            

            elif (i == 19 and j == 0):  # スタートとゴール地点
                fill(0, 0, 255)
                rect(j * 10, i * 10, 10, 10)

            elif variable.brock[i][j] == 0:
                fill(255, 255, 255)  # 白いブロックにする
                rect(j * 10, i * 10, 10, 10)

            elif variable.brock[i][j] == 1:
                fill(0, 0, 0)  # 黒いブロックにする
                    
                if variable.stop_time >=1:
                    fill(255,255,255)
                    # print("iiiiiii")
                    # print(variable.block_num_pre)
                    rect(variable.block_num_pre*10,70,10,10)
                else:   
                    rect(j * 10, i * 10, 10, 10)
                    
                
                
            # print("block_num")
            # print(block_num)
                
                
