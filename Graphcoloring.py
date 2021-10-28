# GRAPH COLORING- CONSTRAINTS SATISFACTION PROBLEM
 
# Vertices of Graph
nodes = {
    0: 'A',
    1: 'B',
    2: 'C',
    3: 'D',
    4: 'E',
}
 
# Graph connections
graph = {
    0: [2, 4],
    1: [2, 3, 4],
    2: [0, 1, 3],
    3: [1, 2, 3],
    4: [0, 1, 3],
}
 
# Colors to be assigned
colors = ["Red", "Green", "Blue"]
 
# Function which checks whether color assign to vertex
def check(node, colour):
    for i in graph[node]:
        # if vertex is present in col_graph and already colored
        # then make condition false
        if i in col_graph and col_graph[i] == colour:
            return False
    return True
 
 
# Function assign color to uncolor vertex
def assign(node, colour):
    col_graph[node] = colour      # assign color
 
 
n = 0       # stores number of vertices
i = 0       # store number of colors
col_graph={}
 
while n < 5:
    assigned = 0            # Initialize all color default values as 0 (False
    for i in range(3):      # 3 == Three colors
        # checking validity
        if check(n, i) == True:
            # Start coloring
            assign(n, i)
            n += 1
            assigned = 1    # Mark as assigned with color
            break
 
           
    if assigned == 0:
        prevas = 0
        for x in range(3):
            if check(n-1, (col_graph[n-1]+1)%3) == True:   # Backtracking
                assign(n,(col_graph[n-1]+1)%3)
                prevas = 1
                break
        if prevas == 0:
            n -= 1
 
 
# Print Solution
for key, value in col_graph.items():
    print(nodes[key] + " : " + colors[value])

