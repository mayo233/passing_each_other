import  sys
import Node
import MAP
import robot2
import variable


def avoid_robot (agent1_x,agent2_x,agent1_y,agent2_y,count_2):

    print(dist (agent1_x ,agent2_x,agent1_y,agent2_y))
    if dist (agent1_x ,agent2_x,agent1_y,agent2_y) <=60.11:   #-5  52.1008644    koreninattatoki,count_2+1ninaru
        #noLoop()
        # print("agent2")
        # print(count_2)

        

        # robot2.stop=True   #robot1 stop
        # variable.stop=False
        #noLoop()
        # if variable.collision ==False:
        #     variable.pre =count
        #     variable.collision =True
        # variable.count =variable.pre
       # variable.pre +=1
            
        return agent2_x,agent2_y-10
        
    else:
        if count_2 ==44:
            variable.count_2 =44
            variable.collision=True
        return agent2_x,agent2_y
        
        
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
    
    
