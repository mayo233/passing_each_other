import  sys
import Node
import MAP
import robot2
import variable

stop_count =0
stop =False

def avoid_robot (agent1_x,agent2_x,agent1_y,agent2_y,count_2):
    global stop_count,stop

    #print(dist (agent1_x ,agent2_x,agent1_y,agent2_y))
    #if dist (agent1_x ,agent2_x,agent1_y,agent2_y) <=60.11:   #-5  52.1008644    koreninattatoki,count_2+1ninaru  60.11
    #if ((floor(mag(agent2_x,agent2_y))/10) - (floor(mag(agent1_x, agent1_y))/10) ==1) and (agent2_y/10 ==8):
    # print(floor(agent2_x/10))
    # print(floor(agent1_x/10))
    
    if (floor(agent2_x/10) - floor(agent1_x/10)) <=2  and floor(agent2_x/10) - floor(agent1_x/10) >=0:

       #noLoop()
        # print("butukaru")
        # print(count_2)

        variable.collision =True
        stop=True
        
        
        return agent2_x,agent2_y,stop
        # while stop_count >=100000:
        #     stop_count +=1 
        #     print("sasasasasa")
        #     print(stop_count)
        #     print
        #     print(dist (agent1_x ,agent2_x,agent1_y,agent2_y))
          
        #noLoop()
        # print("agent2")
        # print(count_2)
        # robot2.stop=True   #robot1 stop
        # variable.stop=False
        #noLoop()
        # if variable.collision ==False:
        #     variable.pre =count
        #     variable.collision =True
       #  # variable.count =variable.pre
       # # variable.pre +=1
       #  print("stop!!!!")
       #  print(agent2_y-10)
            
       #  return agent2_x,agent2_y-10,stop
        #return agent2_x,agent2_y-10,stop
        
    else:
        # print("count_2")
        # print(count_2)
        # stop=False
        # if count_2 ==48:
        #     variable.count_2 =48
        #     variable.collision=True
            
        return agent2_x,agent2_y,stop
        
        
        #return agent1_x
        #noLoop()

        
        #ellipse(variable.pre,agent1_y-10,7,7)

        
        #noLoop()
        #noLoop()
        #ellipse(agent2_x,agent2_y-10,7,7)
    #     if count_collision ==0:
    #         collision =True
    # elif agent2_x - agent1_x <=-20:
    #     variable.stop =False
    # if collision == True:
    #     if space==False:
            
        # print("avoid!!!")
        # #print(agent2)
        # if variable.delete ==False:
        #     variable.temp_x =agent2_x
        #     variable.temp_y= agent2_y
        #     variable.delete =True
        # #ellipse(variable.x_2[7]*10+2.5, variable.y_2[9]*10+4, 7, 7) 
        # ellipse(variable.temp_x,variable.temp_y,7,7)
    
    
