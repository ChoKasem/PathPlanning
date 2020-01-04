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
                 [1,1]]
explore_order = np.array(explore_order)
# print(explore_order[1])
# print(world[explore_order[1][0]][explore_order[1][1]])

# #not = 0 and not = start mean it's already explore
# #Breath First Search
count = 1

exploring = start
while exploring != goal:
    for i in explore_order:
        explore_next = exploring + i
        if explore_next[0] >=0 and explore_next[0] < total_row and explore_next[1] >=0 and explore_next[1] < total_col and world[explore_next[0]][explore_next][1] >= 0:
            queue.append(explore_next)
            world[explore_next[0]][explore_next[1]] = count
            count+=1
    exploring = queue[0]
    queue.pop(0)
    print(world)

