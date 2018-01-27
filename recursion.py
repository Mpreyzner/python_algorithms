def count_down(n):
    print(n)
    if n > 0:
        count_down(n -1)


# count_down(50)

def factorial(x):
    print('x equals:' + str(x))
    if x == 1:
        return 1
    return x * factorial(x - 1)


# print(factorial(6))

def sum_array(array):
    print(array)
    if len(array) == 0:
        return 0
    elif len(array) == 1:
        return array[0]

    last = array.pop()
    array[0] += last
    return sum_array(array)


# sum = sum_array([1,2,3])
# print(sum)
