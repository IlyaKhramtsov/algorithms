import collections


def person_is_seller(name):
    return name[-1] == 'm'


def search(name):
    search_queue = collections.deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person_is_seller(person):
                print(f'{person} is a mango seller!')
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False


graph = {'you': ['alice', 'bob', 'claire'], 'alice': ['peggy'], 'bob': ['mark', 'peggy'], 'claire': ['tom', 'jonny'],
         'peggy': [], 'mark': [], 'tom': [], 'jonny': []}

search('you')
