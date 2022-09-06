import  sys
import Node
import MAP
import robot1
import variable


def avoid_robot (agent1_x,agent2_x,agent1_y,agent2_y):
    print(agent2_x - agent1_x )
    if agent2_x - agent1_x <=10:
        variable.stop =True
        print("sasa")
        noLoop()
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
    
    
