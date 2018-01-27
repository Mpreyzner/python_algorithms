from collections import deque

graph = dict()
graph['wakeup'] = ['exercise', 'wash teeth', 'pack lunch']
graph['pack lunch'] = []

graph['wash teeth'] = ['breakfast']
graph['breakfast'] = []

graph['exercise'] = ['shower']
graph['shower'] = ['dress up']
graph['dress up'] = []


def is_last_element(name):
    if not graph[name]:
        return True
    else:
        return False


# def search(name):
#     search_queue = deque()
#     # create queue and add first graph level
#     search_queue += graph[name]
#     searched = []  # so we wont search for the same person twice and it will prevent infinite loop
#     while search_queue:
#         person = search_queue.popleft()  # get first element from queue, pop left so it was first in
#         if not person in searched:
#             if is_last_element(person): # end of branch
#                 # print(person + ' sells mango')
#                 return searched
#             else:
#                 search_queue += graph[person]  # we add persons friend to queue
#                 searched.append(person)
#     return searched

def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue: # while we havent explored the full tree
        current_node = search_queue.popleft()
        if not current_node in searched:
            search_queue += graph[current_node]
            searched.append(current_node)
    return searched


print(search('wakeup'))
