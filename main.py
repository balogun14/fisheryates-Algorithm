import random

def list_shuffle(items):
    for i in range(len(items) -1, 0, -1):
        pick = random.randint(0, i)
        items[pick], items[i] = items[i], items[pick]

    return items


newlio = ['a', 'b', 'c', 'd', 'e']
newlio2 = list_shuffle(newlio)
print(newlio2)