#
# def get_hash(item):
#     return len(item)
#
#
# def add_to_hash_table(name, value, table):
#     # table[get_hash(name)] = value
#     table.insert(get_hash(name), value)
#     return table
#
#
# def get_value(name, book):
#     hash = get_hash(name)
#     print(hash)
#     print(book)
#     # return book.
#
# book = []
# book = add_to_hash_table('apple', 0.99, book)
# book = add_to_hash_table('orange', 0.5, book)
# book = add_to_hash_table('pear', 0.33, book)
# book = add_to_hash_table('tomato', 0.66, book)

# print(book)
#
# # print(get_value('tomato', book))
#
#
# for index, item in enumerate(book):
#         print (index, item)


voted = {}


def check_voter(name):
    if voted.get('name'):
        print('Get out')
    else:
        voted.update(name=True)
        # the assigment voted[name] did not work
        # why
        print('You can vote')


while True:
    name = input('Enter the name of the voter:' + "\n")
    check_voter(name)
