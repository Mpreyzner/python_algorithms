# algorithm for xxx in weighted graphs


# check how much road to neighbour costs
# try road by traveling through other nodes
# if cheaper update the cost
# we calculate minimum road (weights) to all the nodes skipping the target

graph = dict()
graph['start'] = dict()
graph['start']['a'] = 6
graph['start']['b'] = 2

graph['a'] = dict()
graph['a']['meta'] = 1
# we hold the cost in this too.... but they are straight road costs
graph['b'] = dict()
graph['b']['a'] = 3
graph['b']['meta'] = 5

graph['meta'] = dict()

infinity = float("inf") # cost of getting form start to given point
# if unknown then inf
costs = dict()
costs['a'] = 6
costs['b'] = 2
costs['meta'] = infinity

parents = dict()
parents['a'] = 'start'
parents['b'] = 'start'
parents['meta'] = None

processed = []


def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None

    for node in costs:
        cost = costs[node]
        # we check if the given node has cost lower than the nodes we already looped through
        # starting from infinity
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

node = find_lowest_cost_node(costs)

while node is not None:
    cost = costs[node]
    neighbors = graph[node]

    for neighbor in neighbors.keys():  # loop through all the node neighbors
        new_cost = cost + neighbors[neighbor]
        if costs[neighbor] > new_cost:  # if going trough neighbor is cheaper
            costs[neighbor] = new_cost  # then update the cost
            parents[neighbor] = node  # and set our node as parent to the cheapest neighbor
    processed.append(node)
    node = find_lowest_cost_node(costs)


result = dict((v,k) for k,v in parents.items())
# show result in from -> to form
print(result)
print(costs['meta'])


