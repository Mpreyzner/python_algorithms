import sys

# if(subset is satisfying the constraint)
#     print the subset
#     exclude the current element and consider next element
# else
#     generate the nodes of present level along breadth of tree and
#     recur for next levels

this = sys.modules[__name__]

# we can explicitly make assignments on it
this.total_nodes = 0
this.graph = dict()


def print_subsets(subset, size):
    print(subset)


def subset_sum(set, tuplet, set_size, tuplet_size, sum, nodes_count, target_sum):
    this.total_nodes += 1  # how do we solve it
    if sum == target_sum:
        print_subsets(tuplet, tuplet_size)

        # Exclude previously added item and consider next candidate
        # new_set = [n for n in set if n not in tuplet]
        # print(new_set)
        subset_sum(set, tuplet, set_size, tuplet_size - 1, sum - set[nodes_count - 1], nodes_count + 1, target_sum)
    else:
        # generate nodes along the breadth
        for i in range(nodes_count, set_size):
            not_first = tuplet[-1:]
            if not_first:
                this.graph[not_first.pop()] = set[i]

            tuplet.append(set[i])
            # tuplet[last_elem] = new elem
            # consider next level node (along depth)
            subset_sum(set, tuplet, set_size, tuplet_size + 1, sum + set[i], i + 1, target_sum)


def generate_subsets(set, size, target_sum):
    # what should be in tuplet vector
    # input is weights vector and target_sum
    subset_sum(set, [], size, 0, 0, 0, target_sum)


# weights = [10, 7, 5, 18, 12, 20, 15]
# generate_subsets(weights, len(weights), 35)
weights = [1, 1, 1, 1, 2, 2]
generate_subsets(weights, len(weights), 4)
print(this.graph)
# make it output a graph maybe
