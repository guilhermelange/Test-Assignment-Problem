def update_instance(a,b,c,d,e):
    global distance, similarity, desks, tests, empty

    distance = a
    similarity = b
    desks = c
    tests = d
    empty = e

def set_timeout(a):
    global timeout
    timeout = a

def set_strategy(a):
    global strategy
    strategy = a


def get_values():
    return distance, similarity, desks, tests, empty, timeout