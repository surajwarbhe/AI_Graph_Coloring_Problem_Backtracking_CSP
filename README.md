# GRAPH COLORING PROBLEM : CONSTRAINTS SATISFACTION PROBLEM (BACKTRACKING)
#
#
## AIM: 
#### Assignment on Constraint Satisfaction Problem and Implement graph coloring problem
#
# 
## THEORY:
### CONSTRAINTS SATISFACTION PROBLEM: 
#### Constraint Satisfaction Problems (CSPs) are mathematical questions defined as a set of objects whose state must satisfy a number of constraints. A constraint satisfaction problem (CSP) consists of-
- Variables: It will be a tuple with the variable names.
- Domains: It will be a dictionary with the variable names as keys, and the domains as values (in the form of any iterable you want).
- Constraints will be a list of tuples with two components each: a tuple with the variables involved in the constraint, and a reference to a function that checks the constraint.
 
### BACKTRACKING ALGORITHM:
#### Backtracking is an algorithmic-technique for solving problems recursively by trying to build a solution incrementally, one piece at a time, removing those solutions that fail to satisfy the constraints of the problem at any point of time.
 
### BACKTRACKING APPROACH: 
#### The idea is to assign colors one by one to different vertices, starting from the vertex 0. Before assigning a color, check for safety by considering already assigned colors to the adjacent vertices i.e check if the adjacent vertices have the same color or not. If there is any color assignment that does not violate the conditions, mark the color assignment as part of the solution. If no assignment of color is possible then backtrack and return false.
#
# 
## ALGORITHM:
```
1. Create a recursive function that takes the graph, current index, number of vertices, and output color array.

2. If the current index is equal to the number of vertices. Print the color configuration in the output array.

3. Assign a color to a vertex (1 to m).

4. For every assigned color, check if the configuration is safe, (i.e. check if the adjacent vertices do not have the same color) recursively call the function with next index and number of vertices

5. If any recursive function returns true break the loop and return true.

6. If no recursive function returns true then return false.

```
#
# 
## QUESTION:
![image](https://docs.huihoo.com/boost/1-33-1/libs/graph/doc/figs/sequential_vertex_coloring.png)
#
# 
## OUTPUT:
```

A : Red
B : Red
C : Green
D : Blue
E : Green

```
#
#
## CONCLUSION:
- From this assignment, we learnt the concept of Constraints Satisfaction Problem and Backtracking algorithm in Artificial Intelligence.
- Also, implement Graph Coloring problem of Graph using Backtracking algorithm.

