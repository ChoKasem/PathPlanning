import numpy as np

#create world map
world = [[0,-1,-1,0,0,0,-1,-1,-1,0],
         [0,-1,-1,0,0,0,-1,-1,-1,0],
         [0,0,0,0,0,0,-1,-1,-1,0],
         [0,0,0,0,-1,0,0,0,-1,0],
         [0,0,0,-1,0,-1,0,0,-1,0],
         [0,0,0,-1,0,-1,0,0,0,0]]

world = np.array(world)
print(world)

start = [0,0]
goal = [5,9]
total_row, total_col = np.shape(world)

queue = []
# x = np.array(start) + np.array([0,1])

explore_order = [[0,1],
                 [-1,0],
                 [0,-1],
                 [1,0]]
explore_order = np.array(explore_order)
# print(explore_order[1])
# print(world[explore_order[1][0]][explore_order[1][1]])


# #Breath First Search
def BFS():
    count = 1
    exploring = np.array(start)
    while not all(exploring == goal):
        for i in explore_order:
            explore_next = exploring + i
            if explore_next[0] >=0 and explore_next[0] < total_row and explore_next[1] >=0 and explore_next[1] < total_col and world[explore_next[0]][explore_next][1] == 0 and not all(explore_next == start):
                queue.append(explore_next)
                world[explore_next[0]][explore_next[1]] = count
                count+=1
        if not queue:
            print("No Solution")
            break
        else:
            exploring = queue[0]
            queue.pop(0)
    print(world)

#Depth-First Search
def DFS():
    count = 1
    exploring = np.array(start)
    while not all(exploring == goal):
        for i in explore_order:
            explore_next = exploring + i
            if explore_next[0] >=0 and explore_next[0] < total_row and explore_next[1] >=0 and explore_next[1] < total_col and world[explore_next[0]][explore_next][1] == 0 and not all(explore_next == start):
                queue.append(explore_next)
                world[explore_next[0]][explore_next[1]] = count
                count+=1
        if not queue:
            print("No Solution")
            break
        else:
            exploring = queue[-1]
            queue.pop(-1)
    print(world)

def FowardIteration(): #And also like Dijkstra
    exploring = np.array(start)
    while not all(exploring == goal):
        for i in explore_order:
            explore_next = exploring + i
            if explore_next[0] >=0 and explore_next[0] < total_row and explore_next[1] >=0 and explore_next[1] < total_col and world[explore_next[0]][explore_next][1] == 0 and not all(explore_next == start):
                queue.append(explore_next)
                world[explore_next[0]][explore_next[1]] = world[exploring[0]][exploring[1]] + 1
        if not queue:
            print("No Solution")
            break
        else:
            exploring = queue[0]
            queue.pop(0)
    print(world)

def BackwardIteration():
    exploring = np.array(goal)
    while not all(exploring == start):
        for i in explore_order:
            explore_next = exploring + i
            if explore_next[0] >=0 and explore_next[0] < total_row and explore_next[1] >=0 and explore_next[1] < total_col and world[explore_next[0]][explore_next][1] == 0 and not all(explore_next == goal):
                queue.append(explore_next)
                world[explore_next[0]][explore_next[1]] = world[exploring[0]][exploring[1]] + 1
        if not queue:
            print("No Solution")
            break
        else:
            exploring = queue[0]
            queue.pop(0)
    print(world)

def Astar():
    exploring = np.array(start)
    queue = {}
    hctg = world.copy() #heuristic cost-to-goal
    ctc = world.copy() #cost-to-come
    while not all(exploring == goal):
        for i in explore_order:
            explore_next = exploring + i
            if explore_next[0] >=0 and explore_next[0] < total_row and explore_next[1] >=0 and explore_next[1] < total_col and world[explore_next[0]][explore_next][1] == 0 and not all(explore_next == start):
                ctc[explore_next[0]][explore_next[1]] = ctc[exploring[0]][exploring[1]] + 1
                hctg[explore_next[0]][explore_next[1]] = abs(explore_next[0] - goal[0]) + abs(explore_next[1] - goal[1])
                world[explore_next[0]][explore_next[1]] = hctg[explore_next[0]][explore_next[1]] + ctc[explore_next[0]][explore_next[1]]
                if world[explore_next[0]][explore_next[1]] not in queue:
                    queue[world[explore_next[0]][explore_next[1]]] = []
                queue[world[explore_next[0]][explore_next[1]]].append(explore_next)
        if not queue:
            print("No Solution")
        else:
            if len(queue[sorted(queue.keys())[0]]) > 1:
                minctcSpot = queue[sorted(queue.keys())[0]][0]
                minctc = ctc[queue[sorted(queue.keys())[0]][0][0]][queue[sorted(queue.keys())[0]][0][1]]
                for spot in queue[sorted(queue.keys())[0]]:
                    if minctc > ctc[spot[0]][spot[1]]:
                        minctc = ctc[spot[0]][spot[1]]
                        minctcSpot = spot
                exploring = minctcSpot
                queue[sorted(queue.keys())[0]].remove(minctcSpot)
            else:
                exploring = queue[sorted(queue.keys())[0]][0]
                queue[sorted(queue.keys())[0]].remove(exploring)
            if not queue[sorted(queue.keys())[0]]:
                del queue[sorted(queue.keys())[0]]
    print(world)

if __name__ == "__main__":
    # print("Backward")
    # BackwardIteration()
    # print("Forward")
    # FowardIteration()
    # print("BFS")
    # BFS()
    # print("DFS")
    # DFS()
    Astar()