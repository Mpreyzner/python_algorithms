
def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        if guess == item:
            return mid
        if guess < item:
            low = mid + 1
        if guess > item:
            high = mid - 1


result = binary_search(range(1, 20), 4)

print(result)
