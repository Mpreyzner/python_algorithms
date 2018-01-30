# Subset sum problem is to find subset of elements that are selected from a given set whose sum adds up to a given number K
# We are considering the set contains non-negative values.
# It is assumed that the input set is unique (no duplicates are presented).

set = []

k = 42


def find_subset_that_sum_equals_k(set, k):
    return subset_util(set, [], k)


def subset_util(set, selected, k):
    temp_sum = sum(selected)
    if temp_sum == k:
        # base case
        print(selected)
        return True
    elif temp_sum > k:
        return False

    for i in range(len(set)):
        print(set)
        print(i)
        current = set[i]
        selected.append(current)
        set.remove(current)
        if subset_util(set, selected, k):
            return True
        else:
            print('backtrack')
            continue
    return False


# res = find_subset_that_sum_equals_k([10, 7, 8, 3, 4, 1,2,3,4], 42)
# res = find_subset_that_sum_equals_k([1,1], 3)

# print(res)
