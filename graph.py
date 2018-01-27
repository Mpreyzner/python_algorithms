from collections import deque
# we create a graph with list of our friends and a friends of our friends
graph = dict()
graph['me'] = ['alice', 'bart', 'cecilia']
graph['bart'] = ['John', 'Patricia']
graph['alice'] = ['Patricia']
graph['cecilia'] = ['Tamara', 'Jarek'] # https://www.youtube.com/watch?v=e5uei2AFEaQ
graph['Patricia'] = []
graph['Tamara'] = []
graph['Jarek'] = []
graph['John'] = []


def person_is_seller(name):
    return name[-1] == 'm'  # last letter of name is m


def search(name):
    search_queue = deque()
    # create queue and add our friends to it
    search_queue += graph[name]
    searched = [] # so we wont search for the same person twice and it will prevent infinite loop
    while search_queue:
        person = search_queue.popleft()  # get first element from queue, pop left so it was first in
        if not person in searched:
            if person_is_seller(person):
                print(person + ' sells mango')
                return True
            else:
                search_queue += graph[person]  # we add persons friend to queue
                searched.append(person)
    return False

print('Is there a mango seller? ' + str(search('me')))

# execution time
# O(number_of_people + number_of_connections/edges)
# adding people to queue is O(1) per person so O(n) for n people
# searching every connection takes O(number_of_edges)
