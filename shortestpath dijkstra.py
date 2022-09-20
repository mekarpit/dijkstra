#DRIVER CODE of edges for directed-graph

from cmath import inf

branch = int(input("enter no of branches: "))

edges = {}
for l in range(branch):
    print("Enter first verticies for branch {}".format(l+1))
    a1 = input()
    print("Enter second verticies for branch {}".format(l+1))
    a2 = input()
    print("Enter distance between node for branch{}".format(l+1))
    d1 = int(input())
    edges[(a1,a2)] = d1

start = input("enter starting point: ")
end_node = input("Enter end point: ")


#program

res1, res2 = map(list, zip(*edges))
node_vertices = list(set(res1 + res2)) # v--> list of nodes present
node_len = len(edges)

node_cost = {j: inf for j in node_vertices}
node_cost[start]=0

# print("node_vertices",node_vertices)
# print("nodecost",node_cost)

spath = {v: {} for v in node_vertices}
for (u,v), w_uv in edges.items():
    spath[u][v] = w_uv
    spath[v][u] = w_uv    

visited=[]
final_cost = {}

route={}

for i in range(len(node_vertices)):
    # print("initial cost",node_cost)
    u = min(node_cost,key=node_cost.get)
    # print(u)
    for v in spath[u]:
        if v in visited:
            pass
        else:
            # print("old ",v,'value is',node_cost[v])
            if node_cost[v]>node_cost[u]+spath[u][v]:
                node_cost[v]=node_cost[u]+spath[u][v]
                # print("new ",v,"value is ",node_cost[u]+spath[u][v])
                route[v]=u
    visited.append(u)
    final_cost[u]=node_cost[u]
    # print("final cost",final_cost)
    del node_cost[u]
    del spath[u]

spathroute=[]
print("maximum distance is : ",final_cost[end_node])
def routespath(end_node,route):
    if end_node in route:
        spathroute.append(end_node)
        last = route[end_node]
        return routespath(last,route)
    else:
        spathroute.append(end_node)
        print(spathroute)
        

    
routespath(end_node,route)

finish = input()