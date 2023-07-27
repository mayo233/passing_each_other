"""
Python implementation of Conflict-based search
author: Ashwin Bose (@atb033)
"""

import sys
sys.path.insert(0, '../')
import argparse
import yaml
import os
from math import fabs
from itertools import combinations
from copy import deepcopy

from cbs.a_star import AStar

agent_goal =[]         
agent_goal_num =[]      
agent_num =[]     
agent_wait_num =0
num =0
count =0
goal_reached = False
coflict_spot =False
research_spot =False
conflict_spot =0
task_1 =(8,8)
task_2 =(5,8)

class Location(object):
    def __init__(self, x=-1, y=-1):
        self.x = x
        self.y = y
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    def __str__(self):
        return str((self.x, self.y))

class State(object):
    def __init__(self, time, location):
        self.time = time
        self.location = location
    def __eq__(self, other):
        return self.time == other.time and self.location == other.location
    def __hash__(self):
        return hash(str(self.time)+str(self.location.x) + str(self.location.y))
    def is_equal_except_time(self, state):
        return self.location == state.location
    def __str__(self):
        return str((self.time, self.location.x, self.location.y))

class Conflict(object):
    VERTEX = 1
    EDGE = 2
    def __init__(self):
        self.time = -1
        self.type = -1

        self.agent_1 = ''
        self.agent_2 = ''

        self.location_1 = Location()
        self.location_2 = Location()

    def __str__(self):
        return '(' + str(self.time) + ', ' + self.agent_1 + ', ' + self.agent_2 + \
             ', '+ str(self.location_1) + ', ' + str(self.location_2) + ')'

class VertexConstraint(object):
    def __init__(self, time, location):
        self.time = time
        self.location = location

    def __eq__(self, other):
        return self.time == other.time and self.location == other.location
    def __hash__(self):
        return hash(str(self.time)+str(self.location))
    def __str__(self):
        return '(' + str(self.time) + ', '+ str(self.location) + ')'

class EdgeConstraint(object):
    def __init__(self, time, location_1, location_2):
        self.time = time
        self.location_1 = location_1
        self.location_2 = location_2
    def __eq__(self, other):
        return self.time == other.time and self.location_1 == other.location_1 \
            and self.location_2 == other.location_2
    def __hash__(self):
        return hash(str(self.time) + str(self.location_1) + str(self.location_2))
    def __str__(self):
        return '(' + str(self.time) + ', '+ str(self.location_1) +', '+ str(self.location_2) + ')'

class Constraints(object):
    def __init__(self):
        self.vertex_constraints = set()
        self.edge_constraints = set()

    def add_constraint(self, other):
        self.vertex_constraints |= other.vertex_constraints
        self.edge_constraints |= other.edge_constraints

    def __str__(self):
        return "VC: " + str([str(vc) for vc in self.vertex_constraints])  + \
            "EC: " + str([str(ec) for ec in self.edge_constraints])

class Environment(object):
    def __init__(self, dimension, agents, obstacles):
        self.dimension = dimension
        self.obstacles = obstacles

        self.agents = agents
        self.agent_dict = {}

        self.make_agent_dict()

        self.constraints = Constraints()
        self.constraint_dict = {}

        self.a_star = AStar(self)

    def get_neighbors(self, state):
        neighbors = []

        # Wait action
        n = State(state.time + 1, state.location)
        if self.state_valid(n):
            neighbors.append(n)
        # Up action
        n = State(state.time + 1, Location(state.location.x, state.location.y+1))
        if self.state_valid(n) and self.transition_valid(state, n):
            neighbors.append(n)
        # Down action
        n = State(state.time + 1, Location(state.location.x, state.location.y-1))
        if self.state_valid(n) and self.transition_valid(state, n):
            neighbors.append(n)
        # Left action
        n = State(state.time + 1, Location(state.location.x-1, state.location.y))
        if self.state_valid(n) and self.transition_valid(state, n):
            neighbors.append(n)
        # Right action
        n = State(state.time + 1, Location(state.location.x+1, state.location.y))
        if self.state_valid(n) and self.transition_valid(state, n):
            neighbors.append(n)
        return neighbors


    def get_first_conflict(self, solution):

        global coflict_spot,conflict_spot,task_1,task_2,research_spot

        max_t = max([len(plan) for plan in solution.values()])
        result = Conflict()
        for t in range(max_t):
            for agent_1, agent_2 in combinations(solution.keys(), 2):
                state_1 = self.get_state(agent_1, solution, t)
                state_2 = self.get_state(agent_2, solution, t)
                if state_1.is_equal_except_time(state_2):
                    result.time = t
                    result.type = Conflict.VERTEX
                    result.location_1 = state_1.location
                    result.agent_1 = agent_1
                    result.agent_2 = agent_2
                    #print(state_1.location)

                    if coflict_spot == True:
                        print("pp")
                        

                        conflict_spot =result.location_1


                        #もし，衝突地点がタスクの位置なら探索不可にする場所をタスクの位置付近に変更                
                        if not conflict_spot.x == task_1[0] and conflict_spot.y == task_1[1]  or conflict_spot.x == task_2[0] and conflict_spot.y == task_2[1]:
                            print("ppppp")
                            research_spot =False
                            

                        if  (conflict_spot.x == task_1[0] and conflict_spot.y == task_1[1])  or (conflict_spot.x == task_2[0] and conflict_spot.y == task_2[1]):
                            print("pppppuuuuuu")
                            research_spot =True

                        
                        print("衝突地点")
                        print(conflict_spot)

                    with open("conflict_maze.txt", "w") as f:
                        f.writelines(str(conflict_spot))

                        
                        # conflict_spot_maze(conflict_spot)

                    return result

            for agent_1, agent_2 in combinations(solution.keys(), 2):
                state_1a = self.get_state(agent_1, solution, t)
                state_1b = self.get_state(agent_1, solution, t+1)

                state_2a = self.get_state(agent_2, solution, t)
                state_2b = self.get_state(agent_2, solution, t+1)

                if state_1a.is_equal_except_time(state_2b) and state_1b.is_equal_except_time(state_2a):
                    result.time = t
                    result.type = Conflict.EDGE
                    result.agent_1 = agent_1
                    result.agent_2 = agent_2
                    result.location_1 = state_1a.location
                    result.location_2 = state_1b.location

                    return result
        return False

    def create_constraints_from_conflict(self, conflict):
        constraint_dict = {}
        if conflict.type == Conflict.VERTEX:
            v_constraint = VertexConstraint(conflict.time, conflict.location_1)
            constraint = Constraints()
            constraint.vertex_constraints |= {v_constraint}
            constraint_dict[conflict.agent_1] = constraint
            constraint_dict[conflict.agent_2] = constraint

        elif conflict.type == Conflict.EDGE:
            constraint1 = Constraints()
            constraint2 = Constraints()

            e_constraint1 = EdgeConstraint(conflict.time, conflict.location_1, conflict.location_2)
            e_constraint2 = EdgeConstraint(conflict.time, conflict.location_2, conflict.location_1)

            constraint1.edge_constraints |= {e_constraint1}
            constraint2.edge_constraints |= {e_constraint2}

            constraint_dict[conflict.agent_1] = constraint1
            constraint_dict[conflict.agent_2] = constraint2

        return constraint_dict

    def get_state(self, agent_name, solution, t):
        if t < len(solution[agent_name]):
            return solution[agent_name][t]
        else:
            return solution[agent_name][-1]

    def state_valid(self, state):
        return state.location.x >= 0 and state.location.x < self.dimension[0] \
            and state.location.y >= 0 and state.location.y < self.dimension[1] \
            and VertexConstraint(state.time, state.location) not in self.constraints.vertex_constraints \
            and (state.location.x, state.location.y) not in self.obstacles

    def transition_valid(self, state_1, state_2):
        return EdgeConstraint(state_1.time, state_1.location, state_2.location) not in self.constraints.edge_constraints

    def is_solution(self, agent_name):
        pass

    def admissible_heuristic(self, state, agent_name):
        goal = self.agent_dict[agent_name]["goal"]
        return fabs(state.location.x - goal.location.x) + fabs(state.location.y - goal.location.y)


    def is_at_goal(self, state, agent_name):
        goal_state = self.agent_dict[agent_name]["goal"]
        return state.is_equal_except_time(goal_state)

    def make_agent_dict(self):
        for agent in self.agents:
            start_state = State(0, Location(agent['start'][0], agent['start'][1]))
            goal_state = State(0, Location(agent['goal'][0], agent['goal'][1]))

            self.agent_dict.update({agent['name']:{'start':start_state, 'goal':goal_state}})

    def compute_solution(self):
        solution = {}
        for agent in self.agent_dict.keys():
            self.constraints = self.constraint_dict.setdefault(agent, Constraints())
            local_solution = self.a_star.search(agent)
            if not local_solution:
                return False
            solution.update({agent:local_solution})
        return solution

    def compute_solution_cost(self, solution):
        return sum([len(path) for path in solution.values()])

class HighLevelNode(object):
    def __init__(self):
        self.solution = {}
        self.constraint_dict = {}
        self.cost = 0

    def __eq__(self, other):
        if not isinstance(other, type(self)): return NotImplemented
        return self.solution == other.solution and self.cost == other.cost

    def __hash__(self):
        return hash((self.cost))

    def __lt__(self, other):
        return self.cost < other.cost

class CBS(object):
    def __init__(self, environment):
        self.env = environment
        self.open_set = set()
        self.closed_set = set()

    def search(self):
        global count,coflict_spot,research_spot

        start = HighLevelNode()
        # TODO: Initialize it in a better way
        start.constraint_dict = {}
        for agent in self.env.agent_dict.keys():
            start.constraint_dict[agent] = Constraints()
        start.solution = self.env.compute_solution()
        if not start.solution:
            return {}
        start.cost = self.env.compute_solution_cost(start.solution)

        self.open_set |= {start}

        while self.open_set:
            P = min(self.open_set)
            self.open_set -= {P}
            self.closed_set |= {P}

            self.env.constraint_dict = P.constraint_dict
            conflict_dict = self.env.get_first_conflict(P.solution)
            print(conflict_dict)

            count +=1

            if research_spot ==False:
                if count ==20:

                    coflict_spot =True   
                else:
                    coflict_spot =False         
                
            else:
                print("探索不可にするばしょを再度変えます")
                if count == 23:               

                    coflict_spot =True 
                    break


            if not conflict_dict:
                print("solution found")

                return self.generate_plan(P.solution)

            constraint_dict = self.env.create_constraints_from_conflict(conflict_dict)
            
            for agent in constraint_dict.keys():
                new_node = deepcopy(P)
                new_node.constraint_dict[agent].add_constraint(constraint_dict[agent])

                self.env.constraint_dict = new_node.constraint_dict
                new_node.solution = self.env.compute_solution()
                if not new_node.solution:
                    continue
                new_node.cost = self.env.compute_solution_cost(new_node.solution)

                # TODO: ending condition
                if new_node not in self.closed_set:
                    self.open_set |= {new_node}

        return {}

    def generate_plan(self, solution):
        plan = {}
        for agent, path in solution.items():
            path_dict_list = [{'t':state.time, 'x':state.location.x, 'y':state.location.y} for state in path]
            plan[agent] = path_dict_list        
     

            #print(plan['agent1'][-1])           

        # maxlength = max([len(value) for value in plan.values()])
        # for i in plan:
        #     if len(plan[i]) < maxlength:
        #         plan[i] += [plan[i][-1] for j in range(maxlength-len(plan[i]))]
                        
            agent_goal.append(len(plan[agent]))
            agent_goal_num.append(agent_goal[-1])

            agent_num.append(int(agent[-1]))
            
            #print(agent_num)

            # if len(agent_goal_num) >=2:
            #     if agent_goal_num[0] > agent_goal_num[1] and agent_goal_num[0] != 1 and agent_goal_num[1] != 1:
            #         num =agent_num[0]

            #     elif agent_goal_num[0] < agent_goal_num[1] and agent_goal_num[0] != 1 and agent_goal_num[1] != 1:
            #         num =agent_num[1]

            #     elif 1 in agent_goal_num:
            #         num = agent_num[1] if agent_goal_num[1] == 1 else agent_num[0]

            #     else:
            #         num ="same"
            # else:
            #     num ="finish"

            #print(len(plan[agent]))
            

            # #1回目のcbsを打ち切る処理の作業(仮)
            # print(plan['agent1'][1]['t'])
            
            # for i in range (len(plan)): 
            #     for j in range(len(plan[agent])):
            #         if plan['agent'+str(i+1)][j]['x']

            #         print(plan['agent'+str(i+1)][j]['x'],plan['agent'+str(i+1)][j]['y'])
            #         if plan['agent'+str(i+1)][j]['x'] == agent_goal[i][0] and plan['agent'+str(i+1)][j]['y'] == agent_goal[i][1]:
            #             goal_reached =True
            #             break        
            #         else:
            #             goal_reached =False 
                        
            # if goal_reached==True:
            #     break  
                                                
            # for i in range (len(plan)): 
            #     if i == num:
            #         for j in range((agent_wait_num)):
            #             print(plan['agent'+str(num+1)][j]['x'],plan['agent'+str(num+1)][j]['y'])
            #             if plan['agent'+str(i+1)][j]['x'] == agent_goal[i][0] and plan['agent'+str(i+1)][j]['y'] == agent_goal[i][1]:
            #                 break        

            #         break
         
        #2回目のcbsを打ち切る処理の作業(仮)           
        # maxlength = max([len(value) for value in plan.values()])
        # for i in plan:
        #     if len(plan[i]) > maxlength:
                
        #         plan[i] += [plan[i][-1] for j in range(maxlength-len(plan[i]))]
                        
        #     for i in range (len(plan)): 
        #         if i == num:
        #             for j in range((agent_wait_num)):
        #                 print(plan['agent'+str(num+1)][j]['x'],plan['agent'+str(num+1)][j]['y'])
        #                 if plan['agent'+str(i+1)][j]['x'] == agent_goal[i][0] and plan['agent'+str(i+1)][j]['y'] == agent_goal[i][1]:
        #                     break        
        #     break
        # if isinstance(num, (int, float)):
        #     del plan['agent'+str(num)][:]
        # else:
        #     pass
        

        return plan

# def conflict_spot_map(dimension,obstacles,conflict):

#     #各エージェントが探索した経路の衝突スポット   
#     if dimension[0] -1 !=obstacles and coflict_spot ==True:
#         print("append")   
#         print(conflict)


def conflict_spot_maze(conflict):

    global dimension,obstacles
    #conflict_spot_map(dimension,obstacles,conflict)

def main():

    global coflict_spot,dimension,obstacles
    wait_del =0

    parser = argparse.ArgumentParser()
    parser.add_argument("param", help="input file containing map and obstacles")
    parser.add_argument("output", help="output file with the schedule")
    args = parser.parse_args()

    # Read from input file
    with open(args.param, 'r') as param_file:
        try:
            param = yaml.load(param_file, Loader=yaml.FullLoader)
        except yaml.YAMLError as exc:
            print(exc)

    #衝突した場所を記録するファイルを読み込む
    with open("conflict_maze.txt", "r") as file:
        map_data = file.read().strip()  # 改行を除去する

    dimension = param["map"]["dimensions"]
    obstacles = param["map"]["obstacles"]
    
    # print(map_data)
    
    # conflict_spot_map(dimension,obstacles)
       
#     #各エージェントが探索した経路の衝突スポット   
    print(map_data)
    if dimension[0] -1 !=obstacles and map_data != 0:
    # if dimension[0] -1 !=obstacles :
        #obstacles.append((map_data))
        #obstacles.append(int(map_data))  # 文字列を数値に変換して追加
        obstacles.append(tuple(map(int, map_data.strip("()").split(", "))))


        # obstacles.append((1,7))
        # obstacles.append((2,7))
        # obstacles.append((3,7))
        # obstacles.append((4,7))
        # obstacles.append((5,7))
        # obstacles.append((6,7))
        # obstacles.append((8,7))
        # obstacles.append((10,0))
        # obstacles.append((11,0))
        # obstacles.append((12,0))
        # obstacles.append((13,0))
        # obstacles.append((14,0))
        # obstacles.append((15,0))
        # obstacles.append((16,0))
        # obstacles.append((0,3))
        # obstacles.append((1,3))
        # obstacles.append((2,3))
        # obstacles.append((3,3))
        # obstacles.append((4,3))
        # obstacles.append((5,3))
        # obstacles.append((6,3))
        # obstacles.append((7,3))
        # obstacles.append((8,3))
        # obstacles.append((9,3))
        # obstacles.append((10,3))
        # obstacles.append((11,3))
        # obstacles.append((12,3))
        # obstacles.append((13,3))
        # obstacles.append((14,3))
        # obstacles.append((15,3))
        # obstacles.append((16,3))
        # obstacles.append((17,3))
        # obstacles.append((18,3))
        
    agents = param['agents']

    for i, agent in enumerate(agents):
        agent_goal.append(agent['goal'])

    env = Environment(dimension, agents, obstacles)

    # Searching
    cbs = CBS(env)
    solution = cbs.search()
    if not solution:
        print(" Solution not found" )
        return

    # Write to output file
    with open(args.output, 'r') as output_yaml:
        try:
            output = yaml.load(output_yaml, Loader=yaml.FullLoader)
        except yaml.YAMLError as exc:
            print(exc)

    output["schedule"] = solution
    output["cost"] = env.compute_solution_cost(solution)

    if len(output['schedule']['agent0'] ) < len(output['schedule']['agent1']) and len(output['schedule']['agent0'] ) !=1 and len(output['schedule']['agent1'] ) !=1:
        wait_del = len(output['schedule']['agent1'])- len(output['schedule']['agent0'])
        agent_num =1
        print("agent1")

        # for i in range(wait_del):
        #     output['schedule']['agent'+ str(agent_num)].pop()

    elif len(output['schedule']['agent1'] ) < len(output['schedule']['agent0'])  and len(output['schedule']['agent0'] ) !=1 and len(output['schedule']['agent1'] ) !=1:
        wait_del = len(output['schedule']['agent0'])- len(output['schedule']['agent1'])
        agent_num =0
        print("agent1")

    for i in range(wait_del):
        output['schedule']['agent'+ str(agent_num)].pop()
        
    else:
        wait_del =0
        print("same")
        #pass             

    print(output)

    file_count = 0
    for file_name in os.listdir():
        if file_name.startswith('fact_'):
            file_count += 1

    # ファイル名を決定する
    file_name = f"fact_{file_count+1}.yaml"

    # with open(file_name, 'w') as output_yaml: 
    #     yaml.safe_dump(output, output_yaml)

if __name__ == "__main__":
    main()
    # test()